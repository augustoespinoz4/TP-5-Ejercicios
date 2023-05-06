'''Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3). Por cada empleado se lee su legajo, 
categoría y salario. Se solicita elaborar un informe que contenga:
* Importe total de salarios pagados por la empresa.
* Cantidad de empleados que ganan más de $200000.
* Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
* Legajo del empleado que más gana.
* Sueldo más bajo.
* Importe total de sueldos por cada categoría.
* Salario promedio'''

impTotal = 0
cantEmp200 = 0
cantEmp50 = 0
totalSueldos1 = 0
totalSueldos2 = 0
totalSueldos3 = 0
band = 0

while True:
    try:
        cantEmp = int(input('Ingresar la cantidad de empleados: '))
        while cantEmp < 1:
            cantEmp = int(input('Ingresar un número válido: '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

for i in range(0, cantEmp, 1):
    while True:
        try:
            legajo = int(input('\nIngresar el número de legajo: '))
            while legajo < 1:
                legajo = int(input('Ingresar un legajo válido: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break
    
    while True:
        try:
            categoria = int(input('Ingresar la categoría (entre 1 y 3): '))
            while categoria != 1 and categoria != 2 and categoria != 3:
                categoria = int(input('Fuera del rango. \nIntente nuevamente: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break
    
    while True:
        try:
            salario = float(input('Ingresar el salario: '))
            while salario < 1:
                salario = float(input('Ingresar un salario válido: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break
    
    impTotal += salario

    if band == 0:
        sueldoMax = salario
        legajoMax = legajo
        sueldoMin = salario
        if salario >= 200000:
            cantEmp200 += 1

        if categoria == 1:
            totalSueldos1 += salario
        elif categoria == 2:
            totalSueldos2 += salario
        elif categoria == 3:
            totalSueldos3 += salario
            if salario <= 50000:
                cantEmp50 += 1

        print(impTotal, legajoMax, sueldoMin)

    if band == 1:
        if salario > sueldoMax:
            sueldoMax = salario
            legajoMax = legajo
        elif salario < sueldoMin:
            sueldoMin = salario
        if salario >= 200000:
            cantEmp200 += 1

        if categoria == 1:
            totalSueldos1 += salario
        elif categoria == 2:
            totalSueldos2 += salario
        elif categoria == 3:
            totalSueldos3 += salario
            if salario <= 50000:
                cantEmp50 += 1

        print(impTotal, legajoMax, sueldoMin)
    
    band = 1

promSueldos = impTotal / cantEmp

print('\n* Importe total de salarios pagados: ', impTotal)

if cantEmp200 > 0:
    print('* Cantidad de empleados que ganan mas de 200000: ', cantEmp200)
else:
    print('* No se ingresaron empleados que cobren mas de 200000')
if cantEmp50 > 0:
    print('* Cantidad de empleados que ganan menos de 50000: ', cantEmp50)
else:
    print('* No se ingresaron empleados que cobren menos de 50000')

print('* Legajo del empleado que más gana: ', legajoMax)
print('* Sueldo del empleado que menos gana: ', sueldoMin)

if totalSueldos1 > 0:
    print('* El total de sueldos de la categoría uno es: ', totalSueldos1)
else:
    print('* No se ingresaron empleados de categoría uno.')
if totalSueldos2 > 0:
    print('* El total de sueldos de la categoría dos es: ', totalSueldos2)
else:
    print('* No se ingresaron empleados de categoría dos.')
if totalSueldos3 > 0:
    print('* El total de sueldos de la categoría tres es: ', totalSueldos3)
else:
    print('* No se ingresaron empleados de categoría tres.')

print('* El salario promedio es: ', promSueldos)