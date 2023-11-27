# Interfaz para el guardador en archivo
class GuardadorEnArchivo:
    def guardar(self, info: str):
        pass

# Implementación concreta del guardador en archivo
class GuardadorEnArchivoReal(GuardadorEnArchivo):
    def guardar(self, info: str):
        with open("registros_clic.txt", "a") as archivo:
            archivo.write(info + "\n")

# Proxy para el guardador en archivo
class ProxyGuardadorEnArchivo(GuardadorEnArchivo):
    def __init__(self, guardador_real):
        self.guardador_real = guardador_real

    def guardar(self, info: str):
        # Lógica adicional antes de guardar
        print("Registrando clic...")

        # Llamada al método original
        self.guardador_real.guardar(info)

        # Lógica adicional después de guardar
        print("Clic registrado con éxito")

# Crear instancias de las clases
guardador_real = GuardadorEnArchivoReal()
proxy_guardador = ProxyGuardadorEnArchivo(guardador_real)


