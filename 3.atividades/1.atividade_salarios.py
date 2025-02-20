import os 
os.system("clear")

#calcule quantos salarios minimos uma pessoa recebe com base que o salario minimo e R$1350

salario = float(input("digite seu salario: "))


salario_minimo = 1350

print(f"voçe ganha: {salario / salario_minimo} salarios minimos")

if salario <1350:
      print("acesso negado")
      print("menos que um salario minimo")