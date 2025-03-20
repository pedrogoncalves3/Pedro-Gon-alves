import os 
os.system("clear")




while True:
      nota1 = int(input("digite a primeira nota: "))


      
      if nota1 < 0 or nota1 > 10:
        print("acesso negado nota invalida")
      else:
          break
      
      
while True:
      nota2 = int(input("digite a segunda nota: "))

      if nota2 < 0 or nota2 > 10:
         print("acesso negado nota invalida")  
      else:
         break    
      

media = (nota1 + nota2)/2   

print(f"media total {media}")

     