# 14 Utilizar la función input() que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
7
def es_primo(numero):
    if numero < 4:
        return True
    numero_es_primo = True
    divisor_de_prueba = 2
    while (divisor_de_prueba < numero):
        if (numero % divisor_de_prueba == 0):
            numero_es_primo = False
            break
        divisor_de_prueba += 1
    return numero_es_primo

v14a = int(input('Ingrese un numero para saber si es primo, y si no, encontrar el siguiente: '))

if es_primo(v14a):
    print('{} es un numero primo'.format(v14a))
else:
    print('El numero ingresado no es primo')
    v14b = v14a + 1
    while not(es_primo(v14b)):
        v14b += 1
    print('El proximo numero primo es {}'.format(v14b))