import os 
os.system("clear")

pares = 0
qtd_impares = 0
soma_pares = 0
soma_total = 0
total_numeros = 0


while True:
 numero = int(input("digite os números: "))
 if numero == 0:
    break
 if not numero:
        print("Nenhum número foi lido.")
        
 total_numeros += 1
 soma_total += numero

 if numero % 2 == 0:
            pares += 1
            soma_pares += numero
 else:
            qtd_impares += 1

 if total_numeros == 0:
        print("Nenhum número foi lido.")


media = soma_total / total_numeros
media_pares = soma_pares / pares
                     
  
os.system("clear")

print(f"-----resultados-----")
print(f"a quantidade de números pares:  {pares}")
print(f"a quantidade de números impares:  {qtd_impares}")
print(f"media de valores pares: {media_pares}")
print(f"media geral dos números lidos: {media}")
