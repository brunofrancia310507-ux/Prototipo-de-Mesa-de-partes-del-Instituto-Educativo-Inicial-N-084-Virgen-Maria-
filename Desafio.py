# =====================================================================
# MESA DE PARTES DIGITAL - IEI N°084 "VIRGEN MARÍA"
# Curso: Fundamentos de Programación (CIIN1205P)
#
# ¿Qué hace el programa?
#   1. Registra expedientes (inscripción o traslado)
#   2. Valida los datos ingresados
#   3. Busca un expediente por su código
#   4. Ordena y muestra todos los expedientes
#   5. Guarda y carga los datos desde un archivo de texto
#
# ¿Cómo guarda los datos en memoria?
#   Con ARREGLOS PARALELOS (listas): la posición i de cada lista
#   pertenece al MISMO expediente. Ejemplo, el expediente 0 es:
#   codigos[0], dnis[0], apoderados[0], alumnos[0], tramites[0]
# =====================================================================

# --- Constantes globales ---------------------------------------------
RUTA = "expedientes.txt"   # archivo donde se guardan los datos (persistencia)
MAX = 100                  # capacidad máxima de expedientes del prototipo


# =====================================================================
# PERSONA 2: VALIDACIONES
# Cada función recibe un texto (cadena) y devuelve True si es válido
# o False si no lo es. Así se evitan datos incompletos o ilegibles.
# =====================================================================

def validar_dni(dni):
    # isdigit() -> True si TODOS los caracteres son números
    # len(dni) == 8 -> el DNI peruano tiene exactamente 8 dígitos
    return dni.isdigit() and len(dni) == 8


def validar_nombre(nombre):
    # strip() quita espacios al inicio y al final
    # replace(" ", "") quita los espacios internos para poder usar isalpha()
    # isalpha() -> True si solo hay letras (así se rechazan números o símbolos)
    # len >= 3 -> evita nombres demasiado cortos o vacíos
    return len(nombre.strip()) >= 3 and nombre.replace(" ", "").isalpha()


def validar_tramite(tramite):
    # lower() pasa a minúsculas para aceptar "Traslado", "TRASLADO", etc.
    # Solo se permiten los dos trámites que se observaron en el colegio
    return tramite.strip().lower() in ("inscripcion", "traslado")


def pedir_dato(mensaje, validador, error):
    # Función reutilizable: pide un dato por teclado y lo vuelve a pedir
    # (ciclo while) hasta que la función 'validador' diga que es correcto.
    #   mensaje   -> texto que se muestra al usuario
    #   validador -> función de validación a usar (validar_dni, etc.)
    #   error     -> mensaje si el dato es incorrecto
    while True:
        valor = input(mensaje).strip()
        if validador(valor):
            return valor          # dato correcto: sale del ciclo y lo devuelve
        print(error)              # dato incorrecto: avisa y repite


# =====================================================================
# PERSONA 3: REGISTRO
# =====================================================================

def generar_codigo(total):
    # Crea un código único según cuántos expedientes ya existen.
    # f"{total + 1:04d}" rellena con ceros hasta 4 dígitos.
    # Ejemplo: total=0 -> "EXP-0001", total=24 -> "EXP-0025"
    return f"EXP-{total + 1:04d}"


def registrar(codigos, dnis, apoderados, alumnos, tramites):
    # Verifica que todavía haya espacio (estructura condicional)
    if len(codigos) >= MAX:
        print("Error: sistema lleno")
        return                    # sale de la función sin registrar

    # Pide cada dato validándolo con la función pedir_dato
    dni = pedir_dato("DNI del apoderado (8 dígitos): ", validar_dni, "DNI inválido")
    apoderado = pedir_dato("Nombre del apoderado: ", validar_nombre, "Nombre inválido")
    alumno = pedir_dato("Nombre del estudiante: ", validar_nombre, "Nombre inválido")
    tramite = pedir_dato("Trámite (Inscripcion/Traslado): ", validar_tramite, "Trámite inválido")

    # Genera el código y agrega cada dato al FINAL de su arreglo.
    # Como todos se agregan a la vez, las posiciones siempre coinciden.
    codigo = generar_codigo(len(codigos))
    codigos.append(codigo)
    dnis.append(dni)
    apoderados.append(apoderado.title())   # title() -> "juan perez" = "Juan Perez"
    alumnos.append(alumno.title())
    tramites.append(tramite.lower())       # se guarda siempre en minúsculas
    print("Trámite registrado con éxito. Código:", codigo)


# =====================================================================
# PERSONA 4: BÚSQUEDA Y ORDENAMIENTO
# =====================================================================

def buscar(arreglo, valor):
    # BÚSQUEDA LINEAL: recorre el arreglo posición por posición.
    # Si encuentra el valor devuelve su posición (índice).
    # Si termina el recorrido sin encontrarlo devuelve -1.
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1


def mostrar_expediente(i, codigos, dnis, apoderados, alumnos, tramites):
    # Imprime los datos del expediente que está en la posición i
    print(f"{codigos[i]} | {dnis[i]} | {apoderados[i]} | {alumnos[i]} | {tramites[i]}")


def consultar(codigos, dnis, apoderados, alumnos, tramites):
    # Pide un código, lo busca y muestra el expediente si existe
    codigo = input("Código del expediente (ej. EXP-0001): ").strip().upper()
    i = buscar(codigos, codigo)        # posición del código, o -1 si no existe
    if i == -1:
        print("Expediente no encontrado")
    else:
        mostrar_expediente(i, codigos, dnis, apoderados, alumnos, tramites)


def ordenar_por_codigo(codigos, dnis, apoderados, alumnos, tramites):
    # ORDENAMIENTO BURBUJA: compara pares de vecinos y los intercambia
    # si están en desorden. Repite hasta que todo queda ordenado.
    n = len(codigos)
    for i in range(n - 1):                 # número de pasadas
        for j in range(n - 1 - i):         # compara pares (los últimos ya quedaron ordenados)
            if codigos[j] > codigos[j + 1]:
                # IMPORTANTE: se intercambian TODOS los arreglos a la vez,
                # si no, los datos de un expediente se mezclarían con otro.
                for arr in (codigos, dnis, apoderados, alumnos, tramites):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


def mostrar_todos(codigos, dnis, apoderados, alumnos, tramites):
    # Primero ordena por código y luego imprime cada expediente
    ordenar_por_codigo(codigos, dnis, apoderados, alumnos, tramites)
    if len(codigos) == 0:
        print("No hay expedientes")
    for i in range(len(codigos)):
        mostrar_expediente(i, codigos, dnis, apoderados, alumnos, tramites)


# =====================================================================
# PERSONA 5: ARCHIVOS Y PRUEBAS
# Formato del archivo: una línea por expediente, campos separados por "|"
#   EXP-0001|12345678|Maria Lopez|Ana Lopez|inscripcion
# =====================================================================

def guardar(codigos, dnis, apoderados, alumnos, tramites):
    # "w" = write: crea el archivo o lo reemplaza con los datos actuales
    # "with" cierra el archivo automáticamente al terminar
    with open(RUTA, "w", encoding="utf-8") as f:
        for i in range(len(codigos)):
            f.write(f"{codigos[i]}|{dnis[i]}|{apoderados[i]}|{alumnos[i]}|{tramites[i]}\n")
    print("Datos guardados en", RUTA)


def cargar(codigos, dnis, apoderados, alumnos, tramites):
    # Al iniciar el programa recupera los expedientes guardados antes.
    try:
        with open(RUTA, encoding="utf-8") as f:
            for linea in f:
                # strip() quita el salto de línea; split("|") separa los 5 campos
                partes = linea.strip().split("|")
                if len(partes) == 5:       # solo acepta líneas completas
                    # zip junta cada arreglo con su campo correspondiente
                    for arr, valor in zip((codigos, dnis, apoderados, alumnos, tramites), partes):
                        arr.append(valor)
    except FileNotFoundError:
        # Primera vez que se usa: el archivo aún no existe, no es un error
        pass


def ejecutar_pruebas():
    # assert verifica que una condición sea verdadera; si no, el programa
    # se detiene y muestra error. Sirve para probar las funciones.
    assert validar_dni("12345678") and not validar_dni("1234")   # DNI corto
    assert not validar_dni("12a45678")                           # DNI con letra
    assert validar_tramite("Traslado") and not validar_tramite("otro")
    assert generar_codigo(0) == "EXP-0001"

    # Prueba del ordenamiento: se dan 2 expedientes en desorden
    c = ["EXP-0002", "EXP-0001"]
    d = ["2", "1"]
    ordenar_por_codigo(c, d, ["b", "a"], ["y", "x"], ["t2", "t1"])
    # Debe quedar ordenado y con el DNI siguiendo a su código
    assert c == ["EXP-0001", "EXP-0002"] and d == ["1", "2"]
    print("Todas las pruebas pasaron")


# =====================================================================
# PERSONA 1: MENÚ PRINCIPAL
# =====================================================================

def main():
    # Crea los 5 arreglos paralelos vacíos
    codigos, dnis, apoderados, alumnos, tramites = [], [], [], [], []

    # Carga los expedientes guardados en sesiones anteriores
    cargar(codigos, dnis, apoderados, alumnos, tramites)

    # Agrupa los arreglos en una tupla para pasarlos fácilmente a las funciones.
    # El asterisco (*datos) los "desempaqueta" como 5 parámetros separados.
    datos = (codigos, dnis, apoderados, alumnos, tramites)

    # Ciclo del menú: se repite hasta que el usuario elige salir
    while True:
        print("\nMESA DE PARTES VIRTUAL - IEI 084 VIRGEN MARÍA")
        print("1. Registrar trámite")
        print("2. Buscar por código")
        print("3. Ordenar y mostrar")
        print("4. Guardar datos")
        print("5. Salir")
        op = input("Opción: ").strip()

        # Estructura condicional múltiple: ejecuta la acción según la opción
        if op == "1":
            registrar(*datos)
        elif op == "2":
            consultar(*datos)
        elif op == "3":
            mostrar_todos(*datos)
        elif op == "4":
            guardar(*datos)
        elif op == "5":
            guardar(*datos)        # guarda automáticamente para no perder trámites
            print("Hasta luego")
            break                  # rompe el ciclo y termina el programa
        else:
            print("Opción inválida")


# Este bloque ejecuta main() solo si se corre este archivo directamente
# (no si otro archivo lo importa). Es una buena práctica en Python.
if __name__ == "__main__":
    main()