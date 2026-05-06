import random

def jugar():
    print("--- ¡Adivina el Numero! ---")
numero_secreto = random.randint(1, 10)

intento = int(input("Elige un numero entre 1 y 10: "))

if intento == numero_secreto:
    print("¡Felicidades! ¡Ganaste!")
else:
    print(f"Perdiste. El numero era {numero_secreto}.")
    if __name__ == "__main__":
        jugar()