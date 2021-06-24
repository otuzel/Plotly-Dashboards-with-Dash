#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo



# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('Data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']



data = []
for day in days:
    # What should go inside this Scatter call?
    trace = go.Scatter(x=df['LST_TIME'], y=df[df['DAY'] == day]['T_HR_AVG'], mode='lines', name=day)
    data.append(trace)



# Define the layout
layout = go.Layout(title='Weather Report')

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)