import os 
os.system("clear")


print("""
======CARDAPIO======
codigo \tprato  \tpreço

1    picanha            25.00
2    Lasanha            20.00
3    Strogonoff         18,00
4    Bife Acebolado     15,00
5    Pão com ovo        5,00      


""")

gorjeta_garçom = 0
preco_total = 0






while True:

    nome = input("nome que deseja no seu pedido: ")
    opcao1 = int(input("digite a opcção desejada: "))
    
    



    match opcao1:
       case '1':
        prato == "picanha"
        preco == 25
       case '2':
        prato == "lasanha"
        preco == 20  
       case '3':
        prato == "strogonoff"
        preco == 18  
       case '4':
        prato == "befe acebolado"
        preco == 15
       case '5' :
        prato == "pao com ovo"
        preco == 5
       case '_':
        print("opção invalida")
    preco = 0

    preco_total += preco   
    pergunta = (input("deseja fazer outro pedido?: "))

    if pergunta=="n":
      break

if preco_total >0:
      gorjeta = input("deseja pagar 10% do valor da sua nota como gorjeta para o garçom?")

if gorjeta == "s":
       gorjeta_garçom = preco_total *0.10

total_pagar = preco_total + gorjeta_garçom

print(f"valor da gorjte: {gorjeta_garçom}")
print(f"valor total da compra: {total_pagar}")


