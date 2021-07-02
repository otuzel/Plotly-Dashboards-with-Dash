import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

data = [
  # go.Histogram(
  #   x=df['mpg'],
  #   xbins=dict(start=10, end=50, size=5),
  #   opacity=0.75
  # ),
  go.Histogram(
    x=df['weight'],
        xbins=dict(start=1000, end=5000, size=100),

    opacity=0.75
  )
]


layout = go.Layout(
  title='Mpg frequencies'
)

fig=go.Figure(data=data, layout=layout)
pyo.plot(fig)