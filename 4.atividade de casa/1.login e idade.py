import os
os.system("clear")


nome = (input("digite seu nome: "))
idade = int(input("digite sua idade:"))
login_cadastrado = str(input("digite seu login aqui: "))
senha_cadastrada = str(input("digite a sua senha aqui: "))
print()

if idade < 18:
    print("menoridade!")
else:
    print("acesso permitido!")    
   

login = "pedro123"
senha = "pedro123"

if login_cadastrado == login and senha_cadastrada == senha:
    print("bem vindo senhor pedro! ")
else:
    print("login ou senha invalidos! ")      

print()
print(f"nome: ", idade)
print(f"idade: ",idade)
print(f"login: ",login)
print(f"senha: ",senha)