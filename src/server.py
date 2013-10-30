#!/usr/bin/env python

import os

import tornado.ioloop
import tornado.web

def relative_path(fn):
    return os.path.abspath(os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-1]) + os.path.sep + fn)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""
<html>
<head>
<title>JS Autoreload Test</title>
<link rel="stylesheet" type="text/css" href="/style.css">
</head>
<body>
What does the fox say?
<script src="/react.js" type="text/javascript"></script>
<script src="/index.js" type="text/javascript"></script>
<script src="//localhost:35729/livereload.js"></script>
</body>
</html>
""")

class JSHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(file(relative_path("../js/index.js")).read())

class ReactHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(file(relative_path("../../bower_components/react/react.min.js")).read())

class StyleHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(file(relative_path("../css/style.css")).read())

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/index.js", JSHandler),
    (r"/react.js", ReactHandler),
    (r"/style.css", StyleHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


