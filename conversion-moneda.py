# Paso 1. Definir el valor actual del Euro y Dolar con respecto al Peso Mexicano

tipo_cambio_eur_a_mex= 23.70 # En un caso mas realista habria que consumir informacion actualizada de una BBDD o API
tipo_cambio_usd_a_mex= 20.75 # En un caso mas realista habria que consumir informacion actualizada de una BBDD o API

# Paso 2. Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)

tipo_conversion= input('Ingrese la moneda de origen para la conversion (EUR/USD): ')
tipo_conversion_final=tipo_conversion.upper

# Paso 3. Solicitar al usuario el monto a convertir
monto_a_convertir= float(input('Ingrese el monto a convertir: '))


# Paso 4. Realizar la conversion utilizando el tipo de cambio correspondiente.
# Paso 5. Mostrar el resultado de la conversion al usuario.

if tipo_conversion_final=='EUR':
    resultado= monto_a_convertir * tipo_cambio_eur_a_mex
    print('El resultado de la conversion de EUR a MXN es: ', resultado)
elif tipo_conversion_final =='USD':
    resultado = monto_a_convertir * tipo_cambio_usd_a_mex
    print ('El resultado de la conversion de USD a MXN es: ', resultado)
else:
    print('No esta disponible este tipo de conversion actualmente')