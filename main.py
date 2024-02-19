class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        coloresAsignados = ["Rojo", "Azul", "Verde", "Negro", "Blanco"]
        if nuevoColor.lower() in coloresAsignados:
            if nuevoColor.lower() == self.color.lower():
                print(f"El asiento ya es de color {nuevoColor}. No se realizaron cambios.")
            else:
                print(f"El color del asiento ha sido cambiado de {self.color} a {nuevoColor}.")
                self.color = nuevoColor
        else:
            print(f"El color {nuevoColor} no esta permitido para este asiento.")
            

        