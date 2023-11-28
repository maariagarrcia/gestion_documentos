from fastapi import HTTPException
from fastapi import status


class GuardadorEnArchivo:
    def guardar(self, info: str):
        pass

class GuardadorEnArchivoReal(GuardadorEnArchivo):
    def guardar(self, info: str):
        with open("registros_clic.txt", "a") as archivo:
            archivo.write(info + "\n")

class ProxyGuardadorEnArchivo(GuardadorEnArchivo):
    def __init__(self, guardador_real, permitted_users):
        self.guardador_real = guardador_real
        self.permitted_users = permitted_users

    def guardar(self, info: str, user_id: str):
        if user_id not in self.permitted_users:
            raise PermissionDeniedException()

        print("Registrando clic...")
        self.guardador_real.guardar(info)
        print("Clic registrado con éxito")


class PermissionDeniedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="No tienes permisos para registrar clics")

# Crear instancias de las clases
guardador_real = GuardadorEnArchivoReal()

# Definir usuarios permitidos y no permitidos para registrar clics
usuarios_permitidos = {"1"}  # Puedes ajustar esto según tus necesidades
proxy_guardador = ProxyGuardadorEnArchivo(guardador_real, usuarios_permitidos)
