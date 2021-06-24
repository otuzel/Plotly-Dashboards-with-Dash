#######
# Objective: Create a histogram that plots the 'length' field
# from the Abalone dataset (../data/abalone.csv).
# Set the range from 0 to 1, with a bin size of 0.02
######

# Perform imports here:
from plotly.graph_objs.graph_objs import XBins
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/abalone.csv')
print(df.columns)
# create a DataFrame from the .csv file:


# create a data variable:

data = [
  go.Histogram(
    x=df['length'],
    xbins=dict(start=0, end=1, size=0.02)
  )
]

layout = go.Layout(
  title="my chart"
)

fig=go.Figure(data=data, layout=layout)

pyo.plot(fig)

# add a layout




# create a fig from data & layout, and plot the fig
