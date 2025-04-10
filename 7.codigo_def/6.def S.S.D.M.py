import os
os.system("clear")

def somar(n1,n2):
     calcular = n1 + n2
     return calcular

def subtrair(n1,n2):
     calcular = n1 - n2
     return calcular 

def divisao(n1,n2):
     calcular = n1 / n2
     return calcular 

def multiplicacao(n1,n2):
     calcular = n1 * n2 
     return calcular  



n1 = int(input("digite o primeiro número para calculo: "))
n2 = int(input("digite o segundo número para calculo: "))


soma = somar(n1,n2)
subtracao = subtrair(n1,n2)

print()
print(f"a soma de {n1} + {n2} e igual a: {soma}")
print(f"a subtração de {n1} - {n2} e igual a: {subtracao}")
print(f"a divisão de {n1} / {n2} e igual a: {divisao}")
print(f"a multiplicação de {n1} x {n2} e igual a: {multiplicacao}")