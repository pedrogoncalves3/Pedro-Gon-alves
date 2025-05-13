import os
from dataclasses import dataclass
from time import sleep

os.system("clear")

@dataclass
class Funcionario:
    nome: str
    admisao: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    nascimento: str
    endereco: str

def coletar_dados_funcionario(quantidade_repeticao: int):
    lista_funcionario = []
    for _ in range(quantidade_repeticao):
        print("Dados do funcionário")    
        funcionario = Funcionario(
            nome=input("Digite seu nome: "),
            admisao=input("Digite a data da admissão: "),
            matricula=input("Digite sua matrícula: "),
            endereco=input("Digite seu endereço: ")     
        )
        lista_funcionario.append(funcionario)
        print()
    return lista_funcionario

def coletar_dados_cliente(quantidade_repeticao: int):
    lista_cliente = []
    for _ in range(quantidade_repeticao):
        print("Dados do cliente!")    
        cliente = Cliente(
            nome=input("Digite seu nome: "),
            nascimento=input("Digite a data do seu nascimento: "),
            endereco=input("Digite o seu endereço: ") 
        )
        lista_cliente.append(cliente)
        print()
    return lista_cliente

def salvar_dados_em_arquivo(nome_arquivo: str, dados: list, tipo: str):
    print(f"SALVANDO DADOS NO ARQUIVO {nome_arquivo}!")
    with open(nome_arquivo, "a") as arquivo:
        for item in dados:
            if tipo == "funcionario":
                arquivo.write(f"nome: {item.nome}\nadmissão: {item.admisao}\nmatrícula: {item.matricula}\nendereço: {item.endereco}\n\n")
            elif tipo == "cliente":
                arquivo.write(f"nome: {item.nome}\ndata de nascimento: {item.nascimento}\nendereço: {item.endereco}\n\n")
    print("Dados salvos com sucesso!\n")

def main():
    QUANTIDADE_REPETICAO = 1

    # Coletar dados dos funcionários e clientes
    lista_funcionario = coletar_dados_funcionario(QUANTIDADE_REPETICAO)
    lista_cliente = coletar_dados_cliente(QUANTIDADE_REPETICAO)

    # Salvar dados nos arquivos
    salvar_dados_em_arquivo("dados_do_funcionario.txt", lista_funcionario, "funcionario")
    salvar_dados_em_arquivo("dados_do_cliente.txt", lista_cliente, "cliente")

if __name__ == "__main__":
    main()
    