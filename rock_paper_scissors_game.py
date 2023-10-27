from time import sleep
import random

options = ["PIEDRA", "PAPEL", "TIJERA"]
user_score = 0
pc_score = 0

#################### ------------------------------ FUNCIONES ------------------------------ ####################

def countdown(n):
  for numero in range(n, -1, -1):
    if numero == 0:
      print("¡Empecemos!", end="\n\n")
    else:
      print(numero, end=" ")
      sleep(1)

def points(n):
  for punto in range(n+1):
    print(".", end="")
    sleep(0.5)

def pc_choice():
  choice = random.randint(0, 2)
  sleep(2)
  decision = options[choice]
  return decision


#################### ------------------------------ JUEGO ------------------------------ ####################

print("Bienvenido a 'Piedra, Papel & Tijera', un juego de aleatoriedad.")
sleep(3)

countdown(5)

while True:
    print("Piedra \u270A", end="")
    points(3)
    print(" Papel \u270B", end="")
    points(3)
    print(" Tijera! \u270C", end="\n")

    user_answer = input().upper()
    pc_answer = pc_choice()

    sleep(3)

    if user_answer == options[0] and pc_answer == options[0] or user_answer == options[1] and pc_answer == options[1] or user_answer == options[2] and pc_answer == options[2]:
        print("Vaya, un empate. Nadie gana", end="\n\n")
        sleep(1)

    elif user_answer == options[0] and pc_answer == options[2]:
        print("¡Punto para el usuario!", end="\n\n")
        user_score += 1
        sleep(1)

    elif user_answer == options[1] and pc_answer == options[0]:
        print("¡Punto para el usuario!", end="\n\n")
        user_score += 1
        sleep(1)

    elif user_answer == options[2] and pc_answer == options[1]:
        print("¡Punto para el usuario!", end="\n\n")
        user_score += 1
        sleep(1)

    elif user_answer == "SALIR":
        print("Los resultados son:")
        print("Puntuación del usuario:", user_score)
        print("Puntuación del pc:", pc_score)

        sleep(3)
        break
        quit()

    else:
        print("¡Punto para el PC!", end="\n\n")
        pc_score += 1