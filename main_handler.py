import tornado

htmlstr = """
<!DOCTYPE html>
<html>
<head>
  <!-- Import Vega 3 & Vega-Lite 2 (does not have to be from CDN) -->
  <script src="https://cdn.jsdelivr.net/npm/vega@3"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@2"></script>
  <!-- Import vega-embed -->
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@3"></script>
</head>
<body>

<div id="vis"></div>

<script type="text/javascript">
  var spec = "/chart/test";
  vegaEmbed('#vis', spec).then(function(result) {
    // access view as result.view
  }).catch(console.error);
</script>
</body>
</html>
"""

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, active_charts):
        self.active_charts = active_charts
    def get(self):
        self.write(htmlstr)
