#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pandas.io.formats import style
import plotly.graph_objs as go


# Launch the application:
app = dash.Dash()


# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
	dcc.RangeSlider(
		id='slider',
		min=-10,
		max=10,
		marks={i: i for i in range(-10,10)},
		step=1,
		value= [-3,3]
	),
	html.Div(id='output', style={'padding': '20px'})
])


# Create a Dash callback:
@app.callback(Output('output', 'children'), [
	Input('slider', 'value')
])
def calculate(vals):
	return vals[0] * vals[1]

# Add the server clause:
if __name__ == '__main__':
    app.run_server()
