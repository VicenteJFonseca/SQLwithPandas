import os
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


!pip install -U pandasql
!pip install SQLAlchemy==1.4.46


ddemanda_animais = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/Datasets/mices_rats/pedidos22_23.xlsx",
                                sheet_name = ['demanda','ceua'])
ceua = demanda_animais.get('ceua')
solicitacao = demanda_animais.get('demanda')

from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

q = """ SELECT * FROM ceua; """

ceua2 = pysqldf(q)

q2 = """ SELECT [Protocolo na CEUA], Quantidade FROM solicitacao """

pedidos_ceua = pysqldf(q2)

q3 = """ 
SELECT [Protocolo na CEUA], SUM(Quantidade) AS "Solicitado por CEUA"
FROM solicitacao
GROUP BY [Protocolo na CEUA];
"""

pedidos_por_ceua = pysqldf(q3)

pedidos_por_ceua.rename(columns={'Protocolo na CEUA': 'COD_CEUA'}, inplace = True)

q4 = """
SELECT ceua.Pesquisador,
ceua.COD_CEUA,
ceua.Quantidade,
pedidos_por_ceua.[Solicitado por CEUA]
FROM ceua
INNER JOIN pedidos_por_ceua
ON ceua.COD_CEUA = pedidos_por_ceua.COD_CEUA;
"""

qtd_ceua = pysqldf(q4)

q5 = """ 
SELECT Pesquisador,
COD_CEUA,
Quantidade,
[Solicitado por CEUA],
(Quantidade - [Solicitado por CEUA]) AS "Saldo"
FROM qtd_ceua
WHERE Saldo < 0
ORDER BY "Saldo" ASC;
"""

saldo_ceua = pysqldf(q5)

relatorio = saldo_ceua.sort_values( by = ['Saldo'], ascending = True)
relatorio = relatorio.astype({'Solicitado por CEUA':'int','Quantidade':'int','Saldo':'int'})
relatorio = relatorio.astype({'Solicitado por CEUA':'int','Quantidade':'int','Saldo':'int'})
relatorio.rename(columns={'Quantidade':'Quantidade do protocolo'}, inplace = True)
linhas_duplicadas = relatorio[relatorio.duplicated('COD_CEUA')]
relatorio = relatorio.drop_duplicates(subset=['COD_CEUA'])

q6 = """
SELECT Pesquisador,
SUM(Saldo) AS "Total por Pesquisador"
FROM relatorio
GROUP BY Pesquisador
ORDER BY "Total por Pesquisador" ASC;
"""

total_pesquisador = pysqldf(q6)

with pd.ExcelWriter(r'/content/drive/MyDrive/Colab Notebooks/Datasets/mices_rats/relatorios_ceua_excedentes.xlsx') as relatorios:
    relatorio.to_excel(relatorios, sheet_name='total_por_ceua')
    total_pesquisador.to_excel(relatorios, sheet_name='total_por_pesquisador') 