
#Clase que representa a un paciente que pide turno en la farmacia
class Paciente:
    def __init__(self, nombre, servicio):
        self.nombre = nombre
        self.servicio = servicio
#Retorna una representacion legible del paciente
    def __str__(self):
        return f"{self.nombre} - {self.servicio}"
    

class NodoPaciente:
    def __init__(self, Paciente):
        self.paciente = Paciente
        self.siguiente = None
    
class Cola_Turnos:

#Implemento una cola para generar los turnos en un orden FIFO
    def __init__(self):
        self.frente = None              
        self.final = None    

    def agregar_turno(self, paciente):
#Agrega al paciente al final de la cola
        nuevo = NodoPaciente(paciente)
        if self.final is None:
            # Si la cola está vacía, el nuevo paciente es tanto el primero como el último
            self.frente = self.final = nuevo
        else:
            # Enlazar el nuevo paciente al final de la cola
            self.final.siguiente = nuevo
            self.final = nuevo
        print(f"Paciente '{nuevo.paciente.nombre}' agregado a la cola.")

    def atender_turno(self):
#Atiende al paciente que esta de primero en la cola
        if self.frente is None:
            print("No hay pacientes para atender.")
            return
        nombre = self.frente.paciente.nombre    # Guardar el nombre del paciente atendido
        self.frente = self.frente.siguiente  # Mover el frente al siguiente paciente
        if self.frente is None:
            # Si después de eliminar la cola queda vacía, actualizar el final también
            self.final = None
        print(f"Paciente '{nombre}' ha sido atendido.")
    
    def mostrar_pendientes(self):
#Muestra todos los pacientes en espera
        if self.esta_vacia():
            temporal = self.frente

            while temporal:
                print("Nombre:" + temporal.paciente.nombre + " " +"Servicio:" + temporal.paciente.servicio)
                temporal = temporal.siguiente

        else:
            print("No hay turnos pendientes \n")
            return None
        
    def esta_vacia(self):
        if self.frente is None:
            print("La cola esta vacia!")
            return False
        else:
            return True


        