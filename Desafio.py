# mesa_de_partes.py - Mesa de Partes Digital IEI N°084 "Virgen María"
RUTA = "expedientes.txt"   
MAX = 100                  
def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

def validar_nombre(nombre):
    return len(nombre.strip()) >= 3 and nombre.replace(" ", "").isalpha()

def validar_tramite(tramite):
    return tramite.strip().lower() in ("inscripcion", "traslado")

def pedir_dato(mensaje, validador, error):
    while True:
        valor = input(mensaje).strip()
        if validador(valor):
            return valor          
        print(error)              
