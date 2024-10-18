"""Ejercicio 1: Gestión de empleados en una empresa
Enunciado: Crea un sistema de gestión de empleados en una empresa. 
Implementa dos clases: Empleado (que almacena nombre y salario) y 
Gerente (que hereda de Empleado y tiene un atributo adicional para su departamento). Usa setters y getters para todos los atributos. Crea un menú que permita:

Registrar empleados.
Registrar gerentes.
Mostrar todos los empleados.
Mostrar los gerentes con sus departamentos.
Clases involucradas:
Empleado: nombre, salario.
Gerente: hereda de Empleado y añade departamento.
"""
# Clase base
class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    # retornamos un mensaje 
    def __str__(self):
        return f"Nombre del empleado {self.__nombre}, con un salario de: {self.__salario}"
    
    # set y getter
    @property
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario = salario
# Clase heredera con empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.__departamento = departamento
        
        
    def __str__(self):
        return f"Nombre del empleado {self.__nombre}, con un salario de: {self.__salario} y en el departamento de {self.departamento}"
    
    @property
    def getDepartamento(self):
        return self.__departamento
    def setDepartamento(self, departamento):
        self.__departamento = departamento
        
class SistemaGestionEmpresa:
    # creamos las variables como una lista
    def __init__(self):
        self.empleados = []
        self.gerentes = []
        
        # Agregamos empleados
    def agregar_Empleado(self, empleado): 
        self.empleados.append(empleado)   
        # Para registrar al empleado
    def registrar_Empleado (self):
        nombre = input("Ingrese el nombre del empleado")
        salario = input("Ingrese el salario del empleado")
        empleado = Empleado(nombre, salario)
        
        self.agregar_Empleado(empleado)
        print("Empleado registrado correctamente")
    
        # Agregamos gerentees
    def agregar_Gerente(self, gerente):
        self.gerentes.append(gerente)
        # Para registrar al gerente
    def registrar_Gerente(self):
        nombre = input("Ingrese el nombre del gerente")
        salario = int(input("Ingrese el salario del gerente"))
        departamento = int(input("Ingrese el departamento del gerente"))
        gerente = Gerente(nombre, salario, departamento)
        
        self.agregar_Gerente(gerente)
        print("Gerente registrado correctamente")
        
        # Mostramos al empleado y al gerente
    def mostrar_Empleados(self):
        for empleado in self.empleados:
            print(empleado)
    
    def mostrar_gerentes(self):
        for gerente in self.gerentes:
            print(gerente)
    # Menu de interaccion 
    def menu(self):
        while True:
            opcion = int(input("""Ingrese la opcion que deseas realizar
                            1. Registrar empleados
                            2. Registrar gerentes
                            3. Mostrar todos los empleados
                            4. Mostrar los gerentes cpn sus departamentos
                            5. Salir """))
            if opcion == 1:
                self.registrar_Empleado()
            elif opcion == 2:
                self.registrar_Gerente()
            elif opcion == 3:
                self.mostrar_Empleados()
            elif opcion == 4:
                self.mostrar_gerentes()
            else:
                print("Saliendo de la gestion de la empresa")
                break
                
SystemGestion = SistemaGestionEmpresa()
SystemGestion.menu()
        