class vehiculo:
    def __init__(self,marca,nombre,modelo,cilindrada,problema) -> None:
        self.marca=marca
        self.marca=nombre
        int.modelo=modelo
        float.cilindrada=cilindrada
        self.problema=problema
        pass

class Auto(vehiculo):
    def __init__(self, marca, nombre, modelo,cilindrada, problema) -> None:
        super().__init__(marca, nombre, modelo,cilindrada, problema)
    pass

class camioneta(vehiculo):
    def __init__(self, marca, nombre, modelo,cilindrada, problema) -> None:
        super().__init__(marca, nombre, modelo,cilindrada, problema)
        pass

auto_uno=Auto("chevrolet","corsa",2004,1.4,"correa de distribucion cortada y arbol de levas posiblemente doblado ")
