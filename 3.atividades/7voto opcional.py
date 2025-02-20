import os
os.system("clear")

nome = input("digite seu nome: ")
idade = int(input("digite sua idade para verificar se e obrigatorio votar: "))

if idade >= 18 and  idade <65: 
    print("obrigatorio avotar!")
elif idade < 16:
    print("não pode votar:")    
elif idade == 16 or idade == 17:
    print("seu voto e opcional!")     
else: 
    print("não e obrigatorio a votar!")