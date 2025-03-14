import os
os.system("clear")

produto = float(input("digite o valor do produto: "))

print("""

1 - pagamento avista
2 - parcela em ate 6x       

""")

forma_pagamento = int(input("digite a forma de pagamento: "))



match forma_pagamento:
    case 1:
        debito = "debito"
        print("pagamento avista") 
    case 2:
        credito = "credito"  
        parcelas = int(input("digite quantas parcelas: "))
        parcelado = produto /  parcelas

    case _ :
        print("opção invalida")
print()     

if forma_pagamento == 1:
    valor_debito = produto * 0.1
    valor_final = produto - valor_debito
    print(f"valor do produto: {produto}")
    print(f"FORMA DE PAGAMENTO: {debito}")    
    print(f"VALOR DO DESCONTO: 10%")
    print(f"total a pagar {valor_final}")




if forma_pagamento == 2:
    print(f"valor do produto: {produto}")
    print(f"FORMA DE PAGAMENTO: {credito}")  
    print(f"valor por parcelas: {parcelado}")  
    print(f"total a prazo {produto}")    

