class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo

    def ver_tope(self):
        """
        Devuelve el elemento que está en el tope de la pila.
        Pre: la pila NO está vacía.
        """
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def desapilar(self):
        """
        Desapila el elemento que está en el tope de la pila
        y lo devuelve.
        Pre: la pila NO está vacía.
        Pos: el nuevo tope es el que estaba abajo del tope anterior
        """
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def esta_vacia(self):
        return self.tope is None

