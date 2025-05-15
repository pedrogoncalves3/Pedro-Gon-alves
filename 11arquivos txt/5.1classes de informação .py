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

@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str


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

def salvar_dados_em_arquivo(nome_arquivo: str, dados: list, tipo: str):
    print(f"SALVANDO DADOS NO ARQUIVO {nome_arquivo}!")
    with open(nome_arquivo, "a") as arquivo:
        for item in dados:
            if tipo == "funcionario":
                arquivo.write(f"Nome: {item.nome}\nAdmissão: {item.admissao}\nMatrícula: {item.matricula}\nEndereço: {item.endereco}\n\n")
            elif tipo == "cliente":
                arquivo.write(f"Nome: {item.nome}\nData de nascimento: {item.nascimento}\nEndereço: {item.endereco}\n\n")
    print("Dados salvos com sucesso!\n")

# Salvar os dados em arquivos separados
salvar_dados_em_arquivo("dados_do_funcionario.txt", lista_funcionario, "funcionario")
salvar_dados_em_arquivo("dados_do_cliente.txt", lista_cliente, "cliente")