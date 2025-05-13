import os 
os.system("clear")

pedidos = []
carro = []
preco = []
categoria = []


def menu_carro():
    print("""
codigo   carro    preço

                 
1    porshe 911Gt3      1.100,000  
2    AMG GT 2023        1.250,000        
3    BMW I8             650.000
4    AUDI TT RS         500.000   
5    CIVIC 2023/2024    300.000     
6    CAMARO 2016        250.000
7    JETTA              205.000       

OBS:VERIFIFICAR AS CORES EM ESTOQUE
      

""")
    
nome = input("digite o nome que deseja receber na nota: ")    
    
while True: 
    menu_carro()    
    opcao1 = str(input("digite o codigo do carro: "))    
    
    
    match opcao1:
     case '1':
           carro.append("PORSHE 911GT3") 
           categoria.append("carro de corrida da categoria GT3")
           preco.append  ( 1100000)
     case '2':
           carro.append("AMG GT 2023")
           categoria.append("esportivo")
           preco.append  ( 1250000)   
     case '3':
           carro.append("BMW I8")
           categoria.append("superesportivo")
           preco.append  ( 650000 ) 
     case '4':
           carro.append("AUDI TT RS")
           categoria.append("superesportivo")
           preco.append  ( 500000 ) 
     case '5' :
           carro.append("CIVIC 2023/2024")
           categoria.append("compacto")
           preco.append  ( 300000 ) 
     case '6':
           carro.append("CAMARO 2016")
           categoria.append("esportivo\n")
           preco.append   (250000 )    
     case '7':
           carro.append("JETTA")
           categoria.append("medio(C)\n")
           preco.append  ( 205000 ) 
     case '0' :
           print("espera para digitar a cor do carro!")
           print(f"carro: {carro}")
           print(f"preço: {preco}")
           
           break



print()

def calcular(precos):
    soma = sum(precos)
    return soma

# Calcula o preço total
preco_total = calcular(preco)

# Mostra os resultados
print(f"\nResumo da Compra para {nome}:")
print(f"Quantidade de carros escolhidos: {len(carro)}")
print(f"Carros: {', '.join(carro)}")
print(f"Preço total: R$ {preco_total:,.2f}")


print()
print("_____salvando os dados do cliente_____")
nome_arquivo = "3.0 pedidos da concerssionaria"

# w -> escrita/salvar/sobrescrever
#  escrita/salvar/acumular

with open (nome_arquivo,"a") as arquivo:
      arquivo.write(f"Resumo da Compra de {nome}\ncarros escolhido: {carro}categoria do carro: {categoria}\npreço total: {preco_total:,.2f}\nquantidade de carros: {len(carro)}\n\n\n")
      print()
        
print("Dados salvo com sucesso!\ntenha um bom dia!")       
    