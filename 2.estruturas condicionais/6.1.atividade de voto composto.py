import os 
os.system("clear")

nome = input("digite seu nome: ")
idade = int(input("digite sua idade para verificarmos se e obrigado a votar: "))

if idade < 18 or idade > 65:
    input("não e obrigado a voltar! ")
else:
    input("e obrigado a votar")    