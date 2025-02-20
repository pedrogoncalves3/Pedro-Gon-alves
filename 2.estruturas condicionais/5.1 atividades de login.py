import os
os.system("clear")



#solicitando dados para o usuario
login_cadastrado = str(input("digite seu login aqui: "))
senha_cadastrada = str(input("digite a sua senha aqui: "))
print()


#cadastrando login e senha
login = "pedro123"
senha = "pedro123"

#verificando os dados cadastrados
if login_cadastrado == login and senha_cadastrada == senha:
    print("bem vindo senhor pedro! ")
else:
    print("login ou senha invalidos")      

print()
print(f"login: ",login)
print(f"senha: ",senha)
