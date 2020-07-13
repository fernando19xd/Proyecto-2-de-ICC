import random

p1 = 'Player 1'
p2 = 'Player 2'


def casilla_libre(tablero, casilla):
    '''Devuelve True si la casilla está vacía y False cuando está llena'''

    return tablero[casilla] == " "


def mostrar_tablero_5(tablero):

  '''Muestra el tablero vacío y con las fichas puestas'''

  print()
  print("                          CINCO EN RAYA")
  print()
  print("       1         |2        |3        |4        |5        ")
  print("            {}    |    {}    |    {}    |    {}    |    {}    ".format(tablero[0], tablero[1], tablero[2], tablero[3], tablero[4]))
  print("                 |         |         |         |         ")
  print("       --------------------------------------------------")
  print("       6         |7        |8        |9        |10       ")
  print("            {}    |    {}    |    {}    |    {}    |    {}    ".format(tablero[5], tablero[6], tablero[7], tablero[8], tablero[9]))
  print("                 |         |         |         |         ")
  print("       --------------------------------------------------")
  print("       11        |12       |13       |14       |15       ")
  print("            {}    |    {}    |    {}    |    {}    |    {}    ".format(tablero[10], tablero[11], tablero[12], tablero[13], tablero[14]))
  print("                 |         |         |         |         ")
  print("       --------------------------------------------------")
  print("       16        |17       |18       |19       |20       ")
  print("            {}    |    {}    |    {}    |    {}    |    {}    ".format(tablero[15], tablero[16], tablero[17], tablero[18], tablero[19]))
  print("                 |         |         |         |         ")
  print("       --------------------------------------------------")
  print("       21        |22       |23       |24       |25       ")
  print("            {}    |    {}    |    {}    |    {}    |    {}    ".format(tablero[20], tablero[21], tablero[22], tablero[23], tablero[24]))
  print("                 |         |         |         |         ")
  print()


def hay_ganador_5(tablero, jugador):
    '''Comprueba si un estado del tablero es ganador: Tiene cinco fichas en raya'''

    if tablero[0] == tablero[1] == tablero[2] == tablero[3] == tablero[4] == jugador or tablero[5] == tablero[6] == \
            tablero[7] == tablero[8] == tablero[9] == jugador or tablero[10] == tablero[11] == tablero[12] == \
            tablero[13] == tablero[14] == jugador or tablero[15] == tablero[16] == tablero[17] == tablero[18] == \
            tablero[19] == jugador or tablero[20] == tablero[21] == tablero[22] == tablero[23] == tablero[24] == \
            jugador or tablero[0] == tablero[5] == tablero[10] == tablero[15] == tablero[20] == jugador or tablero[1] == \
            tablero[6] == tablero[11] == tablero[16] == tablero[21] == jugador or tablero[2] == tablero[7] == \
            tablero[12] == tablero[17] == tablero[22] == jugador or tablero[3] == tablero[8] == tablero[13] == \
            tablero[18] == tablero[23] == jugador or tablero[4] == tablero[9] == tablero[14] == tablero[19] == \
            tablero[24] == jugador or tablero[0] == tablero[6] == tablero[12] == tablero[18] == tablero[24] == \
            jugador or tablero[4] == tablero[8] == tablero[12] == tablero[16] == tablero[20] == jugador:
        return True
    else:
        return False


def movimiento_Player1_5(tablero):
    ''' Devuelve la casilla elegida por Player1'''

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
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


def movimiento_Player2_5(tablero):
    ''' Devuelve la casilla elegida por Player1'''

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
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


def movimientoMaquina_5(tablero, ordenador, usuario):
  for i in range(25):
    copia = list(tablero)
    if casilla_libre(copia, i):
      copia[i] = ordenador
      if hay_ganador_5(copia, ordenador):
        return i

  for i in range(25):
    copia = list(tablero)
    if casilla_libre(copia, i):
      copia[i] = usuario
      if hay_ganador_5(copia, usuario):
        return i

  if ordenador == "X":
    if tablero[12] == " ":
        return 12

    elif tablero[6] == " ":
        return 6

    elif tablero[7] == " ":
        return 7

    elif tablero[8] == " ":
        return 8

    elif tablero[11] == " ":
        return 11

    elif tablero[13] == " ":
        return 13

    elif tablero[16] == " ":
        return 16

    elif tablero[17] == " ":
        return 17

    elif tablero[18] == " ":
        return 18

    else:
      if not tablero[12] == " ":
        vacias12 = []
        for i in [0, 2, 4, 6, 8, 10, 14, 16, 18, 20, 22, 24, 1, 3, 5, 9, 15, 17, 19, 21, 23]:
            if tablero[i] == " ":
                vacias12.append(i)
        return random.choice(vacias12)

      if not tablero[6] == " ":
        vacias6 = []
        for i in [0, 2, 4, 12, 8, 10, 14, 16, 18, 20, 22, 24, 1, 3, 5, 9, 15, 19, 21, 23]:
            if tablero[i] == " ":
                vacias6.append(i)
        return random.choice(vacias6)

      if not tablero[7] == " ":
        vacias7 = []
        for i in [1, 3, 5, 9, 11, 13, 15, 17, 19, 21, 23, 0, 2, 4, 10, 14, 18, 20, 22, 24]:
            if tablero[i] == " ":
                vacias7.append(i)
        return random.choice(vacias7)

      if not tablero[8] == " ":
        vacias8 = []
        for i in [0, 2, 4, 6, 12, 10, 14, 16, 18, 20, 22, 24, 1, 3, 5, 9, 15, 17, 19, 21, 23]:
            if tablero[i] == " ":
                vacias8.append(i)
        return random.choice(vacias8)

      if not tablero[11] == " ":
        vacias11 = []
        for i in [1, 3, 5, 9, 7, 13, 15, 17, 19, 21, 23, 0, 2, 4, 10, 14, 18, 20, 22, 24]:
            if tablero[i] == " ":
                vacias11.append(i)
        return random.choice(vacias11)

      if not tablero[16] == " ":
        vacias16 = []
        for i in [0, 2, 4, 6, 8, 10, 14, 12, 18, 20, 22, 24, 1, 3, 5, 9, 15, 17, 19, 21, 23]:
            if tablero[i] == " ":
                vacias16.append(i)
        return random.choice(vacias16)

      if not tablero[13] == " ":
        vacias13 = []
        for i in [1, 3, 5, 9, 11, 7, 15, 17, 19, 21, 23, 0, 2, 4, 10, 14, 18, 20, 22, 24]:
            if tablero[i] == " ":
                vacias13.append(i)
        return random.choice(vacias13)

      if not tablero[18] == " ":
        vacias18 = []
        for i in [0, 2, 4, 6, 8, 10, 14, 16, 12, 20, 22, 24, 1, 3, 5, 9, 15, 17, 19, 21, 23]:
            if tablero[i] == " ":
                vacias18.append(i)
        return random.choice(vacias18)

        if not tablero[17] == " ":
            vacias17 = []
            for i in [1, 3, 5, 9, 11, 13, 15, 7, 19, 21, 23, 0, 2, 4, 10, 14, 18, 20, 22, 24]:
                if tablero[i] == " ":
                    vacias17.append(i)
            return random.choice(vacias17)

  elif ordenador == "O":
    contador = 0
    for i in range(25):
      if tablero[i] == " ":
        contador += 1
    if contador == 23:
      if tablero[12] == " ":
        return 12
      elif tablero[6] == " ":
        return 6
      elif tablero[7] == " ":
        return 7
      elif tablero[8] == " ":
        return 8
      elif tablero[11] == " ":
        return 11
      elif tablero[13] == " ":
        return 13
      elif tablero[16] == " ":
        return 16
      elif tablero[17] == " ":
        return 17
      elif tablero[18] == " ":
        return 18