import os
import time
os.system("clear")

print("""
      
Códigos  |  Descrição

   1     |   Adicionar pessoas

   2     |   exibir resultados    

   3     |  sair

""")
qtd_salario = 0
qtd_pessoas = 0
nome = 0
idades = []
media_salario = 0



while True:
   
   opcao = int(input("digite a opção desejada: "))
   match opcao:
      case 1:

         nome = input(f"digite o seu nome: ")
         idade = int(input("digite a sua idade: "))
         sexo = int(input(f"digite seu sexo:\n 1 para (MASCULINO)\n 2 para (FEMININO)\n: "))
         salario = float(input("digite o seu salário: "))
         print(f"Pessoa adicionada com sucesso!\naguarde 2 segundos")
         time.sleep (2)

         # adicionar idade a lista
         idades.append(idade)
         media_salario += salario
         qtd_pessoas += 1

         if sexo == 2 and salario > 4999:
            qtd_salario += 1

         os.system("clear || cls")
  
      case 2:
         
         if qtd_pessoas > 0:
           media = media_salario / qtd_pessoas
           maior_idade = max(idades) 
           menor_idade = min(idades)
           
         print(f"seu nome é: {nome}")
         print(f"maior idade: {maior_idade}")
         print(f"menor idade: {menor_idade}")
         print(f"media: {media}")
         print(f"quantidade de mulheres que ganham 5k: {qtd_salario}")
          
        
      case 3:
            os.system("clear || cls")
            print("Fechando o programa.")
            time.sleep(1)
            exit()

      case _:
            print("Opção invalida!")
            time.sleep(1)





       
