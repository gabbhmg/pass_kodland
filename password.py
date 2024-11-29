import random 

caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lung_password = int(input("inserisci la lunghezza della password:"))
password = ""
for i in range(lung_password):
    password += random.choice(caratteri)

print("La tua password è:", password)
