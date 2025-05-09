def calcular_inss(salario_base):
    if salario_base <= 1518.00:
        desconto = salario_base * 0.075
    elif salario_base <= 2793.88:
        desconto = salario_base * 0.09 - 113.85
    elif salario_base <= 4190.83:
        desconto = salario_base * 0.12 - 189.54
    elif salario_base <= 8157.41:
        desconto = salario_base * 0.14 - 318.38
    else:
        desconto = 1142.04  # Teto máximo de contribuição
    return desconto

def calcular_irrf(salario_base, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario_base - deducao_dependentes

    if base_calculo <= 2259.20:
        desconto = 0
    elif base_calculo <= 2826.65:
        desconto = base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        desconto = base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        desconto = base_calculo * 0.225 - 662.77
    else:
        desconto = base_calculo * 0.275 - 896.00
    return max(desconto, 0)

def calcular_vale_transporte(salario_base, opcao):
    if opcao.lower() == 's':
        return salario_base * 0.06
    return 0

def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def calcular_folha_pagamento():
    print("Bem-vindo ao Sistema de Folha de Pagamento")
    
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    # Solicitar informações do funcionário
    salario_base = float(input("Digite o salário base do funcionário (R$): "))
    vale_transporte = input("Deseja receber vale transporte? (s/n): ")
    valor_vale_refeicao = float(input("Digite o valor do vale refeição fornecido pela empresa (R$): "))
    dependentes = int(input("Digite a quantidade de dependentes: "))

    # Cálculos
    desconto_inss = calcular_inss(salario_base)
    desconto_irrf = calcular_irrf(salario_base, dependentes)
    desconto_vale_transporte = calcular_vale_transporte(salario_base, vale_transporte)
    desconto_vale_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
    desconto_plano_saude = calcular_plano_saude(dependentes)

    total_descontos = (desconto_inss + desconto_irrf + desconto_vale_transporte + desconto_vale_refeicao + desconto_plano_saude)
    salario_liquido = salario_base - total_descontos

    
    
    
    print("\nResumo da Folha de Pagamento:")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {desconto_inss:.2f}")
    print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {desconto_vale_transporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {desconto_plano_saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

ValueError
print("codigo invalido digite o codigo novamente!")

calcular_folha_pagamento()