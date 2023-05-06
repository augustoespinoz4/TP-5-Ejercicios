'''Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
* Aplica el precio base a la primera docena de unidades.
* Aplica un 10% de descuento a todas las unidades entre 13 y 100.
* Aplica un 25% de descuento a todas las unidades por encima de las 100.

Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
El cálculo resultante sería: 100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04

Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta 
y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar: 
* Cantidad de ventas realizadas total.
* Cantidad de ventas en las que se aplicó un 10% de descuento.
* Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.'''

ventasTotales = 0
ventas10Desc = 0
ventasSinDesc = 0

while True:
    try:
        cantSolicitada = int(input('Ingresar la cantidad solicitada (o -1 para finalizar): '))
        while cantSolicitada < 1 and cantSolicitada != -1:
            cantSolicitada = int(input('Ingrese una cantidad válida: '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

while cantSolicitada != -1:
    precioBase = float(input('Ingresar su precio base: '))

    if cantSolicitada > 100:
        precioFinal = precioBase * 12 + (precioBase - (precioBase * 0.1)) * 88 + (precioBase - (precioBase * 0.25)) * (cantSolicitada - 100)
        ventasTotales += 1  
    elif cantSolicitada > 12 and cantSolicitada <= 100:
        precioFinal = precioBase * 12 + (precioBase - (precioBase * 0.1)) * (cantSolicitada - 12)
        ventasTotales += 1
        ventas10Desc += 1   
    else:
        precioFinal = precioBase * cantSolicitada
        ventasTotales += 1
        ventasSinDesc += 1
    promedio = precioFinal / cantSolicitada

    print('El precio final será de: ', precioFinal, ' y el promedio será: ', promedio)
    
    while True:
        try:
            cantSolicitada = int(input('\nIngresar la cantidad solicitada (o -1 para finalizar): '))
            while cantSolicitada < 1 and cantSolicitada != -1:
                cantSolicitada = int(input('Ingrese una cantidad válida: '))
        except ValueError:
            print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
            continue
        else:
            break

if ventasTotales > 0:
    print('\nCantidad de ventas totales: ', ventasTotales)
    if ventas10Desc > 0:
        print('Cantidad de ventas con 10% de descuento: ', ventas10Desc)
    else:
        print('No se ingresaron ventas con 10% de descuento.')

    if ventasSinDesc > 0:
        print('Cantidad de ventas sin descuento: ', ventasSinDesc)
    else:
        print('No se ingresaron ventas sin descuento.')
else:
    print('No se ingresaron datos.')