# -*- coding: utf-8 -*-
from flask import Flask, make_response


OK_PAGE = """<html>
<body>
<a href="/ok">Should work</a>
<a href="/ok">Should work (but not be checked twice)</a>
<a href="ok">Should also work</a>
<a href="/ok.gif">Should also work</a>

<a href="http://www.google.com/">Should not be called</a>
<a href="/blacklisted">Should not be called</a>
<a href="/darklist">Should not be called</a>
</body>
</html>"""

KO_PAGE = """<html>
<body>
<a href="/oops">Toto</a>
</body>
</html>"""

UTF8_AND_ENTITIES_PAGE = """
<html>
<body>

<input type="text" name="test_utf_8_with_entities"
                   value="printemps &amp; été" />

</body>
</html>"""


def create_app():

  app = Flask(__name__)

  @app.route("/ok")
  def ok():
    return OK_PAGE

  @app.route("/utf8_and_entities")
  def utf8_and_entities():
    return UTF8_AND_ENTITIES_PAGE

  @app.route("/ko")
  def ko():
    return KO_PAGE

  @app.route("/ok.gif")
  def ok_img():
    response = make_response("")
    response.headers['content-type'] = "image/gif"
    return response

  return app
