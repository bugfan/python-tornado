import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("Hello, world "+story_id+"\n")  # 获取restful url参数

    def post(self):
        # self.set_header("Content-Type", "application/json")
        self.write("test post \n"+str(self.request.body))  # 获取body信息

    # 使用了这个装饰器之后，你必须调用 self.finish() 以完成 HTTP 请求，否则 用户的浏览器会一直处于等待服务器响应的状态
    @tornado.web.asynchronous
    def put(self):
        self.write("test put 装饰器\n")
        self.finish()


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,  # 跨站伪造请求的防范
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/story/([0-9]+)", MainHandler),  # 正则匹配id
])  # ,**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
