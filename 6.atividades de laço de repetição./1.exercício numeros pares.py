import os
import time
os.system("clear")

print("de 100 A 120 em números pares")

for i in range(100, 121, 2):
    print(f"números pares: {i}")
    time.sleep(0.2)

print("acabou. ")