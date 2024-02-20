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

class Auto:
     cantidadCreados = 0

     def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

     def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

     def verificarIntegridad(self):
        registros = set()
        registros.add(self.registro)
        registros.add(self.motor.registro)
        for asiento in self.asientos:
            if asiento is not None:
                registros.add(asiento.registro)
        if len(registros) == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro
    
    def asignarTipo(self, nuevoTipo):
        if nuevoTipo.lower() == "electrico" or nuevoTipo.lower() == "gasolina":
            self.tipo = nuevoTipo
            print("El tipo de motor cambiado exitosamente")
        else:
            print("Tipo de motor no valido. El tipo de motor debe ser electrico o de gasolina.")
    

        