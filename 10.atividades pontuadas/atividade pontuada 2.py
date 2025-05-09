import os
from time import sleep

os.system("clear || cls")
# Variáveis para armazenar dados
m = 0
f = 0
qtd_salariof = 0
qtd_pessoas = 0
media_salario = 0
idades = []  # Lista para armazenar idades

while True:
    print("""
Código | Descrição
1      | Adicionar pessoa
2      | Exibir resultados
3      | Sair
    """)
    
    opcao = int(input("Selecione a opção: "))
    
    match opcao:
        case 1:
            idade = int(input("Digite sua idade: "))
            sexo = int(input("Selecione seu sexo: Masculino (1) ou Feminino (outro número): "))
            salario = float(input("Digite seu salário: "))
            
            # Adicionando idade à lista
            idades.append(idade)
            media_salario += salario
            qtd_pessoas += 1
            
            # Adicionando ao numero de mulheres que recebem mais que 5000,00
            if sexo != 1 and salario >= 5000:
                qtd_salariof += 1
            os.system("clear || cls")
                
        case 2:
            # Calculando e exibindo os resultados
            if qtd_pessoas > 0:
                media = media_salario / qtd_pessoas
                maior_idade = max(idades)
                menor_idade = min(idades)
                print(f"A média de salário do grupo é: R${media:.2f}")
                print(f"A maior idade é: {maior_idade} anos")
                print(f"A menor idade é: {menor_idade} anos")
                print(f"Mulheres que recebem mais de 5.000,00: {qtd_salariof}")
            else:
                print("Nenhuma pessoa cadastrada ainda.")
        
        case 3:
            os.system("clear || cls")
            print("Fechando o programa.")
            sleep(1)
            exit()

        case _:
            print("Opção invalida!")
            sleep(1)


