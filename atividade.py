# -*- coding: utf-8 -*-
"""Atividade

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KODvCGuYTifAYcNT-yJI15sL5MAMWGRv
"""

import numpy as np
import matplotlib.pyplot as plt

anos = np.array([2010, 2011, 2012, 2014, 2017, 2018, 2019])
vendas = np.array([723, 814, 905, 1087, 1360, 1451, 1542])

coef = (vendas[-1] - vendas[0]) / (anos[-1] - anos[0])
print("Coeficiente Angular:", coef)

def prever_vendas(ano):
    return vendas[0] + coef * (ano - anos[0])

vendas_2021 = prever_vendas(2021)
vendas_2023 = prever_vendas(2023)
print("Previsão de vendas em 2021:", vendas_2021)
print("Previsão de vendas em 2023:", vendas_2023)

plt.plot(anos, vendas, marker='o', linestyle='-', color='b')
plt.title('Vendas ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()

import numpy as np
from sklearn.linear_model import LinearRegression

anos = np.array([2010, 2011, 2012, 2014, 2017, 2018, 2019]).reshape(-1, 1)
vendas = np.array([723, 814, 905, 1087, 1360, 1451, 1542])

modelo = LinearRegression()
modelo.fit(anos, vendas)

def prever_vendas(ano):
    return modelo.predict([[ano]])

ano_desejado = 2020
vendas_ano_desejado = prever_vendas(ano_desejado)
print("Previsão de vendas em", ano_desejado, ":", vendas_ano_desejado[0])