import csv

ARCHIVO = "clientes.txt"

class Cliente:
    def __init__(self, cedula, nombre, saldo):
        self.cedula = cedula
        self.nombre = nombre
        self.saldo = float(saldo)

    def __str__(self):
        return f"{self.cedula},{self.nombre},{self.saldo}"

def cargar_clientes():
    clientes = []
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # saltar cabecera
            for row in reader:
                if len(row) == 3:
                    clientes.append(Cliente(row[0], row[1], row[2]))
    except FileNotFoundError:
        print("No se encontró el archivo de clientes.")
    return clientes

def consultar_saldo(clientes, nombre):
    encontrados = [c for c in clientes if c.nombre.lower() == nombre.lower()]
    if encontrados:
        for c in encontrados:
            print(f"El saldo de {c.nombre} es: ${c.saldo:.2f}")
    else:
        print("Cliente no encontrado.")

def contar_mayores_50(clientes):
    cantidad = sum(1 for c in clientes if c.saldo > 50)
    print(f"Clientes con saldo mayor a 50: {cantidad}")

def listar_ordenados(clientes):
    ordenados = sorted(clientes, key=lambda c: c.saldo)
    print("\nClientes ordenados por saldo:")
    for c in ordenados:
        print(f"{c.nombre} - ${c.saldo:.2f}")

def menu():
    clientes = cargar_clientes()
    if not clientes:
        return
    
    while True:
        print("\n=== MENÚ BANCO ===")
        print("1. Consultar saldo por nombre")
        print("2. Contar clientes con saldo mayor a 50")
        print("3. Listar clientes ordenados por saldo (ascendente)")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            consultar_saldo(clientes, nombre)
        elif opcion == "2":
            contar_mayores_50(clientes)
        elif opcion == "3":
            listar_ordenados(clientes)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

# Ejecutar menú
if __name__ == "__main__":
    menu()