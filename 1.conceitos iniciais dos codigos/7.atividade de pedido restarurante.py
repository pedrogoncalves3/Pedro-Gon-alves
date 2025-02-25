import os

#limpa terminal 

os.system("clear")

print("""
======CARDAPIO======
cdg prato            valor
      
1   | picanha            | 25.00
2   | Lasanha            | 20.00
3   | Strogonoff         | 18,00
4   | Bife Acebolado     | 15,00
5   | Pão com ovo        | 5,00      
      

""")


nome = input("Nome que deseja no seu pedido: ")
cpf = int(input("Digite seu CPF para codigo: "))
opcao = str(input("Digite a opcção desejada: "))

import random
numero_pedido = random.randint(1,100)

print()
print(f"seu codigo de fila é: {numero_pedido}")

match opcao:
    case '1':
        print(f"picanha: D25.00")
    case '2':
        print(f"lasanha: 20,00")   
    case '3':
        print(f"strogonoff: 18,00")   
    case '4':
        print(f"bife acebolado: 15,00")
    case '5' :
       print("pão com ovo: 5,00")
    case '_' :
       print("opção invalida")


