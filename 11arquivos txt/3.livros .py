import os
from dataclasses import dataclass
from time import sleep

os.system("clear")

lista_Livros = []

@dataclass
class Livro:
    livro: str
    autor: str
    categoria: str
    preco: float
    
lista_livros = []
QUANTIDADE_REPETICAO = 1

for i in range(QUANTIDADE_REPETICAO):
    print("digite os dados do ator!!")
    livros = Livro( 
        livro = input("digite o nome do livro: "),
        autor = input("digite o nome do autor do livro:  "),
        categoria = input("categoria do livro: "),
        preco = input("digite o valor do livro: ") 
    )
    lista_livros.append(livros)
    print()    
    

nome_arquivo = "dados do livro.txt"     

print("SALVANDO DADOS NO ARQUIVO!.")
with open (nome_arquivo, "a") as arquivos_livros:
    for livros in lista_livros:
        arquivos_livros.write(f"{livros.livro}\n{livros.autor}\n{livros.categoria}\n{livros.preco}\n\n")
        
    
print("\nACESSANDO DADOS NO ARQUIVO\nAGUARDE!.")
sleep(2)
try:
    with open (nome_arquivo, "r") as arquivos_livros:
        linhas = arquivos_livros.readlines()    
        for linha in linhas:
            print(f"- {linha.strip()}")
       
except FileExistsError:
    print("o arquivo não foi encontrado")
                
        