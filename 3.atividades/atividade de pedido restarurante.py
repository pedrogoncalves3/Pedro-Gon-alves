import os

#limpa terminal 

os.system("clear")

print("""
======CARDAPIO======
codigo \tprato  \tpreço

1    picanha            25.00
2    Lasanha            20.00
3    Strogonoff         18,00
4    Bife Acebolado     15,00
5    Pão com ovo        5,00      


""")


nome = input("nome que deseja no seu pedido: ")
opcao = str(input("digite a opcção desejada: "))




match opcao:
    case '1':
        print(f"picanha: 25.00")
    case '2':
        print(f"lasanha: 20,00")   
    case '3':
        print(f"strogonoff: 18,00")   
    case '4':
        print(f"bife acebolado: 15,00")
    case '5' :
       print("pão com ovo: 5,00")


