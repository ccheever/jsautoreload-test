import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""
<html>
<head>
<title>JS Autoreload Test</title>
<script src="/index.js" type="text/javascript"></script>
</head>
<body>
What does the fox say?
</body>
</html>
""")

class JSHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(file("../build/index.js").read())

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/index.js", JSHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


