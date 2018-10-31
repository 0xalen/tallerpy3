class Persona:
    'Clase base para todos los empleados'
    _cuentaPersonas = 0

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        Persona._cuentaPersonas += 1

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = nombre

    def mostrarNumPersonas(self):
        print ("Se crearon %d personas" % Persona.cuentaPersonas)
