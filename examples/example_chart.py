#import altair_dashboard
from altair_dashboard import AltairDashboard
import altair as alt
import pandas as pd

df = pd.DataFrame([
    [1,2,"x"],
    [2,3,"x"],
    [3,7,"x"],
    [1,3,"y"],
    [2,5,"y"],
    [3,1,"y"],
], columns=["x","y","type"])

c1 = alt.Chart(df).mark_line().encode(
    x="x",
    y="y",
    color="type"
).interactive()

c2 = alt.Chart(df).mark_bar().encode(
    x= "x:O",
    y= "sum(y)",
    color="type"
).interactive()

dashboard = AltairDashboard()

dashboard.add_chart("Line Chart", c1)
dashboard.add_chart("Bar Chart", c2)
dashboard.add_chart("Both Charts", c1 | c2)

dashboard.listen(port=8080)
