class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def recorrer_inorden(self, nodo):
        if nodo is not None:
            self.recorrer_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.recorrer_inorden(nodo.derecha)

    def recorrer_preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self.recorrer_preorden(nodo.izquierda)
            self.recorrer_preorden(nodo.derecha)

    def recorrer_postorden(self, nodo):
        if nodo is not None:
            self.recorrer_postorden(nodo.izquierda)
            self.recorrer_postorden(nodo.derecha)
            print(nodo.valor, end=" ")

# Ejemplo de uso
arbol = ArbolBinario()
valores = [5, 3, 7, 2, 4, 6, 8]

for valor in valores:
    arbol.insertar(valor)

print("Recorrido inorden:")
arbol.recorrer_inorden(arbol.raiz)

print("\nRecorrido preorden:")
arbol.recorrer_preorden(arbol.raiz)

print("\nRecorrido postorden:")
arbol.recorrer_postorden(arbol.raiz)
