'''Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el número invertido. 
Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321.'''

while True:
    try:
        nro = int(input('Ingresar un número entero: '))
    except ValueError:
        print('\nIngresar un valor entero.')
        continue
    else:
        break

if nro < 0:
    nro = nro * (-1)

inverso = 0

while nro != 0:
    resto = nro % 10
    inverso = inverso * 10 + resto
    nro = nro // 10

print(inverso)