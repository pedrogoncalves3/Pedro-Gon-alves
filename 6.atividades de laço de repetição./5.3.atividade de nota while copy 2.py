import os 
os.system("clear")



soma = 0

for i in range (2):
    while True:
        nota = float(input(f"digite a {i+1}ª nota: "))


        if nota <0 or nota >10:
            print("nota invalida, tente novamente.\n")
        else:
            soma += nota
            break

media = soma / 2

print(f"media: {media}")