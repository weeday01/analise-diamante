import os
import pandas as pd

path = os.getcwd() #os.listdir()

arquivo = 'c:\\Users\\arthu\\OneDrive\\Documentos\\analise_diamantes\\archive.zip'

dados = pd.read_csv(arquivo, index_col = 0, sep=',', decimal='.')


