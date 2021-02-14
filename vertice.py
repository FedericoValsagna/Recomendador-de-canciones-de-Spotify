class Vertice:

    def __init__(self, dato, adyacentes):
        self.dato = dato
        if not adyacentes:
            adyacentes = {}
        self.adyacentes = adyacentes