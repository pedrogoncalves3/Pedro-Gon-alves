import os 
os.system("clear")

nome = input("digite seu nome: ")
idade = int(input("digite sua idade para verificarmos se e obrigado a votar: "))

if idade >=18 and idade <=65:
    input("obrigado a voltar! ")
else:
    input("não e obrigado a voltar!")    