import os 
os.system("clear")




while True:
      nota1 = int(input("digite a primeira nota: "))
      nota2 = int(input("digite a segunda nota: "))

      media = (nota1 + nota2) /2
      
      if nota1 < 0 or nota1 > 10:
        print("acesso negado nota invalida")
        break
      elif nota2 < 0 or nota2 > 10:
        print("acesso negado nota invalida")  
      else:
         break    
      
      
print(f"media total {media}")

     