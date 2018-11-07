from random import randint
import sys
import time

# Conforme a posicao do time no ranking atual da fifa ele será atribuido uma forca aleatoria para cada selecao

atributosTimes_1 = [randint(40, 50) for i in range(0, 8)]
atributosTimes_2 = [randint(30, 50) for i in range(0, 8)]
atributosTimes_3 = [randint(20, 50) for i in range(0, 8)]
atributosTimes_4 = [randint(10, 50) for i in range(0, 8)]

print(atributosTimes_1)
time.sleep(5)
print(atributosTimes_2)
time.sleep(5)
print(atributosTimes_3)
time.sleep(5)
print(atributosTimes_4)