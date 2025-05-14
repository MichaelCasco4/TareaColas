class NodoPaciente:
    def __init__(self, nombre):
        self.nombre = nombre            
        self.siguiente = None           

class ColaClinica:
    def __init__(self):
        self.frente = None              
        self.final = None             

    def insertar_paciente(self, nombre):
        nuevo = NodoPaciente(nombre)   
        if self.final is None:
            # Si la cola está vacía, el nuevo paciente es tanto el primero como el último
            self.frente = self.final = nuevo
        else:
            # Enlazar el nuevo paciente al final de la cola
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"Paciente '{nombre}' agregado a la cola.")

    def atender_paciente(self):
        if self.frente is None:
            print("No hay pacientes para atender.")
            return
        nombre = self.frente.nombre     # Guardar el nombre del paciente atendido
        self.frente = self.frente.siguiente  # Mover el frente al siguiente paciente
        if self.frente is None:
            # Si después de eliminar la cola queda vacía, actualizar el final también
            self.final = None
        print(f"Paciente '{nombre}' ha sido atendido.")

    def mostrar_cola(self):
        if self.frente is None:
            print("No hay pacientes en espera.")
            return
        actual = self.frente
        print("Pacientes en espera:")
        while actual:
            print(f"- {actual.nombre}")  
            actual = actual.siguiente    

