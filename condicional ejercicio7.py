class vehiculo:
    def __init__(self,marca,nombre,modelo,problema) -> None:
        self.marca=marca
        self.marca=nombre
        self.modelo=modelo
        self.problema=problema
        pass

class Auto(vehiculo):
    def __init__(self, marca, nombre, modelo, problema) -> None:
        super().__init__(marca, nombre, modelo, problema)
    pass

class camioneta(vehiculo):
    def __init__(self, marca, nombre, modelo, problema) -> None:
        super().__init__(marca, nombre, modelo, problema)
        pass