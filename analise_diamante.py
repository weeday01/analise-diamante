import pandas as pd



arquivo = 'diamonds.csv'

data = pd.read_csv(arquivo, index_col = 0, sep=',', decimal='.')






