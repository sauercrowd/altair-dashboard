from altair_dashboard import AltairDashboard
import altair as alt
import pandas as pd
import numpy as np

def make_chart():
    x = np.arange(0, 50, 1)
    y = np.random.rand(50)
    data = []
    for i in range(len(x)):
        data.append([x[i],3 + y[i]])
    df = pd.DataFrame(data, columns=['x', 'y'])
    c = alt.Chart(df).mark_line().encode(
        x= "x",
        y= "y"
    ).interactive()
    return c


def getLiveData(state, force):    
    if force:
        state = {'count':0}
        return make_chart(), state
    
    # only update every 4th iteration
    if state is not None and "count" in state and state["count"] < 4:
        state["count"] += 1
        return None, state

    c = make_chart()
    state = {'count':0}
    return c, state

dashboard = AltairDashboard()
dashboard.add_chart("Live Chart", freshdatafn=getLiveData)
dashboard.listen(port=8080)
