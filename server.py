import tornado.httpclient
import tornado.httpserver
import tornado.web

from tornado.options import define, options

define('port', default=8080, type=int)


class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r'/get_url', GetUrlHandler)
        ]

        tornado.web.Application.__init__(self, handlers)


class GetUrlHandler(tornado.web.RequestHandler):
    def get(self):
        url = self.get_argument('url')

        http_request = tornado.httpclient.HTTPRequest(url=url)

        http_client = tornado.httpclient.HTTPClient()

        response = http_client.fetch(http_request)

        self.set_status(response.code)
        self.write(response.body)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Application())
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
