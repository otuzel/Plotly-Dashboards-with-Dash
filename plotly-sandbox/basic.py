import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x,
                    y=random_y,
                    mode='markers',
                    marker=dict(
                        size=20,
                        color='rgb(24,134,32)',
                        symbol='pentagon',
                        line=dict(width=2)
                    ))]
layout = go.Layout(title='Hi First Plot',
                    xaxis=dict(title='My Random X'),
                    yaxis=dict(title='My Random Y'),
                    hovermode ='closest'
                    )

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter.html')