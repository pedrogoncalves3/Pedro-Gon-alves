import os
import time 
os.system("clear")

#função para verificar se a lista esta vazia
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        print(f"\nA lista esta vazia!")
        return True
    return False # se a lista possuir algum conteudo

#função para adicionar nomes
def adicionar(lista_nomes):
    nome = input("digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso!")
    
 
# função pa4ra mostrar nomes
def mostrar(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return
    

    print(f"\n===lista de nomes===")    
    for nome in lista_nomes:
        print(f"- {nome}")
    
# função para atualizar nomes:
def atualizar(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return
    
    mostrar(lista_nomes)
    nome_antigo = input(f"\nDigite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input(f"digite o novo nome para {nome_antigo}: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}")
    else:
        print(f"\n O nome {nome_antigo} não doi encontrado. ")
            
# função para excluir nomes
def excluir(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return
    
    mostrar(lista_nomes)
    
    nome_remover = input("digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"{nome_remover} removido com sucesso!")
    else:
        print(f"o nome {nome_remover} não foi encontrado.")    

nomes = [] #criando lista de nomes

# menu
while True:
    print(f"gerenciador de nomes!\n")
    print("1 - adicionar")
    print("2 - Lista")
    print("3 - Atualizar")
    print(f"4 - Excluir\n")
    
    opcao = int(input("Digite uma das opções acima: "))
    
    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            mostrar(nomes)
        case 3:
            atualizar(nomes)
        case 4:
            excluir(nomes)
        case 5: 
            print(f"\nSaindo do programa.")    
            break
        case _:
            print("opção invalida.\ntente novamente!")
    if opcao != 1:
        time.sleep(1)
    os.system("clear||cls")            
            
            
                        
        





























