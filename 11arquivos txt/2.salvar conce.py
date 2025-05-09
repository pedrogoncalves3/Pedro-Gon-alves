import os
from dataclasses import dataclass
from time import sleep

os.system("clear")


@dataclass
class Loja_carros:
    marca: str
    modelo: str
    categoria: str
    preco: float
    
lista_carros = []
QUANTIDADE_CLIENTE = 2

print("_____pedindo informções!_____")

for i in range(QUANTIDADE_CLIENTE):
    loja_carros = Loja_carros(
        marca = input("digite a marca do carro: "),
        modelo = input("qual o modelo do carro: "),
        categoria = input("digite a categoria do carro: "),
        preco = input("informe o preco do carro: ") 
                    
    )   
    lista_carros.append(loja_carros) 
print()   
 
for loja_carros in lista_carros:
    print("_____exibindo reultado!_____")
    print(f"marca do carro: {i+1} {loja_carros.marca}")    
    print(f"modelo: {loja_carros.modelo}")   
    print(f"categoria: {loja_carros.categoria}")  
    print(f"preco: {loja_carros.preco}") 
    
    
print()
#salvar arquivo txt
print("_____salvando os dados do cliente_____")
nome_arquivo = "2. salvar informações de carros"

with open (nome_arquivo,"a") as arquivos:
    for loja_carros in lista_carros:
        arquivos.write(f"marca do carro: {loja_carros.marca}\nmodelo: {loja_carros.modelo}\ncategoria: {loja_carros.categoria}\npreço: {loja_carros.preco}\n\n\n")
        print()
        
print("Dados salvo com sucesso!\ntenha um bom dia!")        


    