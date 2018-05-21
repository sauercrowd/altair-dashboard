from chart_handler import ChartHandler
from main_handler import MainHandler
import tornado

class AltairDashboard:
    def __init__(self):
        self.charts=[]
    def add_chart(self, name, chart):
        self.charts.append({
            'name': name,
            'chart': chart,
        })

    def listen(self, hostname, port):
        handlers = []
        for chart in self.charts:
            handlers.append(("/chart/"+chart["name"], ChartHandler, dict(chart=chart["chart"], name=chart["name"])))
        handlers.append((r'/', MainHandler, dict(active_charts=[chart['name'] for chart in self.charts])))
        app =  tornado.web.Application(handlers)
        app.listen(port)
        tornado.ioloop.IOLoop.current().start()
