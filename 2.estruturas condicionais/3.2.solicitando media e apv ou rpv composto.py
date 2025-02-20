import os
os.system("clear")

nome = input("digite seu nome aqui: ")
nota1 = float(input("digite a nota da primeira unidade: "))
nota2 = float(input("digite a nota da segunda unidade: "))
nota3 = float(input("digite a nota da terceira unidade: "))

media = (nota1 + nota2 + nota3) /3

print()
if media < 7:
    print ("reprovado")
    print (f"Resultado: ", media )
else:
    print  ("Aprovado") 
    print (f"Resultado: ", media )

    
    




