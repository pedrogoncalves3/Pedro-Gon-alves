import os 
os.system("clear")


# criando lista
lista_de_compras = []
quantidade = 3

# solicitando dados ao usuario
print("=LISTA DE COMPRAS=")
for i in range(quantidade):
    item = input(f"digite o {i+1}ª item a sua lista: ")
    lista_de_compras.append(item)

# exibindo itens da lista de compras 
os.system("clear")
for i, item in enumerate(lista_de_compras , start =1):
    print(f"{i}ª item: {item}")   