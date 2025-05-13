

import os
from time import sleep
from dataclasses import dataclass

os.system("clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    
lista_clientes = []    
    
    
print("_____pedindo informções!_____")

cliente = Cliente(
    nome = input("digite o nome do jogo: "),
    email = input("informe o E-mail utilizado: "),
    telefone = input("informe o telefone: ")
)
lista_clientes.append(cliente)
print()

for cliente in lista_clientes:
    print("_____exibindo reultado do livro!_____")
    print(f"nome do jogo: {cliente.nome}")    
    print(f"email utilizado: {cliente.email}")   
    print(f"telefone: {cliente.telefone}")  
print()



#salvar arquivo txt
print("_____salvando os dados do cliente_____")
nome_arquivo = "1.0salvar informações de login"

# w -> escrita/salvar/sobrescrever
#  escrita/salvar/acumular

with open (nome_arquivo,"a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"nome do jogo: {cliente.nome}\nE-mail utilizado: {cliente.email}\ntelefone: {cliente.telefone}\n\n\n")
        print()
        
print("Dados salvo com sucesso!\ntenha um bom dia!")        