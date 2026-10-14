# OPCIÓN 2: BUSCAR POR DNI  ( MARCUS )
if opcion == "2":
    print("\n--- BÚSQUEDA DE TRÁMITE ---")
    dni_buscar = input("Ingresa el DNI que deseas buscar: ")
    encontrado = False

    # Recorremos la lista buscando coincidencia
    for i in range(len(dnis)):
        if dnis[i] == dni_buscar:
            print("\n¡Trámite encontrado!")
            print(f"DNI: {dnis[i]}")
            print(f"Apoderado: {nombres[i]}")
            print(f"Trámite: {tramites[i]}")
            encontrado = True

    if not encontrado:
        print("No se encontró ningún trámite con ese DNI.")
