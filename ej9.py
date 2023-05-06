'''Ingresar un número N y validar que sea positivo. Luego:
a.Mostrar los primeros números impares, hasta alcanzar el número ingresado.
b.Informar la suma de esos números impares. 
Ejemplo:
* Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
* Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
* Si se ingresa -5, se debe pedir otro número.'''

while True:
    try:
        nro = int(input('Ingresar un número entero positivo: '))
        while nro < 0:
            nro = int(input('Número inválido. \nIngresar un número entero positivo: '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

sumaImpares = 0
impar = 1

if nro == 0:
    print('Se ingresó el numero 0. No hay números impares en este rango.')
else:
    while impar <= nro:
        print(impar)
        sumaImpares += impar
        impar += 2

    print('La suma de los impares es:', sumaImpares)