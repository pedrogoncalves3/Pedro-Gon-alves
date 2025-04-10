import os


def logo_senai():
    os.system("clear")
    print("===SENAI===")

logo_senai()
nome = input("digite seu nome:")

logo_senai()
idade = input("digite sua idade:")

logo_senai()
print(f"\nNome: {nome}")
print(f"\nidade: {idade}")