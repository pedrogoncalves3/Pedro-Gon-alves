import os 
os.system("clear")

nome = (input("digite seu nome: "))
idade = int(input("digite sua idade: "))
nu1 = float(input("digite um número: "))
nu2 = float(input("digite outro número: "))

media = (nu1 + nu2)/2
soma = (nu1 + nu2)
divisao = (nu1 / nu2)

print (f"nome: ",nome)
print (f"idade: ",idade)
print (f"media",media)
print (f"soma",soma)
print (f"divisao",divisao)
