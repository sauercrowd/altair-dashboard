class DashboardChart:
    def __init__(self, name, chart=None, datafn=None):
        self.name = name
        self.chart = chart
        self.datafn = datafn
        self.state = {}
    def get_chart(self, force):
        if self.datafn is not None:
            chart, new_state =  self.datafn(self.state, True)
            if chart is None:
                chart = self.chart
            print("State: {}".format(new_state))
            self.state = new_state
            self.chart = chart
            return chart
        return self.chart
    def get_name(self):
        return self.name
        
