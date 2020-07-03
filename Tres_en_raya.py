p1 = 'Player 1'
p2 = 'Player 2'


def casilla_libre(tablero, casilla):
    '''Devuelve True si la casilla está vacía y False cuando está llena'''

    return tablero[casilla] == " "


def mostrar_tablero_3(tablero):

  '''Muestra el tablero vacío y con las fichas puestas'''

  print()
  print("             Tres en raya")
  print()
  print("       1         |2        |3        ")
  print("            {}    |    {}    |    {}".format(tablero[0], tablero[1], tablero[2]))
  print("                 |         |         ")
  print("       ------------------------------")
  print("       4         |5        |6        ")
  print("            {}    |    {}    |    {}".format(tablero[3], tablero[4], tablero[5]))
  print("                 |         |         ")
  print("       ------------------------------")
  print("       7         |8        |9        ")
  print("            {}    |    {}    |    {}".format(tablero[6], tablero[7], tablero[8]))
  print("                 |         |         ")
  print()


def hay_ganador_3(tablero, jugador):
    '''Comprueba si un estado del tablero es ganador: Tiene tres fichas en raya'''

    if tablero[0] == tablero[1] == tablero[2] == jugador or tablero[3] == tablero[4] == tablero[5] == jugador or \
            tablero[6] == tablero[7] == tablero[8] == jugador or tablero[0] == tablero[3] == tablero[6] == jugador or \
            tablero[1] == tablero[4] == tablero[7] == jugador or tablero[2] == tablero[5] == tablero[8] == jugador or \
            tablero[0] == tablero[4] == tablero[8] == jugador or tablero[2] == tablero[4] == tablero[6] == jugador:
        return True
    else:
        return False


def movimiento_Player1_3(tablero):
    ''' Devuelve la casilla elegida por Player1'''

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("    Es el turno de " + str(p1) + " (1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("    Esta posición esta ocupada")
            else:
                return posicion - 1


def movimiento_Player2_3(tablero):
    ''' Devuelve la casilla elegida por Player2'''

    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion = None
    while True:
        if posicion not in posiciones:
            posicion = input("     Es el turno de " + str(p2) + " (1-9): ")
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion - 1):
                print("    Esta posición esta ocupada")
            else:
                return posicion - 1