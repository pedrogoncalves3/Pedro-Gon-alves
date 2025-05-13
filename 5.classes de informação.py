import os
from dataclasses import dataclass
from time import sleep

os.system("clear")

lista_funcionario = []
lista_cliente = []
QUANTIDADE_REPETICAO = 3

@dataclass
class Funcionario:
    nome = str
    admisao = str
    matricula = str
    endereco = str
    
@dataclass
class Cliente:
    nome = str
    nascimento = str
    endereco = str
    
for i in range(QUANTIDADE_REPETICAO):
    print("Dados do funcionário")    
    funcionario = Funcionario(
            nome = input("Digite seu nome: "),
            admisao = input("Digite a data da admissão: "),
            matricula = input("Digite sua matrícula: "),
            endereco = input("Digite seu endereço: ")
    
    )
    lista_funcionario.append(funcionario)
print()
    
    
nome_arquivo = "dados do funcionario.txt"     
   
for i in range(QUANTIDADE_REPETICAO):
    print("Dados do cliente!")    
    cliente = Cliente(
        nome = input("digite seu nome: "),
        nascimento = input("digite a data de seu nascimento: "),
        endereco = input("digite o seu endereço: ") 
    )
    lista_cliente.append(cliente)
    print()
    
nome_arquivo = "dados do cliente.txt"       

def salvar_dados_em_arquivo(nome_arquivo: str, dados: list, tipo: str):
    print(f"SALVANDO DADOS NO ARQUIVO {nome_arquivo}!")
    with open(nome_arquivo, "a") as arquivo:
        for item in dados:
            if tipo == "funcionario":
                arquivo.write(f"nome: {item.nome}\nadmissão: {item.admisao}\nmatrícula: {item.matricula}\nendereço: {item.endereco}\n\n")
            elif tipo == "cliente":
                arquivo.write(f"nome: {item.nome}\ndata de nascimento: {item.nascimento}\nendereço: {item.endereco}\n\n")
    print("Dados salvos com sucesso!\n")