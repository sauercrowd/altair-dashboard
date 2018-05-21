import tornado.ioloop
import tornado.web

class ChartHandler(tornado.web.RequestHandler):
    def initialize(self, chart, name):
        self.name = name
        self.chart = chart
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(self.chart.to_json())
