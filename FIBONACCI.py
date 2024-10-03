# Función para generar la secuencia de Fibonacci hasta el n-ésimo término
def fibonacci(n):
    # Verificamos si el número es negativo
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1:
        return [0]  # Si el número es 1, devolvemos solo el primer término
    elif n == 2:
        return [0, 1]  # Si el número es 2, devolvemos los dos primeros términos
    else:
        secuencia = [0, 1]  # Inicializamos la secuencia con los dos primeros términos
        for i in range(2, n):  # Calculamos el resto de los términos hasta n
            siguiente = secuencia[i - 1] + secuencia[i - 2]  # Suma de los dos números anteriores
            secuencia.append(siguiente)  # Añadimos el nuevo término a la lista
        return secuencia  # Devolvemos la lista con la secuencia de Fibonacci

# Ejemplo de uso
n = 10  # Definimos cuántos términos queremos calcular
resultado = fibonacci(n)
print(f"Los primeros {n} términos de la secuencia de Fibonacci son: {resultado}")