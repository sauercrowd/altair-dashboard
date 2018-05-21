import sys
sys.path.insert(0,'..')
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

c = alt.Chart(df).mark_line().encode(
    x="x",
    y="y",
    color="type"
).interactive() | alt.Chart(df).mark_bar().encode(
    x= alt.X("x", bin=True),
    y= "sum(y)",
    color="type"
).interactive()

dashboard = AltairDashboard()
dashboard.add_chart("test",c)
dashboard.listen("localhost",8080)