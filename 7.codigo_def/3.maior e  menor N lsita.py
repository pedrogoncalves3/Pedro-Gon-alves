import os 
os.system("clear")


# criando lista
lista_numeros = []


def determinar_numeros(lista_numeros):
    menor = min(lista_numeros)
    maior = max(lista_numeros)
    return menor,maior



# solicitando dados ao usuario  
print("=LISTA DE NUMEROS=")
for i in range(5):
    item = int(input(f"digite o {i+1}ª item a sua lista: "))
    lista_numeros.append(item)


lista = determinar_numeros(lista_numeros)   


# exibindo itens da lista de compras 
os.system("clear")
for i, item in enumerate(lista_numeros , start =1):

 print(f"{i}ª item: {item}")  
print()  
print(f"maior número: {lista[1]}")   
print(f"menor número: {lista[0]}")   