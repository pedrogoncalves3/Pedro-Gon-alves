import os
import time
os.system("clear || cls")


# Calcule os descontos e acréscimos na folha de pagamento do funcionário.
# Mostre o salário líquido do funcionário após os descontos e acréscimos.

usuario = "pedro"
senha_dls = 12345


# while True:
#    matricula = input("digite a sua matricula: ")
#   senha = float(input("digite a sua senha: "))
#  if matricula == usuario and senha == senha_dls:
#    print("acesso permitido!")
#    break
#   else:
#    print("acesso negado")    

os.system("clear")

salario = float(input("digite seu salario bruto: "))
vale_trasnporte = str(input(f"Digite (S) para sim e (N)para Não \ndeseja receber vale tranporte?: "))
vale_alimentacao = str(input(f"Digite o valor do vale refeição fornecido pela empresa "))
dependentes = int(input("digite a quantidade de dependentes: "))



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
        desconto = 1142.04  # Teto máximo de contribuição
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

def calcular_vale_transporte(calculo_trasporte):
  if vale_trasnporte == "s":
     return calculo_trasporte * 0.06
  return 0

def calcular_vale_refeicao(valor_var):
    return valor_var * 0.20


def calcular_plano_saude(dependentes):
    return dependentes * 150.00



desconto_inss = calcular_inss(salario)
desconto_irrf = calcular_irrf(salario, dependentes)
desconto_vale_transporte = calcular_vale_transporte(salario, vale_trasnporte)
desconto_vale_refeicao = calcular_vale_refeicao(vale_alimentacao)
desconto_plano_saude = calcular_plano_saude(dependentes)

total_descontos = (desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_saude)
salario_liquido = salario - total_descontos






