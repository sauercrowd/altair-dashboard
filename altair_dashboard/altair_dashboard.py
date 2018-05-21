import tornado
from .handlers import ChartHandler
from .handlers import MainHandler
from .dashboard import DashboardChart

name = "altair_dashboard"

class AltairDashboard:
    def __init__(self):
        self.arefunctions = False
        self.charts = []
    def add_chart(self, name, chart=None, freshdatafn=None):
        chart = DashboardChart(name=name, chart=chart, datafn=freshdatafn)
        self.charts.append(chart)

    def listen(self, address="localhost", port=8080):
        handlers = []
        i = 0
        for chart in self.charts:
            handlers.append(("/chart/"+str(i), ChartHandler, dict(chart=chart)))
            i+=1
        handlers.append((r'/', MainHandler, dict(active_charts=[chart.name for chart in self.charts])))
        app =  tornado.web.Application(handlers)
        app.listen(port, address=address)
        tornado.ioloop.IOLoop.current().start()
