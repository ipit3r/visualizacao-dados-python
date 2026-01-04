# 📈 Explorando Dados: População e Tendências de Mercado!

Olá!!! Este projeto nasceu de um desafio da minha graduação em Ciência da Computação, onde o objetivo era ir além dos números e usar o *Python* para dar vida a dados reais. 

Como profissional que atua com planejamento e dados (PCM), acredito que uma boa visualização é a ponte entre a informação bruta e a decisão inteligente.

## 💡 O que este projeto resolve?
A ideia aqui foi criar análises diferentes, usando três perspectivas diferentes, duas para entender o mesmo conjunto de dados e uma para entender a tendência do mercado de Streammings:

1.  **Onde está o volume? (Gráfico de Barras):** Uma comparação direta para entender rapidamente quem são os gigantes populacionais de 2023.
2.  **Como isso se distribui no mapa? (Visualização Geográfica):** Usei o `Plotly` para criar um mapa interativo que traz contexto espacial, facilitando a visão global que as tabelas escondem.
3.  **Para onde o mercado está indo? (Séries Temporais):** Analisei a receita da Netflix para mostrar como os dados evoluem ao longo do tempo, identificando tendências de crescimento.

## 🛠️ Ferramentas que utilizei
Para construir essa análise, utilizei as biblioteca de dados do Python:
* **Pandas** para organizar a "casa" (limpeza e manipulação).
* **Matplotlib & Seaborn** para a estética dos gráficos estáticos.
* **Plotly** para dar interatividade ao mapa mundial.

## 📊 Resultados
Segue abaixo linha de código em conjunto com o gráfico gerado:

```

# --- 1. Gráfico de Barras: População Mundial ---
paises = ('Índia', 'China', 'Estados Unidos', 'Indonésia', 'Paquistão')
indice = np.arange(len(paises))
populacao = [1428000000, 1425000000, 334600000, 281600000, 232900000]

plt.bar(indice, populacao)
plt.xticks(indice, paises)
plt.ylabel('População')
plt.title('Países mais populosos de 2023')
plt.show()
```

*Gráfico Gerado:*

![Cinco países mais populosos em gráfico de barras](Plot1.png)

```

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

```
*Gráfico Gerado:*

![Cinco países mais populosos em gráfico geográfico.](Plot2.png)

```

# --- 3. Séries Temporais: Receita Netflix ---
# Nota: Certifique-se que o arquivo CSV está no diretório correto
series = read_csv("NetflixRevenue.csv", header=0, index_col=0, parse_dates=True)
series.plot()   
plt.title('Evolução da Receita - Netflix')
plt.show()

```
*Gráfico Gerado:*

![Dataset sobre Receita e Assinantes da Netflix por região em gráfico de linhas.](Plot3.png)

```
