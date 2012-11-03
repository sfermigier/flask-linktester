from flask import Flask

OK_PAGE = """<html>
<body>
<a href="/ok">Toto</a>
</body>
</html>"""

KO_PAGE = """<html>
<body>
<a href="/oops">Toto</a>
</body>
</html>"""


def create_app():

  app = Flask(__name__)

  @app.route("/")
  def index():
    return OK_PAGE

  @app.route("/ok")
  def ok():
    return OK_PAGE

  @app.route("/ko")
  def ko():
    return KO_PAGE

  return app
