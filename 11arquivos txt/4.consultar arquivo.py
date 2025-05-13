import os
from dataclasses import dataclass
from time import sleep

os.system("clear")

@dataclass
class Paciente:
    nome: str
    idade: int


lista_paciente = []

for i in range(2):
    print("digite os dados do paciente!")
    paciente = Paciente( 
        nome = input("digite o nome do paciente: "),
        idade = input("digite a idade: ") 
    )
    lista_paciente.append(paciente)
    print()
    
nome_arquivo = "dados_pacientes.txt"    

print("SALVANDO DADOS NO ARQUIVO!.")
with open (nome_arquivo, "a") as arquivos_paciente:
    for paciente in lista_paciente:
        arquivos_paciente.write(f"{paciente.nome}\n{paciente.idade}\n\n")
        
print("SALVO COM SUCESSO!")

print("\nacessando dados em arquivos.")
try:
    with open (nome_arquivo, "r") as arquivos_paciente:
        linhas = arquivos_paciente.readlines()    
        for linha in linhas:
            print(f"- {linha.strip()}")
       
except FileExistsError:
    print("o arquivo não foi encontrado")
        
    