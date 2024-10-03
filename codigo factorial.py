# Función para calcular el factorial de un número
def factorial(n):
    if n < 0:  # Verificamos si el número es negativo
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:  # El factorial de 0 y 1 es 1
        return 1
    else:
        resultado = 1  # Inicializamos el resultado en 1
        for i in range(2, n + 1):  # Recorremos desde 2 hasta n
            resultado *= i  # Multiplicamos el resultado por i en cada iteración
        return resultado  # Devolvemos el factorial calculado

# Ejemplo de uso
numero = 6  # Definimos el número para calcular su factorial
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")