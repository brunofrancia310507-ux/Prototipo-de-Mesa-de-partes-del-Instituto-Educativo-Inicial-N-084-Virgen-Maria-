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
