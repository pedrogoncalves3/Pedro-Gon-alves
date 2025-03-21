import os 
os.system("clear")



login = "12345"
senha = "12345"
contador = 0

print(f"vc tem: 3  tentativas")        


for i in range(3):
    login_cadastrado = input("digite o seu login: ")
    senha_cadastrada = input("digite sua senha: ")
   

    if login_cadastrado == login and senha_cadastrada == senha:
        print("acesso permitido")
        break
    else:
        print("acesso negado! tente novamente")
        
        if contador == 2:
            print("NÚMERO DE TENTATIVAS ACIMA DO PERMITIDO")   
            break
       

    

 