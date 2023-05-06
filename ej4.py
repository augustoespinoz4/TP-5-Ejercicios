'''Una empresa factura a sus clientes el último día de cada mes. 
Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, 
tiene un descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura, 
mientras que si paga después del día 20 deberá abonar una multa de $350 o del 10% de su factura, 
lo que resulte mayor. Escribir un programa que lea el número del cliente y el total de la factura, 
y emita un informe donde conste el número del cliente y los tres importes que podría abonar según la fecha de pago.'''

while True:
    try:
        nroCliente = int(input('Ingrese su numero de cliente: '))
        while nroCliente < 1:
            nroCliente = int(input('Ingrese un valor válido: '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

while True:
    try:
        totalFactura = float(input('Ingrese el total de su factura: '))
        while totalFactura < 1:
            totalFactura = float(input('Ingrese un valor válido: '))
    except ValueError:
        print('\n-----------------------\n------VALUE ERROR------\n-----------------------\n')
        continue
    else:
        break

descuento = totalFactura * 0.02
if descuento < 200:
    descuento = 200
descuento = totalFactura - descuento

multa = totalFactura * 0.1
if multa < 350:
    multa = 350
multa = totalFactura + multa

print('\nNúmero de cliente: ', nroCliente, '\nSi paga dentro de los primeros 10 días del mes siguiente: ', descuento,'\nSi paga en los siguientes 10 días del mes: ', totalFactura, '\nSi paga despues del 20: ', multa)