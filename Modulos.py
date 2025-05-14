from collections import deque


#Clase que representa a un paciente que pide turno en la farmacia
class Paciente:
    def __init__(self, nombre, servicio):
        self.nombre = nombre
        self.servicio = servicio
#Retorna una representacion legible del paciente
    def __str__(self):
        return f"{self.nombre} - {self.servicio}"
    
class Cola_Turnos:

#Implemento una cola para generar los turnos en un orden FIFO
    def __init__(self):
        self.cola = deque()

    def agregar_turno(self, paciente):
#Agrega al paciente al final de la cola
        self.cola.append(paciente)

        print(f"Turno registrado, {paciente}. \n")

    def atender_turno(self):
#Atiende al paciente que esta de primero en la cola
        if not self.esta_vacia():
            paciente = self.cola.popleft()   #Extrae al primer paciente de la cola (FIFO: el que llegó primero)'popleft()' elimina y retorna el primer elemento de la deque
            print(f"El cliete {paciente} esta siendo atendido.. \n")
            return paciente
        else:
#Validacion de cola vacia
            print("En este momento no hay pacientes en espera. \n")
            return None
    
    def mostrar_pendientes(self):
#Muestra todos los pacientes en espera
        if not self.esta_vacia():
            print("Turnos pendientes: ")
            #Recorre la cola enumerando cada paciente desde el número 1
            for i, paciente in enumerate(self.cola, start=1):
                # Muestra el número de turno junto con la información del paciente
                print(f"{i}. {paciente} ")
                print()

        else:
            print("No hay turnos pendientes \n")
            return None
        
    def esta_vacia(self):
        return len(self.cola) == 0


        