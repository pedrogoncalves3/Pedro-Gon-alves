import os
os.system("clear")

maca = 1.30


maca_comprada = float(input("digite a quantidade de maca: "))

if maca_comprada >=12:
    maca = 1.00

total = (maca_comprada*maca)

print(f"a quantidade de maças foi: {maca_comprada} o preço total foi: {total}")
    