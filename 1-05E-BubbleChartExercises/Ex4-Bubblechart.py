#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import pandas as pd
from plotly.graph_objs.graph_objs import YAxis
import plotly.offline as pyo
import plotly.graph_objs as go


# create a DataFrame from the .csv file:
df = pd.read_csv('data/mpg.csv')

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['weight'] * 0.45, 
                    y=df['horsepower'], 
                    mode='markers',
                    marker=dict(size=(df['weight'] / df['acceleration'])/10,
                                color=df['weight'],
                                showscale=True
                                ),
                    text=df['name']
)]

layout = go.Layout(title='Horsepower vs. Weight', 
                    xaxis=dict(title='Weight'),
                    yaxis=dict(title='Horse power'),
                    hovermode='closest',
                    )

figure = go.Figure(data=data, layout=layout)
pyo.plot(figure)














# create a layout with a title and axis labels







# create a fig from data & layout, and plot the fig
