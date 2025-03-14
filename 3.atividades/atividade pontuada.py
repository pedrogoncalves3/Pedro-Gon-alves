import os 
os.system("clear || cls")

produto = float(input("digite o valor do produto: "))

os.system("clear || cls")

print("""

FORMA DE PAGAMENTO!
      
1- A VISTA
2- A PRAZO      


""")

pagamento = int(input("digite a forma de pagamento: "))

os.system("clear || cls")
match pagamento:
    case 1:
        desconto = produto * 0.10
        total_com_desconto = produto - desconto

        print(f"valor do produto: {produto}")
        print(f"forma de pagamento: {pagamento}")
        print(f"valor do desconto: {desconto}")
        print(f"total a pagar: {total_com_desconto}")

    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
            valor_da_parcela = produto / quantidade_parcelas 

        print(f"\nValor do produto: R$ {produto}")
        print(f"Forma de pagamento: à prazo")
        print(f"Quantidade de parcelas: {quantidade_parcelas}")
        print(f"Valor por parcela: R$ {valor_da_parcela:.2f}")
        print(f"Total à prazo: R$ {produto}")
       