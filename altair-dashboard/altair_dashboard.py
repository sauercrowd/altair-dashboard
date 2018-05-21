from chart_handler import ChartHandler
from main_handler import MainHandler
import tornado
from collections import namedtuple
import altair as alt

class AltairDashboard:
    def __init__(self):
        self.charts=[]
    def add_chart(self, name, chart):
        chart = DashboardChart(name=name, chart=chart)
        self.charts.append(chart)

    def listen(self, address="localhost", port=8080):
        handlers = []
        i = 0
        for chart in self.charts:
            handlers.append(("/chart/"+str(i), ChartHandler, dict(chart=chart.chart, name=chart.name)))
            i+=1
        handlers.append((r'/', MainHandler, dict(active_charts=[chart.name for chart in self.charts])))
        app =  tornado.web.Application(handlers)
        app.listen(port, address=address)
        tornado.ioloop.IOLoop.current().start()

DashboardChart = namedtuple('DashboardChart', ['name', 'chart'])