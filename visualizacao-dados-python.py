import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
        
paises = ('Índia', 'China', 'Estados Unidos', 'Indonésia', 'Paquistão')
indice = np.arange(len(paises))
populacao = [1428000000,1425000000,334600000,281600000,232900000]
plt.bar(indice, populacao)
plt.xticks(indice, paises)
plt.ylabel('População')
plt.title('Países mais populosos de 2023')

plt.show()

import plotly.graph_objects as go

data = go.Choropleth(
    locations=['IND', 'CHN', 'USA', 'IDN', 'PAK'],
    locationmode='ISO-3',
    colorscale='YlGnBu',
    z=[1428000000, 1425000000, 334600000, 281600000, 232900000],
    text=['1.428 bilhão', '1.425 bilhão', '334,6 milhões', '281,6 milhões', '232,9 milhões'],
    colorbar=dict(title='População')
)

layout = go.Layout(geo=dict(showframe=False, showcoastlines=False))
map = go.Figure(data=[data], layout=layout)
map.show()

from pandas import read_csv
from matplotlib import pyplot

series = read_csv(r"NetflixRevenue.csv", header=0, index_col=0, parse_dates=True)
series.plot()   
pyplot.show()