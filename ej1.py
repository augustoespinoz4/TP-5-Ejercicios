'''Leer números que representan edades de un grupo de personas, 
finalizando la lectura cuando se ingrese el número -1. Imprimir 
cuántos son menores de 18 años, cuántos tienen 18 años o más y el 
promedio de edad de ambos grupos. Descartar valores que no representan una 
edad válida. (Se considera válida una edad entre 0 y 100).'''

cantMen18 = 0
cantMay18 = 0
sumaMen18 = 0
sumaMay18 = 0
band = 0

while True:
    try:
        edad = int(input('Ingrese edad (o -1 para finalizar): '))
        while (edad < 0 or edad > 100) and edad != -1:
            edad = int(input('Fuera del rango. \n\nIngrese nuevamente: '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

while edad != -1:
    if edad >= 18:
        sumaMay18 += edad
        cantMay18 += 1
    elif edad < 18:
        sumaMen18 += edad
        cantMen18 += 1

    while True:
        try:
            edad = int(input('Ingrese una nueva edad: '))
            while (edad < 0 or edad > 100) and edad != -1:
                edad = int(input('Fuera del rango. \n\nIngrese nuevamente: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break
    band = 1

if band == 1:
    if cantMay18 > 0:
        promedioMay18 = sumaMay18 / cantMay18
        print('\nCantidad de mayores: ', cantMay18, ' \nPromedio de mayores: ', promedioMay18,)
    else:
        print('No se ingresaron mayores de 18.')

    if cantMen18 > 0:
        promedioMen18 = sumaMen18 / cantMen18
        print('\nCantidad de menores: ', cantMen18, '\nPromedio de menores: ', promedioMen18)
    else:
        print('No se ingresaron menores de 18.')
else:
    print('No se ingresaron datos.')

