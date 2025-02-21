import os

#limpa terminal 

os.system("clear")


nome = input("digite seu nome aqui: ")
idade = int(input("digite sua idade: "))
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite a nota da segunda unidade: "))


#exibindo dados:
print()
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"soma_dos_numero: {numero1 + numero2}")
print(f"soma_dos_numero: {numero1 - numero2}")
print(f"soma_dos_numero: {numero1 / numero2}")
print(f"soma_dos_numero: {numero1 * numero2}")