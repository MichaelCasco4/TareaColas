from Modulos import Paciente, Cola_Turnos

#Creacion del menu, para la vista al usuario

def mostrar_menu():
    print("------------MENU DE FARMACIA---------------")
    print("1. Registrar nuevo paciente")
    print("2. Atender siguiente paciente")
    print("3. Mostrar turnos pendientes")
    print("4. SALIR")


def main():
    cola_turnos = Cola_Turnos()

    while True:
        mostrar_menu()
        opcion = input("Bienvenido, seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            servicio = input("Tipo de servicio: (Consulta/Compra/Receta):  ")
            paciente = Paciente(nombre, servicio)
            cola_turnos.agregar_turno(paciente)

        elif opcion =="2":
            cola_turnos.atender_turno()

        elif opcion == "3":
            cola_turnos.mostrar_pendientes()

        elif opcion == "4":
            print("Saliendo del programa, hasta luego!")
            break

        else:
            print("Opcion invalida, por favor ingrese nuevamente")

    
if __name__ == "__main__":
    main()
