import os
os.system("clear")

def somar(n1,n2, n3):
     calcular = n1 + n2 + n3
     return calcular
  



n1 = int(input("digite o primeiro número para calculo: "))
n2 = int(input("digite o segundo número para calculo: "))
n3 = int(input("digite o terceiro número para calculo: "))



calculo = (n1 + n2 + n3)
media = somar(n1,n2,n3)/3

print(f"o calculo dos números e: {calculo} e a media é {media}")
print(f"sua média foi: {media}")


    

