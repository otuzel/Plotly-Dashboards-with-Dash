#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv('data/abalone.csv')
print(df)


data = [
  go.Box(
    y=np.random.choice(df['rings'], 100, replace=False),
    name='Set 1'
  ),
  go.Box(
    y=np.random.choice(df['rings'], 100, replace=False),
    name='Set 2'
  )
]

layout = go.Layout(
  title='Comparison of random samples'
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)



# add a layout




# create a fig from data & layout, and plot the fig
