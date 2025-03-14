import os
import time
os.system("clear || cls")

nu = int(input("digite o numero q deseja para o timer(sempre coloque 1 a mais): "))
nu2 = float(input("digite quantos segundos vc precisa de um numero para o outro: "))

print("com laço de repetição")
print("contagem regressiva. ")
for i in range(1, nu, ):
    print(f"o valor da variavel i: {i}")
    time.sleep (nu2)  #espera 1 segundo
    
print("acabou. ")    

