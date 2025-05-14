from Modulos import ColaClinica

cola = ColaClinica()

while True:
    print("\n--- Menú Clínica ---")
    print("1. Registrar paciente")
    print("2. Atender siguiente paciente")
    print("3. Ver pacientes en espera")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre del paciente: ")
        cola.insertar_paciente(nombre)
    elif opcion == "2":
        cola.atender_paciente()
    elif opcion == "3":
        cola.mostrar_cola()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")
