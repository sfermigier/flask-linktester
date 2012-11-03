# -*- coding: utf-8 -*-
"""
Test the application by clicking on all the links.

Some links are blacklisted due to side effects.
"""

from HTMLParser import HTMLParser
import urlparse

__all__ = ['LinkTester']


class LinkExtractor(HTMLParser):

  def __init__(self):
    HTMLParser.__init__(self)
    self.links = set()

  def handle_starttag(self, tag, attrs):
    for attr_name, attr_value in attrs:
      if (tag, attr_name) in [('a', 'href'), ('link', 'href'), ('script', 'src'), ('img', 'src')]:
        url = attr_value
        scheme = urlparse.urlparse(url).scheme
        if scheme != '':
          continue
        link = urlparse.urldefrag(url)[0]
        self.links.add(link)


class LinkTester(object):

  _black_list = set(["/logout"])

  def __init__(self, client, root):
    self.client = client
    self.to_visit = set([root])
    self.black_list = self._black_list.copy()
    self.visited = set()
    self.allowed_codes = set([200, 301])
    self.verbosity = 0

  def blacklisted(self, url):
    for path in self.black_list:
      if path.endswith("*"):
        if url.startswith(path[0:-1]):
          return True
      else:
        if url == path:
          return True
    return False

  def crawl(self):
    while self.to_visit:
      link = self.to_visit.pop()
      if not link or link in self.visited:
        continue

      if self.verbosity >= 1:
        print "Crawling URL:", link

      response = self.client.get(link)

      if self.verbosity >= 2:
        print "  Got response:", response

      status_code = response.status_code
      assert status_code in self.allowed_codes,\
        "Response from URL %s was %s" % (link, response.status_code)

      if self.verbosity >= 2:
        print "  Got content-type:", response.content_type
        print "  Got body:", response.data

      if not response.content_type.startswith('text/html'):
        continue

      self.visited.add(link)
      parser = LinkExtractor()
      parser.feed(response.data)

      if self.verbosity >= 2:
        print "  Found links:", parser.links

      for new_link in parser.links:
        if not new_link.startswith("/"):
          new_link = link.split("?")[0] + new_link
        if self.blacklisted(new_link):
          continue
        if new_link not in self.visited:
          self.to_visit.add(new_link)
