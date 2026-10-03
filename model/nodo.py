class Nodo:
    def __init__(self, nombre, es_carpeta):
        self.nombre = nombre
        self.es_carpeta = es_carpeta
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        tipo = "Carpeta" if self.es_carpeta else "Archivo"
        return f"[{tipo}] {self.nombre}"