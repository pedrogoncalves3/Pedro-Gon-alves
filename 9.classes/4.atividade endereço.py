import os
os.system("clear")
from dataclasses import dataclass
from time import sleep


@dataclass
class Endereco:
    logradouro: str
    numero: int
    
@dataclass
class pessoa:
    nome: str
    idade: int
    endereco: Endereco
    
    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}\nnúmero: {self.endereco.numero}")
        
        
endereco1 = Endereco("rua A",23)
pessoa1 = pessoa("marta",44,endereco1)
pessoa1.exibir_dados()

print()

endereco2 = Endereco("rua A",23)
pessoa2 = pessoa("marta",44,endereco2)
pessoa2.exibir_dados()
    

