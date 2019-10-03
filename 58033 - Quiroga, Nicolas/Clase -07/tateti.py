from tablero import draw_tablero, win, full, validate
tablero =[]
for i in range (0,9):
    tablero.append (" ")
draw_tablero(tablero)
while not win(tablero) and not full(tablero):
    print("Turno X")
    valido=False
    while not valido:
        print("ingrese una posicion valida de 1 a 9")
        posicion=int(input())
        valido= validate (tablero,posicion)
        if not valido:
            print ("Error de posicion")
    tablero[posicion-1]="X"
    draw_tablero(tablero)
    gano= win (tablero)
    if gano:
        print ("Gano X")
    else:
        print ("Turno O")
        valido=False
        while not valido:
            print ("ingrese una posicion valida de 1 a 9")
            posicion=int(input())
            valido=validate (tablero,posicion)
            if not valido:
                print ("Error de posicion")
        tablero[posicion-1]="O"
        draw_tablero(tablero)
        gano=win (tablero)
        if gano:
            print ("Gano O")
    if full(tablero) or not win (tablero):
        print ("Empataron giles")




