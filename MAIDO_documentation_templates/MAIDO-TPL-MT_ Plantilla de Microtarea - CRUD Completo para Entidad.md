# **MAIDO-TPL-MT: Plantilla de Microtarea - CRUD Completo para Entidad**

Referencia MAIDO: Plantilla de Microtarea Específica

Versión de la Plantilla: 1.0

Fecha: \[Fecha_Creacion_o_Ultima_Modificacion_de_esta_plantilla\]

## **1. Propósito de esta Plantilla**

- Proporcionar una estructura detallada para definir microtareas que
  involucren la implementación de funcionalidades CRUD (Create, Read,
  Update, Delete) completas para una entidad específica dentro de un
  proyecto que sigue la metodología MAIDO.

- Facilitar al Product Visionary la especificación de todos los
  requisitos necesarios de manera clara y completa.

- Permitir al AI Orquester (el orquestador) generar un "Paquete de Tarea
  Inteligente" exhaustivo para el LLM de Codificación o para la
  implementación directa de los componentes de backend (Servidor MCP) y
  frontend.

- Asegurar que se consideren todos los aspectos de una funcionalidad
  CRUD, desde la interfaz de usuario hasta la lógica de negocio y la
  interacción con la base de datos.

## **2. Cuándo Usar esta Plantilla**

Utilizar esta plantilla cuando una microtarea del "Plan de Desarrollo
Incremental" (MAIDO-TPL-06) tenga como objetivo principal implementar
las operaciones CRUD para una entidad de datos del sistema (ej. "Gestión
de Tareas", "Administración de Usuarios", "Manejo de Eventos de
Agenda").

## **3. Información a ser Completada por el Product Visionary (con asistencia del Orquestador)**

**(El orquestador puede pre-rellenar secciones basándose en otros
documentos del proyecto y luego solicitar validación/completitud al
Product Visionary)**

### **3.1. Identificación de la Microtarea**

- **ID de la Microtarea (del Plan de Desarrollo):**
  \[ID_Microtarea_Ej_MVP1-TAREAS-BF001\]

- **Título Descriptivo de la Microtarea:** \[Ej. Implementación CRUD
  Completo para la Entidad "Tareas"\]

- **Objetivo Principal de la Microtarea:** \[Ej. Permitir a los usuarios
  crear, ver, listar, modificar y eliminar "Tareas" en el sistema\]

### **3.2. Entidad Principal Involucrada**

- **Nombre de la Entidad:** \[Ej. Tarea, EventoAgenda, ElementoZerebro,
  PerfilUsuario\]

- **Descripción Breve de la Entidad:** \[Propósito de esta entidad en el
  sistema\]

- **Referencia al Modelo de Datos (en MAIDO-TPL-04):** \[Sección o
  nombre de la tabla/colección que representa esta entidad\]

### **3.3. Documentos Maestros de Referencia del Proyecto**

- **Especificaciones Funcionales (MAIDO-TPL-03):** \[Sección(es)
  relevante(s) para esta entidad/funcionalidad\]

- **Arquitectura Técnica (MAIDO-TPL-04):** \[Sección del Modelo de
  Datos, Tecnologías implicadas\]

- **Contrato API/MCP (MAIDO-TPL-05):** \[Nombres de herramientas MCP a
  crear/usar para esta entidad\]

- **Sistema de Diseño UI (MAIDO-TPL-09):** \[Componentes UI
  reutilizables a emplear, principios de diseño\]

- **Nomenclaturas y Convenciones (MAIDO-TPL-08):** \[A aplicar en
  código, API, DB\]

### **3.4. Especificación de Funcionalidades CRUD**

#### **3.4.1. Crear (Create) Entidad**

- **Flujo de Usuario (Alto Nivel):** \[Ej. 1. Usuario hace clic en
  "Nueva Tarea". 2. Se muestra formulario. 3. Usuario rellena datos y
  guarda. 4. Sistema confirma creación y muestra la nueva tarea.\]

- **Acceso/Permisos:** ¿Quién puede crear esta entidad?

- **Formulario de Creación (Campos):**

  - Para cada campo:

    - **Nombre del Campo (Label UI):**

    - **Atributo de la Entidad (Backend/DB):**

    - **Tipo de Input UI:** (Ej. text, textarea, date, select, checkbox,
      file, number)

    - **¿Obligatorio?:** (Sí/No)

    - **Validaciones (Frontend y Backend):** (Ej. formato, longitud,
      rango, requerido si otro campo X tiene valor Y)

    - **Valor por Defecto (si tiene):**

    - **Ayuda Contextual/Placeholder:**

    - **Opciones (para select, radio, checkbox group):** \[Fuente de las
      opciones: estática, otra entidad, API\]

- **Acción de Guardado:**

  - ¿Qué sucede al guardar? (Llamada a herramienta MCP, feedback al
    usuario).

- **Mensajes al Usuario:** (Éxito, error de validación, error del
  servidor).

- **Herramienta(s) MCP Implicada(s) (Backend):** \[Ej.
  entidad.create(datosEntidad)\]

  - Parámetros Esperados:

  - Respuesta Esperada (Éxito/Error):

- **Componentes UI Implicados (Frontend):** \[Ej. FormularioCrearTarea,
  InputText, DatePickerComponent, BotonGuardar de la biblioteca
  MAIDO-TPL-09\]

#### **3.4.2. Leer (Read) - Listar Entidades**

- **Flujo de Usuario (Alto Nivel):** \[Ej. 1. Usuario navega a la
  sección "Mis Tareas". 2. Se muestra una lista/tabla de tareas.\]

- **Acceso/Permisos:** ¿Quién puede listar estas entidades? ¿Se filtran
  por usuario?

- **Visualización de la Lista/Tabla:**

  - **Campos a Mostrar por Ítem:** \[Ej. Título, Fecha Límite
    (abreviada), Prioridad, Estado\]

  - **Ordenación por Defecto:** \[Ej. por Fecha de Creación
    descendente\]

  - **Opciones de Ordenación para el Usuario:** \[Ej. por Título, por
    Fecha Límite\]

  - **Paginación:** (Sí/No. Si sí, ¿cuántos ítems por página?)

  - **Funcionalidad de Búsqueda/Filtrado:**

    - Campos por los que se puede buscar/filtrar:

    - Tipos de filtro: (Ej. texto libre, selección de estado, rango de
      fechas)

- **Acciones por Ítem en la Lista:** \[Ej. Ver Detalle, Editar Rápido,
  Eliminar\]

- **Mensajes al Usuario:** (Ej. "No hay tareas para mostrar", error al
  cargar).

- **Herramienta(s) MCP Implicada(s) (Backend):** \[Ej.
  entidad.list(filtros, orden, paginacion)\]

  - Parámetros Esperados:

  - Respuesta Esperada (Lista de entidades, metadatos de paginación):

- **Componentes UI Implicados (Frontend):** \[Ej. TablaTareas,
  ElementoListaTarea, Paginador, BarraBusquedaFiltros\]

#### **3.4.3. Leer (Read) - Ver Detalle de una Entidad**

- **Flujo de Usuario (Alto Nivel):** \[Ej. 1. Usuario hace clic en una
  tarea de la lista. 2. Se muestra una vista detallada de la tarea.\]

- **Acceso/Permisos:** ¿Quién puede ver el detalle de esta entidad?

- **Visualización del Detalle:**

  - **Campos a Mostrar:** \[Listar todos los campos relevantes de la
    entidad y cómo se presentarán\]

  - **Información Relacionada a Mostrar:** (Ej. subtareas, comentarios,
    archivos adjuntos)

- **Acciones Disponibles en la Vista de Detalle:** \[Ej. Editar,
  Eliminar, Cambiar Estado, Añadir Comentario\]

- **Mensajes al Usuario:** (Ej. "Tarea no encontrada", error al cargar).

- **Herramienta(s) MCP Implicada(s) (Backend):** \[Ej.
  entidad.get(idEntidad)\]

  - Parámetros Esperados:

  - Respuesta Esperada (Objeto de la entidad detallada):

- **Componentes UI Implicados (Frontend):** \[Ej. VistaDetalleTarea,
  SeccionComentarios\]

#### **3.4.4. Actualizar (Update) Entidad**

- **Flujo de Usuario (Alto Nivel):** \[Ej. 1. Usuario está en la vista
  de detalle y hace clic en "Editar". 2. Se muestra formulario
  pre-cargado con datos. 3. Usuario modifica y guarda.\]

- **Acceso/Permisos:** ¿Quién puede actualizar esta entidad? ¿Hay campos
  que solo ciertos roles pueden modificar?

- **Formulario de Edición (Campos):** Similar al de Creación, pero
  pre-cargado.

  - Indicar si hay campos que no son editables.

- **Acción de Guardado:**

  - ¿Qué sucede al guardar? (Llamada a herramienta MCP, feedback al
    usuario).

  - Manejo de concurrencia (optimistic/pessimistic locking, si aplica).

- **Mensajes al Usuario:** (Éxito, error de validación, error del
  servidor, conflicto de concurrencia).

- **Herramienta(s) MCP Implicada(s) (Backend):** \[Ej.
  entidad.update(idEntidad, datosActualizados)\]

  - Parámetros Esperados:

  - Respuesta Esperada (Entidad actualizada o confirmación):

- **Componentes UI Implicados (Frontend):** \[Ej. FormularioEditarTarea
  (puede ser el mismo que FormularioCrearTarea con lógica adicional)\]

#### **3.4.5. Eliminar (Delete) Entidad**

- **Flujo de Usuario (Alto Nivel):** \[Ej. 1. Usuario hace clic en
  "Eliminar" en una tarea. 2. Se pide confirmación. 3. Usuario
  confirma. 4. Sistema elimina y notifica.\]

- **Acceso/Permisos:** ¿Quién puede eliminar esta entidad?

- **Confirmación Requerida:** (Sí/No. Altamente recomendado que sí).

  - Mensaje de Confirmación:

- **Tipo de Eliminación:** (Lógica o Física. ¿Qué sucede con los datos
  relacionados? ¿Cascada, set null, restringir?).

- **Mensajes al Usuario:** (Éxito, error, "No se puede eliminar porque
  X").

- **Herramienta(s) MCP Implicada(s) (Backend):** \[Ej.
  entidad.delete(idEntidad)\]

  - Parámetros Esperados:

  - Respuesta Esperada (Confirmación):

- **Componentes UI Implicados (Frontend):** \[Ej.
  ModalConfirmacionEliminar, Botón de Eliminar\]

### **3.5. Requisitos No Funcionales Específicos para esta Entidad/Funcionalidad**

- **Rendimiento:** \[Ej. La lista de tareas debe cargar en menos de X
  segundos para 1000 tareas\]

- **Seguridad:** \[Ej. Solo el propietario de la tarea puede modificarla
  o eliminarla, los datos de la tarea X deben estar encriptados en la
  BD\]

- **Usabilidad:** \[Ej. El formulario de creación debe poder completarse
  en menos de Y clics para los campos obligatorios\]

### **3.6. Criterios de Aceptación Detallados para la Microtarea**

*(Lista de escenarios "Dado... Cuando... Entonces..." para probar cada
funcionalidad CRUD)*

1.  **Crear:**

    - Dado que el usuario está autenticado, Cuando rellena el formulario
      de nueva tarea con datos válidos y guarda, Entonces la tarea se
      crea en el sistema Y se muestra un mensaje de éxito Y el usuario
      ve la nueva tarea.

    - Dado que el usuario intenta crear una tarea sin un título, Cuando
      guarda, Entonces se muestra un error de validación Y la tarea no
      se crea.

    - ... (más escenarios de creación, incluyendo casos límite y
      errores)

2.  **Listar:**

    - Dado que el usuario tiene N tareas, Cuando accede a la lista de
      tareas, Entonces se muestran las N tareas con los campos X, Y, Z.

    - Dado que el usuario aplica un filtro por "Estado: Completada",
      Cuando la lista se actualiza, Entonces solo se muestran tareas
      completadas.

    - ... (más escenarios de listado, filtros, ordenación, paginación)

3.  **Ver Detalle:**

    - Dado que existe una tarea con ID X, Cuando el usuario solicita ver
      el detalle de la tarea X, Entonces se muestran todos los campos
      relevantes de la tarea X.

    - ...

4.  **Actualizar:**

    - Dado que el usuario está editando una tarea existente, Cuando
      modifica el título y guarda, Entonces la tarea se actualiza con el
      nuevo título Y se muestra un mensaje de éxito.

    - ...

5.  **Eliminar:**

    - Dado que el usuario confirma la eliminación de una tarea, Cuando
      el sistema procesa la solicitud, Entonces la tarea ya no es
      visible en la lista Y se muestra un mensaje de éxito.

    - ...

### **3.7. Dependencias de esta Microtarea**

- **Microtareas Previas Requeridas:** \[IDs de microtareas que deben
  estar completadas antes de iniciar esta\]

- **Impacto en Microtareas Futuras:** \[IDs de microtareas que dependen
  de la finalización de esta\]

## **4. Instrucciones para el AI Orquester**

- Utilizar la información de esta plantilla completada para generar el
  "Paquete de Tarea Inteligente" para el LLM de Codificación (si la
  implementación es compleja) o las functionCalls MCP directas (si la
  implementación es más sencilla y el Servidor MCP tiene herramientas de
  alto nivel).

- Asegurar que el paquete/functionCall incluya referencias a los
  componentes UI del Sistema de Diseño (MAIDO-TPL-09) y a las
  herramientas MCP definidas en el Contrato API (MAIDO-TPL-05).

- Incluir los Criterios de Aceptación en el paquete para guiar la
  generación de pruebas o la guía de verificación.

- Considerar la generación de esqueletos de código para los componentes
  frontend y las funciones backend basadas en esta especificación.

## **5. Historial de Versiones de esta Plantilla (si se modifica la plantilla en sí)**

- **v1.0 (\[Fecha\]):** Creación inicial.
