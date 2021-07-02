import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('SourceData/nst-est2017-alldata.csv')

df2 = df[df['DIVISION']== '1']
df2.set_index('NAME', inplace=True)
list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]
print(df2)
data = [go.Scatter(x=df2.columns,y=df2.loc[name],mode='lines ',name=name) for name in df2.index]

pyo.plot(data)