import os 
os.system("clear")



login = str(input("digite o seu login: "))
senha = str(input("digite sua senha: "))

login  = "pedro123"
senha = "123456"

while  login == senha and senha == login:
    print("login e senha corretos")
    login = str(input("digite o seu login: "))
    senha = str(input("digite sua senha: "))

print("acesso permitido!")    