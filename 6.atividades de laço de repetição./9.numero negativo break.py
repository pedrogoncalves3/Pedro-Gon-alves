import os 
os.system ("clear")


soma = 0
contador = 0



while True:
     nota = float(input(f"digite a sua nota: "))
     soma += nota
     contador += 1
 
     if nota <0:
        break  

     resposta = input("deseja digitar mais uma nota? \nresponda com s ou n: ")
     if resposta == "n":
        break
        
media = soma / contador       
os.system("clear")         
print (F"QUANTIDADDE DE NOTAS INFORMADA: {contador}")     
print(f"total da media: {media}")  
print(f"valor somado: {soma}")  
    
    