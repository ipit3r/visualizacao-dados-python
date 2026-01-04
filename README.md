# projects
Projeto Visualização de Dados para visualizar em sua máquina:

## 📊 Visualização de Dados

1. **Prepare o ambiente:**
   ```bash
   pip install pandas matplotlib numpy plotly

2. **Garanta os dados:** 

Certifique-se de que o arquivo NetflixRevenue.csv está na mesma pasta do código.

3. **Rode o script:**

```
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from pandas import read_csv

# --- 1. Gráfico de Barras: População Mundial ---
paises = ('Índia', 'China', 'Estados Unidos', 'Indonésia', 'Paquistão')
indice = np.arange(len(paises))
populacao = [1428000000, 1425000000, 334600000, 281600000, 232900000]

plt.bar(indice, populacao)
plt.xticks(indice, paises)
plt.ylabel('População')
plt.title('Países mais populosos de 2023')
plt.show()

# --- 2. Mapa Coroplético Interativo ---
data = go.Choropleth(
    locations=['IND', 'CHN', 'USA', 'IDN', 'PAK'],
    locationmode='ISO-3',
    colorscale='YlGnBu',
    z=populacao,
    text=['1.428 bilhão', '1.425 bilhão', '334,6 milhões', '281,6 milhões', '232,9 milhões'],
    colorbar=dict(title='População')
)
map = go.Figure(data=[data])
map.show()

# --- 3. Séries Temporais: Receita Netflix ---
# Nota: Certifique-se que o arquivo CSV está no diretório correto
series = read_csv("NetflixRevenue.csv", header=0, index_col=0, parse_dates=True)
series.plot()   
plt.title('Evolução da Receita - Netflix')
plt.show()
```
