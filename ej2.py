'''Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. 
El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen 
considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. 
Terminada la carga de datos, informar:
* Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
* Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
* Porcentaje de alumnos que están aplazados (tienen 1 en el examen). '''

cantAprobados = 0
cantDesaprobados = 0
cantAplazados = 0
band = 0

while True:
    try:
        legajo = int(input('Ingrese número de legajo (o -1 para finalizar): '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

while legajo != -1:
    while True:
        try:
            nota = int(input('\nIngrese la nota del examen final: '))
            while nota < 1 or nota > 10:
                nota = int(input('Fuera del rango. \nIngrese nuevamente: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break

    if nota >= 4:
        cantAprobados += 1
        print('Aprobado.\n')
    elif nota < 4:
        if nota == 1:
            cantDesaprobados += 1
            cantAplazados += 1
            print('Aplazado')
        else:
            cantDesaprobados += 1
            print('Desaprobado')

    while True:
        try:
            legajo = int(input('\nIngrese otro número de legajo: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break

    band = 1

if band == 1:
    if cantAprobados > 0:
        print('\nLa cantidad de aprobados son: ', cantAprobados, '.')
    else:
        print('\nNo se ingresaron aprobados.')

    if cantDesaprobados > 0:
        print('\nLa cantidad de desaprobados son: ', cantDesaprobados, '.')
    else:
        print('\nNo se ingresaron desaprobados.')

    if cantAplazados > 0:
        print('\nLa cantidad de aplazados son: ', cantAplazados, '.')
    else:
        print('\nNo se ingresaron aplazados.')
else:
    print('\nNo se ingresaron datos.')

