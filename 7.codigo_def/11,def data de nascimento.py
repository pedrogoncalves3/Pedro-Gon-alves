import os 
from datetime import date
os.system("clear")

def idade_real(ano):
    return date.today().year - ano
    
    

ano = int(input("digite o ano em que voçe nasceu: ")) 

idade = idade_real(ano)

print(f"voçe tem {idade} anos")
   