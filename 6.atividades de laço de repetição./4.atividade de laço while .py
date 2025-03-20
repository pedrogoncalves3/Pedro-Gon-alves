import os 
os.system("clear")




while True:
      nu1 = int(input("digite uma nota: "))

      if nu1 < 0 or nu1 > 10:
        print("acesso negado nota invalida")
      else:
         break    
      
      
print(f"nota informada: {nu1}")   

     