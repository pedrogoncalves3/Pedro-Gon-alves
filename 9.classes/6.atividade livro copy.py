import os
from time import sleep
from dataclasses import dataclass

os.system("clear")

@dataclass
class Autor:
    nome: str
    biografia: str
    
class livro:
    titulo: str
    ano: int 
    autor: Autor        
    
    
lista_livro = []
QUANTIDADE_CLIENTES = 1
 
print("_____pedindo informções!_____")
print()

for i in range(QUANTIDADE_CLIENTES):
    autor =Autor(
        nome_livro = input("digite o titulo do livro: "),
        autor_livro = input("digite o autor do livro: "),
        ano_livro = input("digite o ano em que foi lançado: "), 
    )   
    lista_livro.append(autor)
    print()
    
    
    
for autor in lista_livro:
    print("_____exibindo reultado do livro!_____")
    print(f"titulo do livro: {autor.nome_livro}")    
    print(f"autor do livro: {autor.autor_livro}")   
    print(f"ano de lançamento: {autor.ano_livro}")       