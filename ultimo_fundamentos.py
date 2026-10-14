
#BRUNO
def ejecutar_mesa_partes():     
    # Creamos listas (equivalentes a los arreglos en paralelo)
    dnis = []
    nombres = []
    tramites = []
    
    # Nombre del archivo de texto para la persistencia
    archivo_txt = "tramites_mesa_partes.txt"

    while True:
        print("\n==========================================")
        print("   MESA DE PARTES - COLEGIO VIRGEN MARÍA   ")
        print("==========================================")
        print("1. Registrar nuevo trámite")
        print("2. Buscar trámite por DNI")
        print("3. Ordenar y mostrar trámites")
        print("4. Mostrar todos los datos")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        

        # OPCIÓN 1: REGISTRAR TRÁMITE    
        if opcion == "1":
            print("\n--- REGISTRO DE EXPEDIENTE ---")
            if len(dnis) < 100:
                dni = input("Ingresa el DNI del apoderado (8 dígitos): ")
                nombre_apoderado = input("Ingresa el nombre completo: ")
                tipo_tramite = input("Tipo de trámite (Inscripción / Traslado): ")

                # Guardamos la información en las listas
                dnis.append(dni)
                nombres.append(nombre_apoderado)
                tramites.append(tipo_tramite)

                # Guardamos una copia automática en un archivo de texto (.txt)
                with open(archivo_txt, "a", encoding="utf-8") as archivo:
                    archivo.write(f"DNI: {dni} | Apoderado: {nombre_apoderado} | Trámite: {tipo_tramite}\n")

                print("¡Trámite registrado y guardado en archivo con éxito!")
            else:
                print("¡Error! El sistema está lleno.")

        # OPCIÓN 2: BUSCAR POR DNI   ( MARCUS )
        elif opcion == "2":
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

        # OPCIÓN 3: ORDENAR Y MOSTRAR (Método Burbuja)   (LUZ POMA)
        elif opcion == "3":
            print("\n--- LISTADO ORDENADO POR DNI ---")
            if len(dnis) > 0:
                n = len(dnis)
                # Algoritmo de ordenamiento burbuja
                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if dnis[j] > dnis[j + 1]:
                            # Ordenamos el DNI
                            dnis[j], dnis[j + 1] = dnis[j + 1], dnis[j]
                            # Movemos el nombre en paralelo para que no se mezcle
                            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                            # Movemos el trámite en paralelo
                            tramites[j], tramites[j + 1] = tramites[j + 1], tramites[j]

                # Mostramos la lista ordenada en pantalla
                for i in range(len(dnis)):
                    print(f"DNI: {dnis[i]} - Apoderado: {nombres[i]} - Trámite: {tramites[i]}")
            else:
                print("No hay trámites registrados para ordenar.")

        # OPCIÓN 4: MOSTRAR DATOS  (JHONATAN)
        elif opcion == "4":
            print("\n--- DATOS REGISTRADOS ---")
            if len(dnis) > 0:
                for i in range(len(dnis)):
                    print(f"DNI: {dnis[i]} | Apoderado: {nombres[i]} | Trámite: {tramites[i]}")
                    print("-" * 40)
            else:
                print("No hay registros todavía.")
                
               
        # OPCIÓN SALIR - NINANQUI ZARATE CARLOS
        # OPCIÓN 5: SALIR
        elif opcion == "5":
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 5.")

        if opcion != "5":
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    ejecutar_mesa_partes()