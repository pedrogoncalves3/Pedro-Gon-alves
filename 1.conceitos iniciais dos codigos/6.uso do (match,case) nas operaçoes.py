import os

#limpa terminal 

os.system("clear")


nome = input("digite seu nome aqui: ")
numero1 = float(input("digite o primeiro número: "))
operacao = input("digite a operação desejada: ")
numero2 = float(input("digite a nota da segunda unidade: "))



match operacao:
    case '+':
        print(f"valor somado: {numero1 + numero2}")
    case '-':
        print(f"resultado: {numero1 - numero2}")   
    case '*':
        print(f"resultado: {numero1 * numero2}")   
    case '/':
        print(f"resultado: {numero1 / numero2}")   


print()    
print(f"primeiro número: {numero1}")
print(f"segundo número: {numero2}")
print(f"operação: {operacao}")




