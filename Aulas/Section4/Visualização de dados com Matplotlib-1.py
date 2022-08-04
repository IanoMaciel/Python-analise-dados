from turtle import color
from matplotlib import markers
from matplotlib.lines import _LineStyle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# gráfico de linhas
np.random.seed(7)
y = np.random.randint(low=1, high=1500, size=10)

plt.plot(y)


# insere a primeira linha no plot 
plt.plot(
    y,
    color='#c4f0ff',
    marker='o',
    ms=5,
    mec='k',
    markerfacecolor='w',
    ls='-.'
)

# insere a segunda linha no plot 
plt.plot(
    y*2,
    marker='+',
    color='k',
    ms=5
)

# rótulos
plt.xlabel('Eixo X', color ='red', size=12)
plt.ylabel('Eixo Y')
plt.title('Title', loc='center')

# gridlines
plt.grid(
    axis='y',
    color = '#e4e4e4',
    linestyle='--',
    linewidth=1,
    alpha=0.8
)
plt.show()