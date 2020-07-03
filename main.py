from Tres_en_raya import mostrar_tablero_3, hay_ganador_3, movimiento_Player1_3, movimiento_Player2_3
from Cuatro_en_raya import mostrar_tablero_4, hay_ganador_4, movimiento_Player1_4, movimiento_Player2_4


print()
print()
print("              BIENVENIDOS AL ARCADE")
print()
print()
print()
print("                  Tres en Raya")
print()
print("                 Cuatro en Raya")
print()
print()
print("   ¿Qué quieren jugar? *Coloque 3 o 4*")
print()


while True:
  tipo_juego = input("Tipo de juego: ")
  if tipo_juego == "3" or tipo_juego == "4":
      break
  else:
    print("Ingrese un juego que este dentro del arcade")


Player1 = input("Ingrese nombre jugador 1: ")
Player2 = input("Ingrese nombre jugador 2: ")
p1 = Player1
p2 = Player2


juego = ""
def presentacion_1():
  if tipo_juego == "3":
    juego = "Tres en raya"
  elif tipo_juego == "4":
    juego = "Cuatro en raya"
    
  ''' Devuelve la ficha elegida por Player1 y Player2'''

  print()
  print("            ", juego)
  print()
  print()
  print("Comienza la ficha O")
  print()
  print(" Elige O/X")
  print()
  print()
  
  ficha = ""
  while ficha != "O" and ficha != "X":
    ficha = input("    -->  ").upper()
    
  if ficha == "O":
    Player1 = "O"
    Player2 = "X"
  
  else:
    Player1 = "X"
    Player2 = "O"
  
  return Player1, Player2


def seguir_jugando():
  if tipo_juego == "3":
    juego = "Tres en raya"
  elif tipo_juego == "4":
    juego = "Cuatro en raya"
    
  '''Devuelve True si el usuario quiere jugar otra partida, sino devuelve False'''

  print()
  print("             ¿Quieren jugar otra partida de" , juego, "?" )
  respuesta = input("             Respuesta: ")
  respuesta = respuesta.lower()
  if respuesta == "si" or respuesta == "sí":
    return True
  else:
    print()

    print(            "Si quiere jugar Cuatro en raya, reinice el juego :D")
    return False


def tablero_lleno(tablero):
  
  ''' Devuelve True si una casilla esta vacia y False si esta llena'''
  
  for i in tablero:
    if i == " ":
      return False
  else:
    return True


if tipo_juego == "3":
  jugando_3 = True

  while jugando_3:
    tablero = [" "] * 9
  
    Player1, Player2 = presentacion_1()
  
    mostrar_tablero_3(tablero)

    if Player1 == "O":
      turno = "Player 1"
    else:
      turno = "Player 2"

    partida_3 = True
  
    while partida_3:
      if tablero_lleno(tablero):
        print("           Empate")
        break
    
      elif turno == "Player 1":
        casilla = movimiento_Player1_3(tablero)
        tablero[casilla] = Player1
        turno = "Player 2"
        mostrar_tablero_3(tablero)
        if hay_ganador_3(tablero, Player1):
          print("          Has ganado", p1)
          partida = False
          break

      elif turno == "Player 2":
        casilla = movimiento_Player2_3(tablero)
        tablero[casilla] = Player2
        turno = "Player 1"
        mostrar_tablero_3(tablero)
        if hay_ganador_3(tablero, Player2):
          print("          Has ganado", p2)
          partida = False
          break
    jugando_3 = seguir_jugando()

if tipo_juego == "4":
  jugando_4 = True
  while jugando_4:
    tablero = [" "] * 16
  
    Player1, Player2 = presentacion_1()
  
    mostrar_tablero_4(tablero)
  

    if Player1 == "O":
      turno = "Player 1"
    else:
      turno = "Player 2"

    partida_4 = True
  
    while partida_4:
      if tablero_lleno(tablero):
        print("           Empate")
        break
    
      elif turno == "Player 1":
        casilla = movimiento_Player1_4(tablero)
        tablero[casilla] = Player1
        turno = "Player 2"
        mostrar_tablero_4(tablero)
        if hay_ganador_4(tablero, Player1):
          print("          Has ganado", p1)
          partida = False
          break

      elif turno == "Player 2":
        casilla = movimiento_Player2_4(tablero)
        tablero[casilla] = Player2
        turno = "Player 1"
        mostrar_tablero_4(tablero)
        if hay_ganador_4(tablero, Player2):
          print("          Has ganado", p2)
          partida = False
          break
    jugando_4 = seguir_jugando()