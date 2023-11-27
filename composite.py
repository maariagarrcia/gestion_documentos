from typing import List

class Componente:
    """
    Clase base para el patrón Composite
    """
    def obtener_detalles(self) -> str:
        """
        Método para obtener detalles específicos del componente
        """
        pass

class Archivo(Componente):
    nombre: str

    def __init__(self, nombre: str):
        self.nombre = nombre

    def obtener_detalles(self) -> List[str]:
        return [f"Archivo: {self.nombre}"]

class Carpeta(Componente):
    nombre: str
    contenido: List[Componente]

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.contenido = []

    def agregar_componente(self, componente: Componente):
        self.contenido.append(componente)

    def obtener_detalles(self) -> List[str]:
        detalles = [f"Carpeta: {self.nombre}"]
        for componente in self.contenido:
            detalles.extend(componente.obtener_detalles())
        return detalles

# Ejemplo de uso
#if __name__ == "__main__":
#    archivo1 = Archivo(nombre="Documento1.txt")
#    archivo2 = Archivo(nombre="Documento2.docx")
#
#    carpeta1 = Carpeta(nombre="Carpeta1")
#    carpeta1.agregar_componente(archivo1)
#
#    carpeta2 = Carpeta(nombre="Carpeta2")
#    carpeta2.agregar_componente(archivo2)
#
#    carpeta_principal = Carpeta(nombre="Documentos")
#    carpeta_principal.agregar_componente(carpeta1)
#    carpeta_principal.agregar_componente(carpeta2)
#    carpeta_principal.agregar_componente(Archivo(nombre="Documento3.pdf"))
#
#    print("Detalles de la carpeta principal:")
#    print(carpeta_principal.obtener_detalles())
