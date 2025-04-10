import os 
os.system("cls||clear")




def contador_pares_e_impares ():
    pares = 0
    impares = 0


    for i in range(6):
        n1 = int(input(f"digite um número:  "))
        
        if n1 % 2 == 0:
         pares += 1  
        else:
         impares += 1 
    return pares,impares    


quantidade_pares,quantidade_impares = contador_pares_e_impares()

print(f"voçe digitou {quantidade_pares} numeros pares")
print(f"voçe digitou {quantidade_impares} numeros impares")


    

 





