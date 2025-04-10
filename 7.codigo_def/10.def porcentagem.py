import os
os.system("clear||cls")



def porcentagem(preco):
    

    if preco < 100: 
       valor = preco * 1.10 
    elif preco >= 100:
        valor = preco * 1.20   
    return valor

    
    
    
preco = int(input("digite o preço do produto: "))    

valor = porcentagem(preco)

print(f"o valor com a tarrifa fica no total de: {valor:.2f}")