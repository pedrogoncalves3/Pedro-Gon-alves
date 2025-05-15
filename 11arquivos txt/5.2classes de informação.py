import os
from dataclasses import dataclass
from time import sleep

os.system("clear")


lista_funcionario = []
lista_cliente = []
QUANTIDADE_REPETICAO = 1


@dataclass
class Funcionario:
    nome: str
    admissao: str
    matricula: str
    endereco: str

def salvar_funcionarios(lista):
    nome_arquivo = "dados_funcionarios.csv"
    with open(nome_arquivo, "a") as arquivo_funcionarios:
        for funcionario in lista:
            arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.admissao}, {funcionario.matricula}, {funcionario.endereco}\n")

    print("Salvando dados dos funcionários...")


@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str
    
    
def salvar_clientes(lista):
    nome_arquivo = "dados_clientes.csv"
    with open(nome_arquivo, "a") as arquivo_funcionarios:
        for cliente in lista:
            arquivo_funcionarios.write(f"{cliente.nome}, {cliente.nascimento}, {cliente.endereco}\n")
    
    print("Salvando dados dos clientes...")    


for i in range(QUANTIDADE_REPETICAO):
    print("Dados do funcionário")    
    funcionario = Funcionario(
        nome=input("Digite seu nome: "),
        admissao=input("Digite a data da admissão: "),
        matricula=input("Digite sua matrícula: "),
        endereco=input("Digite seu endereço: ")
    )
    lista_funcionario.append(funcionario)
    print()


for i in range(QUANTIDADE_REPETICAO):
    print("Dados do cliente")    
    cliente = Cliente(
        nome=input("Digite seu nome: "),
        nascimento=input("Digite a data de seu nascimento: "),
        endereco=input("Digite o seu endereço: ") 
    )
    lista_cliente.append(cliente)
    print()


salvar_funcionarios(lista_funcionario)
salvar_clientes(lista_cliente)