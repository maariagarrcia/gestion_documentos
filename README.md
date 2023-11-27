# gestion_documentos
# -------------------

 **1. Clases Principales:**
 
 - **Document (Documento):**
   - Representa un archivo con nombre, tipo (texto, imagen, video), tamaño y contenido.
   - Puede ser accedido y modificado.
   - Para documentos sensibles, se registra quién y cuándo accede o modifica.
 
 - **Link (Enlace):**
   - Es una referencia a otro documento o carpeta.
   - No tiene contenido propio, pero proporciona un acceso rápido a la información referenciada.
 
 - **Folder (Carpeta):**
   - Es un contenedor que alberga documentos, enlaces y otras carpetas.
   - Su tamaño es la suma de los tamaños de los elementos contenidos.
 
 - **AccessProxy (Proxy de Acceso):**
   - Actúa como intermediario para acceder a documentos sensibles.
   - Registra cada acceso o modificación a documentos sensibles.
   - Solo permite el acceso a usuarios autorizados.
 
 **2. Funciones de Manipulación del Sistema:**
 
 - **navegar_por_estructura:**
   - Permite recorrer la estructura de documentos mostrando sus nombres.
 
 - **añadir_documento_a_carpeta y eliminar_elemento_de_carpeta:**
   - Facilitan la manipulación de elementos en una carpeta.
 
 - **acceder_a_documento_con_proxy y modificar_documento_con_proxy:**
   - Utilizan el Proxy para controlar y registrar el acceso a documentos sensibles.
   - El Proxy registra el acceso y permite o deniega el acceso según la autorización del usuario.
 
 **3. Pruebas:**
 
 - Se realizaron pruebas de acceso con el proxy, mostrando cómo se registra el acceso 
 y cómo se controla el acceso a través del proxy.
 
 En resumen, el código implementa un sistema de gestión documental 
 donde puedes crear documentos, carpetas y enlaces. Un proxy garantiza la 
  seguridad y trazabilidad en el acceso a documentos sensibles. Las funciones 
 permiten realizar operaciones como navegar por la estructura, añadir o eliminar elementos,
 y acceder a documentos mediante el uso del proxy. Las pruebas validan la correcta 
 implementación del sistema, especialmente en lo que respecta a la seguridad y el 
 registro de acceso a documentos.