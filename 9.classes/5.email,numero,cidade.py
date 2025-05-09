import os
from time import sleep
from dataclasses import dataclass

os.system("clear")

@dataclass
class Autor:
    nome: str
    biografia: str
    
@dataclass
class livro:
    titulo: str
    ano: int 
    autor: Autor        
    

 
print("_____pedindo informções!_____")
print()


autor = Autor(
    nome_livro = str(input("digite o titulo do livro: ")),
    autor_livro = str(input("digite o autor do livro: ")),
    ano_livro = int(input("digite o ano em que foi lançado: "))
)
autor.exibir_detahes()

def exibir_Deltlhes(self):
    print("_____exibindo reultado do livro!_____")
    print(f"titulo do livro: {self.autor.nome}")    
    print(f"autor do livro: {self.autor.autor_livro}")   
    print(f"ano de lançamento: {self.autor.ano_livro}")  
print()
    
    
    
