
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
    nome = input("digite o nome: "),
    email = input("informe seu E-mail: "),
    telefone = input("informe o telefone: ")
)
lista_clientes.append(cliente)
print()

for cliente in lista_clientes:
    print("_____exibindo reultado do livro!_____")
    print(f"titulo do livro: {cliente.nome}")    
    print(f"autor do livro: {cliente.email}")   
    print(f"ano de lançamento: {cliente.telefone}")  
print()

