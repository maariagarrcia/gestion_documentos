GESTOR DE DOCUMENTOS
-------------------
 
 - **Document (Documento):**
   - Representa un archivo con nombre, tipo (texto, imagen, video), tamaño y url.
   - Puede ser accedido y modificado.
   - Para documentos sensibles, se registra quién y cuándo accede o modifica.
 
 - **Link (Url):**
   - Es una referencia a otro documento o carpeta.
   - No tiene contenido propio, pero proporciona un acceso rápido a la información referenciada.
 
 - **Folder (Carpeta):**
   - Es un contenedor que alberga documentos, enlaces y otras carpetas.
   - Su tamaño es la suma de los tamaños de los elementos contenidos.
 
 - **AccessProxy (Proxy de Acceso):**
   - Actúa como intermediario para acceder a documentos sensibles.
   - Registra cada acceso o modificación a documentos sensibles.
   - Solo permite el acceso a usuarios autorizados.
 
 **2. EXPLICACIÓN:**
El sistema de gestión documental va más allá de ser una simple plataforma de almacenamiento. Permite a los usuarios realizar una variedad de acciones, desde la creación y modificación de documentos hasta la organización y gestión de carpetas y archivos. La estructura jerárquica facilita la ubicación rápida de la información, promoviendo la eficiencia en la gestión del conocimiento.

- Creación y Modificación de Documentos:
 Los usuarios pueden crear nuevos documentos con atributos detallados como nombre, tipo y URL. La posibilidad de modificar el contenido garantiza la flexibilidad en la gestión de   información.
- Organización de Carpetas:
 La inclusión de carpetas permite a los usuarios organizar sus documentos de manera jerárquica. Esto es esencial para proyectos complejos con múltiples documentos relacionados.
- Gestión de Enlaces:
 Los enlaces actúan como referencias rápidas a otros documentos o carpetas, facilitando la interconexión de información y mejorando la accesibilidad.
- Eficiencia en la Recuperación de Información:
 La estructura jerárquica de carpetas permite una recuperación rápida y eficiente de la información, reduciendo el tiempo necesario para encontrar documentos específicos.

 
 **3. PATRONES DE DISEÑO:**
 - COMPOSITE: El composite es un patrón estructural que permite utlizar colectivamente un conjunto de objetos como una entidad única, independiendtemente de si son objetos           individuales o estructuras compuestas de múltiples objetos.
  Por ello, podremos observar como está estructurado en carpetas y archivos nuestro gestor, el usuario podrá crear, eliminar, modificar, buscar y ver sus documentos.
  Recalcar que una carpeta es un conjunto de archivos o de carpetas también. Todos los datos recogidos de la base de datos se convierten en objetos para el frontend y un buen uso    de este patrón.
  La implementación del patrón composite no solo simplifica la interacción con documentos y carpetas, sino que también facilita la expansión y adaptación del sistema a medida que    crece la cantidad de información.


 - PROXY: El proxy es un patrón estructural que permite tener un objeto representante o sustitutot para controlar el acceso al objeto real.
   Lo usaremos de intermediario para interactuar con el objeto real.
   Por ello, garantizaremos la seguridad y trazabilidad en el acceso a documentos sensibles, realizando pruebas de acceso con el proxy, mostrando cómo se registra el acceso 
   y cómo se controla el acceso a través del proxy.
   Al tener en el frontend objetos estructurados que nos devuelve el patrón composite podremos usar ahi el proxy ya que no estamos usando datos sino objetos.
   El uso del patrón proxy asegura que el acceso a documentos sensibles sea controlado y rastreado. Esto no solo mejora la seguridad, sino que también proporciona un registro         claro de las interacciones, crucial para la conformidad y auditoría.

