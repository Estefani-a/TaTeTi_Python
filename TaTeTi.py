def imprimir_tablero(tablero): #imprime el tablero en forma de cuadricula
    print('\n')
    for fila in tablero: 
        for i in range(len(fila)): #recorremos cada elemento de cada fila
            if i == len(fila) - 1: #si es el ultimo elemento de la fila que realize un enter
                print(fila[i], end='\n') #genera el enter
            else:
                print(fila[i], end='  ') #si no que deje dos espacios
    print('\n')

    
def actualizar_tablero(tablero, posicion, jugador): #funcion que cambia el valor del tablero
    if jugador: #determianmos que jugador es 
        simbolo = 'x'
    else:
        simbolo = 'o'
    
    if posicion == 1: #ocupamos el tablero segun la posicion que eliga
        if tablero[4][0] == ' ':
            tablero[4][0] = simbolo
            return 0 #se utiliza para chequear que la funcion anduvo bien
        else:
            return 'Esa posicion ya esta ocupada.' #si llega a estar ocupada imprime este mensaje
    elif posicion == 2:
        if tablero[4][2] == ' ':
            tablero[4][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 3:
        if tablero[4][4] == ' ':
            tablero[4][4] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 4:
        if tablero[2][0] == ' ':
            tablero[2][0] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 5:
        if tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 6:
        if tablero[2][4] == ' ':
            tablero[2][4] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 7:
        if tablero[0][0] == ' ':
            tablero[0][0] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 8:
        if tablero[0][2] == ' ':
            tablero[0][2] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    elif posicion == 9:
        if tablero[0][4] == ' ':
            tablero[0][4] = simbolo
            return 0
        else:
            return 'Esa posicion ya esta ocupada.'
    else:
        return 'Esa posicion no existe.'


def hay_ganador(tablero): #chequea si hay ganador viendo tablero 
    for simbolo in ['x', 'o']: #chequeamos poniendo todas las posibles jugadas ganadoras
        fila_0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo
        fila_2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
        fila_4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
        columna_0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero[4][0] == simbolo
        columna_2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero[4][2] == simbolo
        columna_4 = tablero[0][4] == simbolo and tablero[2][4] == simbolo and tablero[4][4] == simbolo
        diagonal_abajo = tablero[0][0] == simbolo and tablero[2][2] == simbolo and tablero[4][4] == simbolo
        diagonal_arriba = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo

        if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_abajo or diagonal_arriba:
            if simbolo == 'x': #chequeamos quien es el ganador x o
                return 1
            elif simbolo == 'o':
                return 2
            break

            
def leer_archivo():
    # lee el archivo 'Registro_partidas.txt' con los resultados, si el archivo no existe lo crea
    nombre_archivo = 'Registro_partidas.txt'
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        diccionario = {}
        for linea in lineas:
            # construimos un diccionario con los datos del archivo
            # el diccionario contiene el nombre del jugador con las partidas que gano, empato y perdio
            datos = linea.split()
            nombre = datos[0]
            ganadas = int(datos[1].split(':')[1])
            empates = int(datos[2].split(':')[1])
            perdidas = int(datos[3].split(':')[1])
            diccionario[nombre] = {'Victorias':ganadas, 'Empates':empates, 'Derrotas':perdidas}
    except:
        with open(nombre_archivo, 'w') as archivo:
            print('Archivo ' + nombre_archivo + ' creado.')
        diccionario = {}
        
    finally:
        return  diccionario    
                  
def escribir_archivo(diccionario):
    nombre_archivo = 'Registro_partidas.txt'
    with open(nombre_archivo, 'w') as archivo:
        for nombre in diccionario.keys():
            ganadas = diccionario[nombre]['Victorias']
            empates = diccionario[nombre]['Empates']
            perdidas = diccionario[nombre]['Derrotas']
            linea = nombre + ' Victorias:' + str(ganadas) + ' Empates:' + str(empates) + ' Derrotas:' + str(perdidas) + '\n'
            archivo.write(linea)
        

print('Jugaremos al tateti, las posiciones para colocar las fichas son las siguientes')
print()

tablero = [
    ['7', '|', '8', '|', '9'],
    ['-', '+', '-', '+', '-'],
    ['4', '|', '5', '|', '6'],
    ['-', '+', '-', '+', '-'],
    ['1', '|', '2', '|', '3']
]

imprimir_tablero(tablero) 
print('\nQue comience el juego\n')


turno_1 = True #booleano para determinar de quien es el turno de jugar 

diccionario_registro = leer_archivo()

while True:
    
    # nombres de los jugadores
    while True:
        print('Nombre de jugador 1 (x)')
        jugador_1 = input()
        if jugador_1!='':
            break
    
    while True:
        print('Nombre de jugador 2 (o)')
        jugador_2 = input()
        if jugador_2!='':
            break
    
    # buscar si existen los jugadores en el diccionario, y si no crearlos
    for nom in (jugador_1,jugador_2):
        try:
            diccionario_registro[nom]
        except:
            diccionario_registro[nom] = {'Victorias':0, 'Empates':0, 'Derrotas':0}
    
    tablero = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
    ]
    
    turno = 0
    imprimir_tablero(tablero) 
    
    while turno < 9: #revisamos que no se generen mas de 9 turnos ya que terminaria el juego
        
        if turno_1:
            print('\n' + jugador_1 + ', elegi una posicion')
        else:
            print('\n' + jugador_2 + ', elegi una posicion')

        while True:
            try:
                jugada = int(input()) #se realiza una jugada con numero en numpad
                break
            except:
                print('Elegi una posicion (numero entero)')

        valor = actualizar_tablero(tablero, jugada, turno_1) 
        if valor == 0: #le pasamos el turno al otro jugador
            turno_1 = not turno_1
            turno += 1 #sumamos un turno
            imprimir_tablero(tablero) #imprimimos devuelta ya que cambio
            if hay_ganador(tablero) == 1: #chequeamos si gano jugador 1
                print('\n' + jugador_1 + " gano!")
                # sumar uno a las victorias del jugador1, sumar derrotas jugador 2
                diccionario_registro[jugador_1]['Victorias'] += 1
                diccionario_registro[jugador_2]['Derrotas'] += 1
                break
            elif hay_ganador(tablero) == 2: #gano jugador 2
                print('\n' + jugador_2 + " gano!")
                # sumar uno a las victorias del jugador2, sumar derrotas jugador 1
                diccionario_registro[jugador_2]['Victorias'] += 1
                diccionario_registro[jugador_1]['Derrotas'] += 1
                break
        else:
            print(valor)

        if turno == 9: #si se llego a 9 movimientos empate
            print("Empate...")
            # sumar uno a los empates de los dos jugadores
            diccionario_registro[jugador_1]['Empates'] += 1
            diccionario_registro[jugador_2]['Empates'] += 1
            
        
    while True:
        repetir = input('\nQuieren volver a jugar?  SI/NO')
        if repetir.lower()=='si' or repetir.lower()=='no':
            break
    
    if repetir.lower()=='no':
        print('\nGracias por jugar, que tengas un lindo dia.')
        escribir_archivo(diccionario_registro)
        break
        
    