# Sorteio dos grupos da copa
from random import randint
import sys
import time

cabecas_1 = ["FRANCA", "BELGICA", "BRASIL", "CROACIA", "URUGUAI", "INGLATERRA", "PORTUGAL", "SUICA"]

cabecas_2 = ["ESPANHA", "DINAMARCA", "ARGENTINA", "CHILE", "SUECIA", "COLOMBIA", "ALEMANHA", "MEXICO"]

cabecas_3 = ["HOLANDA", "POLONIA", "GALES", "ITALIA", "EUA", "TUNISIA", "AUSTRIA", "SENEGAL"]

cabecas_4 = ["SLOVAKIA", "ROMENIA", "IRLANDA", "UKRANIA", "PARAGUAI", "VENEZUELA", "IRA", "BOSNIA"]

grupos = []
for i in range(0, 8):
    print(i)
    grupos.append([])
    selecionado_grupo_1 = randint(0, 7 - i)
    selecionado_grupo_2 = randint(0, 7 - i)
    selecionado_grupo_3 = randint(0, 7 - i)
    selecionado_grupo_4 = randint(0, 7 - i)

    grupos[i].append(cabecas_1[selecionado_grupo_1])
    grupos[i].append(cabecas_2[selecionado_grupo_2])
    grupos[i].append(cabecas_3[selecionado_grupo_3])
    grupos[i].append(cabecas_4[selecionado_grupo_4])

    cabecas_1 = cabecas_1[:selecionado_grupo_1] + cabecas_1[selecionado_grupo_1 + 1:]
    cabecas_2 = cabecas_2[:selecionado_grupo_2] + cabecas_2[selecionado_grupo_2 + 1:]
    cabecas_3 = cabecas_3[:selecionado_grupo_3] + cabecas_3[selecionado_grupo_3 + 1:]
    cabecas_4 = cabecas_4[:selecionado_grupo_4] + cabecas_4[selecionado_grupo_4 + 1:]

    print(grupos[i])