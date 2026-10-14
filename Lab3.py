# ---------- Funciones de ordenamiento (se definen primero) ----------
def burbuja(a):
    a = a[:]
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def seleccion(a):
    a = a[:]
    for i in range(len(a) - 1):
        menor = i
        for j in range(i + 1, len(a)):
            if a[j] < a[menor]:
                menor = j
        a[i], a[menor] = a[menor], a[i]
    return a


# ---------- Etapa 1: lista unidimensional ----------
print("\n=== ETAPA 1 ===")
nums = [4, 9, 1, 7, 3, 8, 2, 6, 5, 10]
for n in nums:
    print(n)
nums[2] = int(input("Nuevo valor para la posición 3: "))
print("Lista modificada:", nums)
x = int(input("Número a buscar: "))
print("Existe" if x in nums else "No existe")

# ---------- Etapa 2: matriz 3x3 ----------
print("\n=== ETAPA 2 ===")
m = [[0] * 3 for _ in range(3)]
total = 0
for i in range(3):
    for j in range(3):
        m[i][j] = int(input(f"m[{i}][{j}]: "))
        total += m[i][j]
for fila in m:
    print(fila)
print("Suma:", total)

# ---------- Etapa 3: menú con lista dinámica ----------
print("\n=== ETAPA 3 ===")
lista = []
while True:
    op = input("1.Insertar 2.Eliminar 3.Buscar 4.Mostrar 5.Salir: ")
    if op == "1":
        lista.append(int(input("Valor: ")))
    elif op == "2":
        pos = int(input("Posición: "))
        if 0 <= pos < len(lista):
            lista.pop(pos)
        else:
            print("Posición fuera de rango")
    elif op == "3":
        v = int(input("Valor: "))
        print(lista.index(v) if v in lista else "No está")
    elif op == "4":
        print(lista)
    elif op == "5":
        break
    else:
        print("Opción inválida")

# ---------- Etapa 4: ordenamiento ----------
print("\n=== ETAPA 4 ===")
datos = [64, 25, 12, 22, 11, 90, 5]
print("Antes:", datos)
print("Burbuja:", burbuja(datos))
print("Selección:", seleccion(datos))