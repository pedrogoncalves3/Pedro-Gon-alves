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
pessoa1 = pessoa(
    nome = input("digite seu nome: "),
    idade = int(input("digite sua idade: ")),
    peso = float(input("digite seu peso: ")),
    altura = float(input("digite sua altura: ")),      
    )
 
print() 
 
pessoa2 =pessoa(
    nome = input("digite seu nome: "),
    idade = int(input("digite sua idade: ")),
    peso = float(input("digite seu peso: ")),
    altura = float(input("digite sua altura: ")),      
) 
 
os.system("clear")

print(f"dados da primeira pessoa: \n° {pessoa1.nome}\nidade: {pessoa1.idade},\npeso: {pessoa1.peso},\naltura: {pessoa1.altura}") 
print()
print(f"dados da segunda pessoa: \n° {pessoa2.nome}\nidade: {pessoa2.idade}\npeso: {pessoa2.peso}\naltura: {pessoa2.altura}") 

@dataclass
class pet:
    nome: str
    idade: int
    peso: float
  
print()   
print("=====Preencha as informações do seu Pet e aguarde ser chamado(A)=====")
print()

pet1 =pet(
    nome = input("digite o nome: "),
    idade = int(input("digite a idade: ")),
    peso = float(input("digite o peso: ")),     
    ) 



print("\n dados do cachorro:")
print(f"Dados do Pet: \n° {pet1.nome}\nidade: {pet1.idade},\npeso: {pet1.peso}") 


    