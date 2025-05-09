import os
os.system("clear")

login = "pedro"
senha = "123456"
QUANTIDADE_NOTAS = 3
soma = 0
contador = 0

print("voçe tem apenas 3 tentativas")

for i in range(3):   
 
    login_cadastrado = input("digite o seu login : ")
    senha_cadastrada = input("digite a sua senha: ")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("acesso permitido")
        break
    else:
        print(f"senha ou login incorrerto. \ntente novamente!")
        contador += 1
        if contador == 2:
            print("NÚMERO DE TENTATIVAS ACIMA DO PERMITIDO")   
            break



for i in range(QUANTIDADE_NOTAS):        
    while True:
       nota = float(input(f"digite a {i+1}ªnota: ")) 
       if nota <0 or nota >10:
            print("nota invalida, tente novamente.\n")
       else:
            soma += nota
            break

    media = soma / (QUANTIDADE_NOTAS)
    
    if media >= 7:
          resultado = "aprovado"
    elif media >=5:
         resultado = "recuperação"
    else:
         resultado = "reprovado"   
   

print(f"media: {media}")
print(f"resultado: {resultado}")

   

