import bd
from datetime import datetime

#programa utilizado para calcular o indice a partir de uma data específica
data = datetime(2023,3,15)
print("Data calcula: " + str(data.date()))
bd.salvar_indice(data.date())
