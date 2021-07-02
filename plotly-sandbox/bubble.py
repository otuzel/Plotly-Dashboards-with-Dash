import pandas as pd
from plotly.graph_objs.graph_objs import YAxis
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')

data = [go.Scatter(x=df['horsepower'], 
                    y=df['mpg'], 
                    mode='markers',
                    marker=dict(size=df['cylinders'] * 2,
                                color=df['weight'],
                                showscale=True
                                ),
                    text=df['name'],
)]

layout = go.Layout(title='mpg vs. horsepower', 
                    xaxis=dict(title='Horse power'),
                    yaxis=dict(title='mpg'),
                    hovermode='closest',
                    )

figure = go.Figure(data=data, layout=layout)
pyo.plot(figure)