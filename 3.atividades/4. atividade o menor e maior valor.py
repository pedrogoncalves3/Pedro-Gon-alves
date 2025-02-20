import os
os.system("clear")

nu1 = float(input("digite um numero aqui: "))

nu2 = float(input("digite outro número aqui: "))


media = (nu1 + nu2) / 2
soma = (nu1 + nu2)
produto = (nu1 * nu2)
print()


if nu1 > nu2:
   print(f"{nu2} e menor que {nu1}")

if nu1 == nu2:
   print("os números são iguais")

else:
   print(f"{nu1} e menor que {nu2}")



print()
print(f"media: ",media)

print(f"soma: ",soma)

print(f"produto: ",produto)
