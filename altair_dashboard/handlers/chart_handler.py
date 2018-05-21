import tornado.ioloop
import tornado.web

class ChartHandler(tornado.web.RequestHandler):
    def initialize(self, chart):
        self.chart = chart
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(self.chart.get_chart(True).to_json())
