import os
os.system("clear")


def calcular():
    
     peso = float(input("digite seu peso: "))    
     altura = float (input("digite usa altura: ")) 
     final = peso / (altura * altura)
     return final
    
    
 
media = calcular()



if media < 18.5:
    print("abaixo do peso\nconsulte um nutricionista! ")
elif media < 24.9:
    print("peso normal\n mantenha abitos saudaveis.")
elif media < 29.9:
    print("sobrepeso\n faça caminhada ou atividades fisicas.")
elif media < 34.9:
    print("obesidade G1\n procure uma orientação médica")
elif media < 39.9:
    print("obesidade G2\nconsulte o médico para orientação e avaliação.")
else:
    print("obesidade, procure um tratamento urgente.")    
    
