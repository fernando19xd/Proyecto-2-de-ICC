import random

p1 = 'Player 1'
p2 = 'Player 2'


def casilla_libre(tablero, casilla):
    '''Devuelve True si la casilla está vacía y False cuando está llena'''

    return tablero[casilla] == " "


def mostrar_tablero_4(tablero):

  '''Muestra el tablero vacío y con las fichas puestas'''

  print()
  print("                    CUATRO EN RAYA")
  print()
  print("       1         |2        |3        |4        ")
  print("            {}    |    {}    |    {}    |    {}".format(tablero[0], tablero[1], tablero[2],tablero[3]))
  print("                 |         |         |         ")
  print("       ----------------------------------------")
  print("       5         |6        |7        |8        ")
  print("            {}    |    {}    |    {}    |    {}".format(tablero[4], tablero[5], tablero[6],tablero[7]))
  print("                 |         |         |         ")
  print("       ----------------------------------------")
  print("       9         |10       |11       |12        ")
  print("            {}    |    {}    |    {}    |    {}".format(tablero[8], tablero[9], tablero[10],tablero[11]))
  print("                 |         |         |         ")
  print("       ----------------------------------------")
  print("       13        |14       |15       |16       ")
  print("            {}    |    {}    |    {}    |    {}".format(tablero[12], tablero[13], tablero[14],tablero[15]))
  print("                 |         |         |         ")
  print()


def hay_ganador_4(tablero, jugador):
    '''Comprueba si un estado del tablero es ganador: Tiene cuatro fichas en raya'''

    if tablero[0] == tablero[1] == tablero[2] == tablero[3] == jugador or tablero[4] == tablero[5] == tablero[6] == \
            tablero[7] == jugador or tablero[8] == tablero[9] == tablero[10] == tablero[11] == jugador or tablero[12] == \
            tablero[13] == tablero[14] == tablero[15] == jugador or tablero[0] == tablero[4] == tablero[8] == tablero[
        12] == jugador or tablero[1] == tablero[5] == tablero[9] == tablero[13] == jugador or tablero[2] == tablero[
        6] == tablero[10] == tablero[14] == jugador or tablero[3] == tablero[7] == tablero[11] == tablero[
        15] == jugador or tablero[0] == tablero[5] == tablero[10] == tablero[15] == jugador or tablero[3] == tablero[
        6] == tablero[9] == tablero[12] == jugador:
        return True
    else:
        return False


def movimiento_Player1_4(tablero):
    ''' Devuelve la casilla elegida por Player1'''

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("    Es el turno de " + str(p1) + " (1-16): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("    Esta posición esta ocupada")
            else:
                return posicion - 1


def movimiento_Player2_4(tablero):
    ''' Devuelve la casilla elegida por Player1'''

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("    Es el turno de " + str(p2) + " (1-16): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("    Esta posición esta ocupada")
            else:
                return posicion - 1


def movimientoMaquina_4(tablero, ordenador, usuario):
  for i in range(16):
    copia = list(tablero)
    if casilla_libre(copia, i):
      copia[i] = ordenador
      if hay_ganador_4(copia, ordenador):
        return i

  for i in range(16):
    copia = list(tablero)
    if casilla_libre(copia, i):
      copia[i] = usuario
      if hay_ganador_4(copia, usuario):
        return i

  if ordenador == "X":
    if tablero[5] == " ":
        return 5

    elif tablero[6] == " ":
        return 6

    elif tablero[9] == " ":
        return 9

    elif tablero[10] == " ":
        return 10

    else:
      if not tablero[5] == " ":
        vacias5 = []
        for i in [0, 2, 8, 10, 3, 7, 11, 12, 13, 14, 15]:
            if tablero[i] == " ":
                vacias5.append(i)
        return random.choice(vacias5)

      if not tablero[6] == " ":
        vacias6 = []
        for i in [1, 3, 9, 11, 0, 4, 8, 12, 13, 14, 15]:
            if tablero[i] == " ":
                vacias6.append(i)
        return random.choice(vacias6)

      if not tablero[9] == " ":
        vacias9 = []
        for i in [4, 6, 12, 14, 0, 1, 2, 3, 7, 11, 15]:
            if tablero[i] == " ":
                vacias9.append(i)
        return random.choice(vacias9)

      if not tablero[10] == " ":
        vacias10 = []
        for i in [5, 7, 13, 15, 0, 1, 2, 3, 4, 8, 12]:
            if tablero[i] == " ":
                vacias10.append(i)
        return random.choice(vacias10)

  elif ordenador == "O":
    contador = 0
    for i in range(16):
      if tablero[i] == " ":
        contador += 1
    if contador == 14:
      if tablero[5] == " ":
        return 5
      elif tablero[6] == " ":
        return 6
      elif tablero[9] == " ":
        return 9
      elif tablero[10] == " ":
        return 10