# SQLwithPandas

Utilizando linguagem SQL para realizar consultas em Pandas DataFrames

Objetivo do código: automatizar um relatório de quantos animais um pesquisador já utilizou do saldo total aprovado para experimentos pela CEUA (Comissão de Ética de Uso Animal)<br>
Observação: ao utilizar animais para experimentação é necessário que o pesquisador especifique quantos animais serão utilizados na pesquisa de modo que ele não pode ultrapassar o quantitativo total. O Biotério que fornece esses animais é responsável por garantir que esse limite seja respeitado. <br>
Como existem centenas de pesquisadores com centenas de projetos aprovados foi necessário gerar um código que gerasse o relatório comparando o total do certificado com o total já utilizado pelo pesquisador e qual o saldo restante.<br>
Assim o programa gerado funciona da seguinte forma:<br>
1 - Ler a planilha com os dados de demanda de animais(tabela filha) e os dados do protocolo CEUA  (tabela pai).<br>
2 - Transforma cada planilha em dataframes.<br>
3 - É realizado queries utilizando a linhagem SQL através do biblioteca Python "SQLAlchemy".<br>
4 - Os resultados das consultas são salvas como Dataframe.<br>
5 - Por fim, o programa gera um arquivo excel com as consultas geradas.<br>
<br>
Dessa forma, o relatório gerado retorna o nome do pesquisador, o número do projeto, o total do projeto, o total já retirado e o saldo disponível para retirada.

