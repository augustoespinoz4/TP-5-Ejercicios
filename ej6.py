'''Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene. 
Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa 12345 se debe imprimir 5.'''

while True:
    try:
        nro = int(input('Ingresar un numero entero: '))
    except ValueError:
        print('\nIngresar sólo valores enteros.')
        continue
    else:
        break

if nro < 0:
    nro = nro * (-1)

digitos = 0

while nro != 0:
    digitos += 1
    nro = nro // 10

print('El número tiene', digitos, 'dígitos.')