import os
from dataclasses import dataclass
os.system("clear")

# criando uma classe.
@dataclass
class pessoa:
    nome: str
    idade: int
    
 
#aplicando caracteristicas
pessoa1 = pessoa ("alice", 30)
pessoa2 = pessoa ("bob", 25)

print("\n dados da pessoa:")
print(f" {pessoa1.nome},idade: {pessoa1.idade}")
print(f" {pessoa2.nome},idade: {pessoa2.idade}")

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
    