import pandas as pd
import plotly.express as px

df = pd.read_csv("Class 103/Project-103/Copy+of+data+-+data.csv")
fig = px.scatter( df, x='Date', y='Cases', color= 'Country')
fig.show()