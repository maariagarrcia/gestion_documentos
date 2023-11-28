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
    def __init__(self, guardador_real, permitted_users, intentos_fallidos_guardador):
        self.guardador_real = guardador_real
        self.permitted_users = permitted_users
        self.intentos_fallidos_guardador = intentos_fallidos_guardador

    def guardar(self, info: str, user_id: str):
        if user_id not in self.permitted_users:
            # Guardar intento fallido en un archivo antes de lanzar la excepción
            self.intentos_fallidos_guardador.guardar(info, user_id)
            raise PermissionDeniedException()

        print("Registrando clic...")
        self.guardador_real.guardar(info)
        print("Clic registrado con éxito")



class IntentosFallidosGuardadorEnArchivo:
    def guardar(self, info: str, user_id: str):
        with open("intentos_fallidos.txt", "a") as archivo:
            archivo.write(f"Intento fallido - User ID: {user_id}, Info: {info}\n")

class ProxyIntentosFallidosGuardadorEnArchivo(IntentosFallidosGuardadorEnArchivo):
    def __init__(self, intentos_fallidos_guardador_real):
        self.intentos_fallidos_guardador_real = intentos_fallidos_guardador_real

    def guardar(self, info: str, user_id: str):
        # Guardar intento fallido antes de llamar al guardador real
        super().guardar(info, user_id)
        # Llamar al guardador real para realizar acciones adicionales, si es necesario
        self.intentos_fallidos_guardador_real.guardar(info, user_id)




class PermissionDeniedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="No tienes permisos para registrar clics")


# Crear instancias de las clases
guardador_real = GuardadorEnArchivoReal()
intentos_fallidos_guardador_real = IntentosFallidosGuardadorEnArchivo()
proxy_intentos_fallidos_guardador = ProxyIntentosFallidosGuardadorEnArchivo(intentos_fallidos_guardador_real)
usuarios_permitidos = {"2"}  # Puedes ajustar esto según tus necesidades
proxy_guardador = ProxyGuardadorEnArchivo(guardador_real, usuarios_permitidos, proxy_intentos_fallidos_guardador)
