import os
os.system("clear")

nu1 = float(input("digite um numero aqui: "))

nu2 = float(input("digite outro número aqui: "))

media = (nu1 + nu2) / 2

soma = (nu1 + nu2)

produto = (nu1 * nu2)

print()

maior_numero = max (nu1,nu2)
menor_numero = min (nu1,nu2)

if nu1 == nu2:
   print("os números são iguais")


print()

print(f"maior: ",maior_numero)

print(f"menor: ",menor_numero)

print(f"media: ",media)

print(f"soma: ",soma)

print(f"produto: ",produto)
