import tornado

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, active_charts):
        self.active_charts = active_charts
    def get(self):
        self.render('main_handler.html', charts=self.active_charts)
