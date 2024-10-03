# Definición de un nodo de la lista
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # El valor que contiene el nodo
        self.siguiente = None  # Puntero al siguiente nodo (inicialmente None)

# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista comienza vacía (sin nodos)

    # Método para insertar un valor al final de la lista
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)  # Crear un nuevo nodo con el valor dado
        if self.cabeza is None:  # Si la lista está vacía
            self.cabeza = nuevo_nodo  # El nuevo nodo será la cabeza de la lista
        else:
            actual = self.cabeza
            while actual.siguiente:  # Avanzar hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Conectar el nuevo nodo al final de la lista

    # Método para mostrar todos los elementos de la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:  # Recorremos la lista hasta que no haya más nodos
            print(actual.dato, end=" -> ")  # Imprimimos el valor del nodo
            actual = actual.siguiente
        print("None")  # Al final de la lista se imprime 'None'

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)

print("Elementos de la lista:")
lista.mostrar()