import os 
os.system ("clear")

QUANTIDADE_NOTAS = 3
soma = 0


for i in range(QUANTIDADE_NOTAS):
    while True:
     nota = float(input(f"digite a sua {i+1}ª: "))

     if nota <0 or nota > 10:
        print("nota invalida")
     else:
        soma += nota
        break

media = soma / QUANTIDADE_NOTAS  

if media >= 7:
   resultado = "aprovado"
elif media >=5:
   resultado = "recuperação"
else:
   resultado = "reprovado"   

print(f"media: {media}")
print(f"resultado: {resultado}")