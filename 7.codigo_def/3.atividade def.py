import os
os.system("clear")
from time import sleep

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = { i * numero}")



nu1 = int(input("digite o número que deseja para ver a tabuada: "))
tabuada(nu1)