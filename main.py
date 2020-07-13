from Tres_en_raya import mostrar_tablero_3, hay_ganador_3, movimiento_Player1_3, movimiento_Player2_3, movimientoMaquina_3
from Cuatro_en_raya import mostrar_tablero_4, hay_ganador_4, movimiento_Player1_4, movimiento_Player2_4, movimientoMaquina_4
from Cinco_en_raya import mostrar_tablero_5, hay_ganador_5, movimiento_Player1_5, movimiento_Player2_5, movimientoMaquina_5


print()
print()
print("              BIENVENIDOS AL ARCADE")
print()
print("                  Tres en Raya")
print()
print("                 Cuatro en Raya")
print()
print("                  Cinco en Raya")
print()
print()
print("   ¿Qué quieren jugar? *Coloque 3, 4 o 5*")
print()


while True:
  tipo_juego = input("Tipo de juego: ")
  if tipo_juego == "3" or tipo_juego == "4" or tipo_juego == "5":
      break
  else:
    print("Ingrese un juego que este dentro del arcade")



def presentacion_0():
  modo = ""
  while modo != "solo" and modo != "multiplayer":
    modo = input("Ingrese la modalidad de juego: ").lower()
    if modo != "solo" and modo != "multiplayer":
      print("Ingrese solo o multiplayer")
      modo = input("Ingrese la modalidad de juego: ").lower()
    return modo


def presentacion_1():
  if tipo_juego == "3":
    juego = "Tres en raya"
  elif tipo_juego == "4":
    juego = "Cuatro en raya"
  elif tipo_juego == "5":
    juego = "Cinco en raya"
    
  ''' Devuelve la ficha elegida por Player1 y Player2'''

  print()
  print("            ", juego)
  print()
  print()
  print(" Sale la ficha O")
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
  elif ficha == "X":
    Player1 = "X"
    Player2 = "O"
  return Player1, Player2


def seguir_jugando():
  if tipo_juego == "3":
    juego = "Tres en raya"
    otro = "Cuatro en raya o  Cinco en raya"
  elif tipo_juego == "4":
    juego = "Cuatro en raya"
    otro = "Tres en raya o Cinco en raya"
  elif tipo_juego == "5":
    juego = "Cinco en raya"
    otro = "Tres en raya o Cuatro en raya"

    '''Devuelve True si el usuario quiere jugar otra partida, sino devuelve False'''

  print()
  print("             ¿Quieren jugar otra partida de", juego, "?")
  respuesta = input("             Respuesta: ")
  respuesta = respuesta.lower()
  if respuesta == "si" or respuesta == "sí":
    print()
    if tipo_juego == "3":
      if hay_ganador_3(tablero, Player1):
        archivo = open("archivos/puntaje_3.txt", "a+")
        archivo.write(str(puntaje_1) + "\n")
        archivo.close()
      elif hay_ganador_3(tablero, Player2):
        archivo = open("archivos/puntaje_3.txt", "a+")
        archivo.write(str(puntaje_2) + "\n")
        archivo.close()
    elif tipo_juego == "4":
      if hay_ganador_4(tablero, Player1):
        archivo = open("archivos/puntaje_4.txt", "a+")
        archivo.write(str(puntaje_1) + "\n")
        archivo.close()
      elif hay_ganador_4(tablero, Player2):
        archivo = open("archivos/puntaje_4.txt", "a+")
        archivo.write(str(puntaje_2) + "\n")
        archivo.close()
    elif tipo_juego == "5":
      if hay_ganador_5(tablero, Player1):
        archivo = open("archivos/puntaje_5.txt", "a+")
        archivo.write(str(puntaje_1) + "\n")
        archivo.close()
      elif hay_ganador_5(tablero, Player2):
        archivo = open("archivos/puntaje_5.txt", "a+")
        archivo.write(str(puntaje_2) + "\n")
        archivo.close()
    return True
  else:
    print()
    print("            Si quieren jugar", otro, ", reinice el juego :D")
    print()
    if tipo_juego == "3":
      if hay_ganador_3(tablero, Player1):
        archivo = open("archivos/puntaje_3.txt", "r")
        puntaje_total_3 = []
        for i in archivo:
          puntaje_total_3.append(i)
        archivo.close()
        print("Puntaje de", p1, ": ", len(puntaje_total_3)+1)
      elif hay_ganador_3(tablero, Player2):
        archivo = open("archivos/puntaje_3.txt", "r")
        puntaje_total_3 = []
        for i in archivo:
          puntaje_total_3.append(i)
        archivo.close()
        print("Puntaje de", p2, ": ", len(puntaje_total_3)+1)

    elif tipo_juego == "4":
      if hay_ganador_4(tablero, Player1):
        archivo = open("archivos/puntaje_4.txt", "r")
        puntaje_total_4 = []
        for i in archivo:
          puntaje_total_4.append(i)
        archivo.close()
        print("Puntaje de", p1, ": ", len(puntaje_total_4)+1)
      elif hay_ganador_4(tablero, Player2):
        archivo = open("archivos/puntaje_4.txt", "r")
        puntaje_total_4 = []
        for i in archivo:
          puntaje_total_4.append(i)
        archivo.close()
        print("Puntaje de", p2, ": ", len(puntaje_total_4)+1)

    elif tipo_juego == "5":
      if hay_ganador_5(tablero, Player1):
        archivo = open("archivos/puntaje_5.txt", "r")
        puntaje_total_5 = []
        for i in archivo:
          puntaje_total_5.append(i)
        archivo.close()
        print("Puntaje de", p1, ": ", len(puntaje_total_5)+1)
      elif hay_ganador_5(tablero, Player2):
        archivo = open("archivos/puntaje_5.txt", "r")
        puntaje_total_5 = []
        for i in archivo:
          puntaje_total_5.append(i)
        archivo.close()
        print("Puntaje de", p2, ": ", len(puntaje_total_5)+1)
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
        modo = presentacion_0()
        if modo == "solo":
            Player1 = input("Ingrese nombre jugador 1: ")
            Player2 = "IA"
            p1 = Player1
            p2 = Player2
        elif modo == "multiplayer":
            Player1 = input("Ingrese nombre jugador 1: ")
            Player2 = input("Ingrese nombre jugador 2: ")
            p1 = Player1
            p2 = Player2
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
                puntaje_1 = 0
                if hay_ganador_3(tablero, Player1):
                    puntaje_1 += 1
                    print("          Ha ganado", p1)
                    print()
                    partida = False
                    break

            elif turno == "Player 2":
                if modo == "multiplayer":
                    casilla = movimiento_Player2_3(tablero)
                elif modo == "solo":
                    casilla = movimientoMaquina_3(tablero, Player2, Player1)
                tablero[casilla] = Player2
                turno = "Player 1"
                mostrar_tablero_3(tablero)
                puntaje_2 = 0
                if hay_ganador_3(tablero, Player2):
                    puntaje_2 += 1
                    print("          Ha ganado", p2)
                    print()
                    partida = False
                    break
        jugando_3 = seguir_jugando()

if tipo_juego == "4":
    jugando_4 = True
    while jugando_4:
        tablero = [" "] * 16
        modo = presentacion_0()
        if modo == "solo":
            Player1 = input("Ingrese nombre jugador 1: ")
            Player2 = "IA"
            p1 = Player1
            p2 = Player2
        elif modo == "multiplayer":
            Player1 = input("Ingrese nombre jugador 1: ")
            Player2 = input("Ingrese nombre jugador 2: ")
            p1 = Player1
            p2 = Player2
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
                puntaje_1 = 0
                if hay_ganador_4(tablero, Player1):
                    puntaje_1 += 1
                    print("          Ha ganado", p1)
                    print()
                    partida = False
                    break

            elif turno == "Player 2":
                if modo == "multiplayer":
                    casilla = movimiento_Player2_4(tablero)
                elif modo == "solo":
                    casilla = movimientoMaquina_4(tablero, Player2, Player1)
                tablero[casilla] = Player2
                turno = "Player 1"
                mostrar_tablero_4(tablero)
                puntaje_2 = 0
                if hay_ganador_4(tablero, Player2):
                    puntaje_2 += 1
                    print("          Ha ganado", p2)
                    print()
                    partida = False
                    break
        jugando_4 = seguir_jugando()

if tipo_juego == "5":
    jugando_5 = True
    while jugando_5:
        tablero = [" "] * 25
        modo = presentacion_0()
        if modo == "solo":
            Player1 = input("Ingrese nombre jugador 1: ")
            Player2 = "IA"
            p1 = Player1
            p2 = Player2
        elif modo == "multiplayer":
            Player1 = input("Ingrese nombre jugador 1: ")
            Player2 = input("Ingrese nombre jugador 2: ")
            p1 = Player1
            p2 = Player2
        Player1, Player2 = presentacion_1()
        mostrar_tablero_5(tablero)
        if Player1 == "O":
            turno = "Player 1"
        else:
            turno = "Player 2"

        partida_5 = True
        while partida_5:
            if tablero_lleno(tablero):
                print("           Empate")
                break

            elif turno == "Player 1":
                casilla = movimiento_Player1_5(tablero)
                tablero[casilla] = Player1
                turno = "Player 2"
                mostrar_tablero_5(tablero)
                puntaje_1 = 0
                if hay_ganador_5(tablero, Player1):
                    puntaje_1 += 1
                    print("          Ha ganado", p1)
                    print()
                    partida = False
                    break

            elif turno == "Player 2":
                if modo == "multiplayer":
                    casilla = movimiento_Player2_5(tablero)
                elif modo == "solo":
                    casilla = movimientoMaquina_5(tablero, Player2, Player1)
                tablero[casilla] = Player2
                turno = "Player 1"
                mostrar_tablero_5(tablero)
                puntaje_2 = 0
                if hay_ganador_5(tablero, Player2):
                    puntaje_2 += 1
                    print("          Ha ganado", p2)
                    print()
                    partida = False
                    break
        jugando_5 = seguir_jugando()