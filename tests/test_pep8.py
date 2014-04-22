from unittest import TestCase
import pep8

import os


class TestPep8(TestCase):

  black_list = ['docs']
  expected = ['E111', 'E121', 'E401', 'E127']

  def test_pep8(self):
    root_dir = os.path.join(os.path.dirname(__file__), os.path.pardir)
    root_dir = os.path.normpath(root_dir)

    py_files = []

    for root, dirs, files in os.walk(root_dir):
      for dir in dirs[:]:
        if dir.startswith(".") or dir == 'env' or dir.endswith(".egg"):
          dirs.remove(dir)
          continue
        for black_listed in self.black_list:
          if dir == black_listed:
            dirs.remove(dir)
            continue
      for name in files:
        if name.endswith(".py"):
          py_files.append(os.path.join(root, name))

    for py_file in py_files:
      checker = pep8.Checker(py_file)
      num_errors = checker.check_all(expected=self.expected)
      assert num_errors == 0, "PEP8 errors found in file %s" % py_file
