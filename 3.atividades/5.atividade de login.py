import os
os.system("clear")


login = str(input("digite seu login aqui: "))
senha = str(input("digite a sua senha aqui: "))

if login == "pedro.programas":
      print("bem vindo pedro!")
else:
      print("login incorreto")
    

if senha == "pedro123":
      print("senha correta!")
else:
      print("senha incorreta")
      print("tente novamente!")   

print()
print(f"login: ",login)
print(f"senha: ",senha)
