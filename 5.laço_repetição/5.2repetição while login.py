import os 
os.system("clear")



login = "12345"
senha = "12345"


while  True:
    login_cadastrado = input("digite o seu login: ")
    senha_cadastrada = input("digite sua senha: ")
    

    if login_cadastrado == login and senha_cadastrada == senha:
        print("acesso permitido")
        break
    else:
        print("acesso negado! tente novamente")  
         

    
     
    

 