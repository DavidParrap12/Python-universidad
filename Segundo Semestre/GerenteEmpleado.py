class Empleado:
    def __init__(self, nombre, salario, puesto):
        self.__nombre = nombre
        self.__salario = salario
        self.__puesto = puesto
    
    @property
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def getSalario(self):
        return self.__salario
    def setNombre(self, salario):
        self.__salario = salario
    
    @property
    def getPuesto(self):
        return self.__puesto
    def setNombre(self, puesto):
        self.__puesto = puesto
    
    def descripcion(self):
        return f"{self.__nombre} {self.__salario} {self.__puesto}"
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, puesto, departamento):
        super().__init__(nombre, salario, puesto)
        self.__departamento = departamento
    
    @property
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def getDepartamento(self):
        return self.__departamento
    def setDepartamento (self, departamento):
        self.__departamento = departamento
    
    def descripcion(self):
        return f"{super().descripcion()} en el departamento {self.__departamento}"

mi_empleado = Gerente("David", 10000000, "Desarrollador", "Nueva York")
print(mi_empleado.descripcion())