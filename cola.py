class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        """
        Desencola el elemento que está en el frente de la cola
        y lo devuelve.
        Pre: la cola NO está vacía.
        Pos: el nuevo frente es el que estaba siguiente al frente anterior
        """
        if self.esta_vacia():
            raise ValueError("cola vacía")
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return dato

    def ver_frente(self):
        """
        Devuelve el elemento que está en el frente de la cola.
        Pre: la cola NO está vacía.
        """
        if self.esta_vacia():
            raise ValueError("cola vacía")
        return self.frente.dato

    def esta_vacia(self):
        return self.frente is None
