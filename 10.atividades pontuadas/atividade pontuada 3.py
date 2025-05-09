import os
from time import sleep
os.system("clear || cls")


usuario = "pedro"
senha_dls = "12345"

def painel_esperando():
 print("""
            
 Aguarde um pouco!
 estamos verificando sua matrícula!   
               
""")  


while True:
    matricula = input("digite a sua matricula: ")
    senha = input("digite a sua senha: ")
    if matricula == usuario and senha == senha_dls:
     print("acesso permitido!")
     break
    else:
     print("acesso negado")
     
        
os.system("clear")


painel_esperando()
sleep(5)
os.system("clear")


salario = float(input("digite seu salario bruto: "))
  

def calcular_inss(salario_base):
    if salario <= 1518.00:
        desconto = salario_base * 0.075
    elif salario <= 2793.88:
        desconto = salario_base * 0.09 - 113.85
    elif salario <= 4190.83:
        desconto = salario_base * 0.12 - 189.54
    elif salario <= 8157.41:
        desconto = salario_base * 0.14 - 318.38
    else:
        desconto = 1142.04  
    return desconto

def calcular_irrf(salario,dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario - deducao_dependentes

    if base_calculo <= 2259.20:
        desconto = 0
    elif base_calculo <= 2793.88:
        desconto = base_calculo * 0.075 - 169.44
    elif base_calculo <= 4190.83:
        desconto = base_calculo * 0.15 - 381.44
    elif base_calculo <= 8157.41:
        desconto = base_calculo * 0.225 - 662.77
    else:
        desconto = base_calculo * 0.275 - 896.00    
    return max(desconto,0)

while True:
 vale_trasnporte = str(input(f"Digite (S) para sim e (N)para Não \ndeseja receber vale tranporte?: "))        
 def calcular_vale_transporte(salario, opcao):
    if opcao.lower() == 's':
        return salario * 0.06
    return 0
 break


while True:
 vale_alimentacao = float(input(f"Digite o valor do vale refeição fornecido pela empresa "))    
 def calcular_vale_refeicao(vale_alimentacao):
    return vale_alimentacao * 0.20
 break

while True:
 dependentes = int(input("digite a quantidade de dependentes: "))    
 def calcular_plano_saude(dependentes):
    return dependentes * 150.00
 break



desconto_inss = calcular_inss(salario)
desconto_irrf = calcular_irrf(salario, dependentes)
desconto_vale_transporte = calcular_vale_transporte(salario, vale_trasnporte)
desconto_vale_refeicao = calcular_vale_refeicao(vale_alimentacao)
desconto_plano_saude = calcular_plano_saude(dependentes)

total_descontos = (desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_saude)
salario_liquido = salario - total_descontos

os.system("clear")
print("aguarde estamos verificando o resulatado!")
sleep (5)


print("\nResumo da Folha de Pagamento:")
print(f"Salário Base: R$ {salario:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
print(f"Desconto Vale Transporte: R$ {desconto_vale_transporte:.2f}")
print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
print(f"Desconto Plano de Saúde: R$ {desconto_plano_saude:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")








