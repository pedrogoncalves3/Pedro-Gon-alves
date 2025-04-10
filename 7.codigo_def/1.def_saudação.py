import os
os.system("clear")

# função sem retorno
def saudacao (nome):
    print(f"ola {nome}! bem-vindo(a) ao curso de DS!")

nome_visitante = "marta" 


# crie uma função com o nome disciplina que receba o nome de 
# uma disciplina do curso de DS
# mostre o texto: a disciplina ***** faz parte do curso de DS

def disciplina(nome):
    print(f"a disciplina {nome} faz parte do curso de DS! ")


nome = input("digite seu nome: ")
nome_disciplina = input("digite o nome da disciplina: ")



saudacao(nome)  
disciplina(nome_disciplina)   
 