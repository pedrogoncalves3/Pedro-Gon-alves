import os
from dataclasses import dataclass
os.system("clear")

# criando uma classe.
@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
    
 
#aplicando caracteristicas
pessoa1 = pessoa (input("digite seu nome: "),input("digite a sua idade: "),input("digite seu peso: "),(input("digite sua altura: ")))
os.system("clear")
pessoa2 = pessoa (input("digite seu nome: "),input("digite a sua idade: "),input("digite seu peso: "),(input("digite sua altura: ")))

os.system("clear")

print(f"dados da primeira pessoa: \n° {pessoa1.nome},idade: {pessoa1.idade},peso: {pessoa1.peso},altura: {pessoa1.altura}") 
print(f"dados da segunda pessoa: \n° {pessoa2.nome},idade: {pessoa2.idade},peso: {pessoa2.peso},altura: {pessoa2.altura}") 

@dataclass
class pet:
    nome: str
    idade: int
    peso: float
    

pet1 = pet ("kevin", 3,6.4)
pet2 = pet ("bob", 2,4.6)

print("\n dados do cachorro:")
print(f" {pet1.nome},idade: {pet1.idade},peso: {pet1.peso}")
print(f" {pet2.nome},idade: {pet2.idade},peso{pet2.peso}")    
    