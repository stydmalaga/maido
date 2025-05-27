# **MAIDO-TPL-05: Contrato de API / MCP del Proyecto - \[Nombre_del_Proyecto\]**

Versión: 1.0

Fecha: \[Fecha_Creacion_o_Ultima_Modificacion\]

Estado: Borrador / Consolidado

Proyecto: \[Nombre_del_Proyecto\]

ID del Proyecto (si aplica): \[ID_Proyecto\]

## **1. Propósito de este Documento**

- Definir el contrato de la API interna del proyecto
  "\[Nombre_del_Proyecto\]", especialmente si se utiliza el Model
  Context Protocol (MCP) para la comunicación entre el frontend (Cliente
  MCP) y el backend (Servidor MCP, ej. implementado en Supabase Edge
  Functions).

- Especificar las herramientas (funciones o métodos) expuestas por el
  Servidor MCP, sus parámetros de entrada, los formatos de respuesta
  esperados y los códigos de error.

- Servir como una referencia técnica precisa para el orquestador IA, el
  LLM de codificación y los desarrolladores del frontend y backend.

- Asegurar una comunicación coherente y predecible entre los componentes
  del sistema.

- Este documento se basa en las "Especificaciones Funcionales"
  (MAIDO-TPL-03) y la "Arquitectura Técnica" (MAIDO-TPL-04).

## **2. Principios Generales del Contrato API/MCP**

- **2.1. Formato de Mensajería:**

  - \[Ej. JSON-RPC 2.0 sobre HTTPS, RESTful con JSON, GraphQL\]. Si es
    MCP, especificar la versión y cualquier particularidad.

  - *MAIDO sugiere JSON-RPC 2.0 para MCP por su claridad en la
    definición de métodos y parámetros.*

- **2.2. Convenciones de Nomenclatura:**

  - Para nombres de herramientas/métodos: \[Ej.
    nombreModulo.accionVerbo, verboNombreModulo\]

  - Para parámetros y propiedades en payloads JSON: \[Ej. camelCase,
    snake_case\].

    - *MAIDO recomienda camelCase para los payloads JSON intercambiados
      vía MCP, y que el Servidor MCP maneje la transformación a
      snake_case si la base de datos lo requiere (como PostgreSQL).*

- **2.3. Autenticación y Autorización:**

  - ¿Cómo se pasarán los tokens de autenticación (ej. JWT de Supabase
    Auth) en las solicitudes? \[Ej. Cabecera Authorization: Bearer
    \<token\>\].

  - ¿Cómo manejará el Servidor MCP la autorización basada en roles para
    acceder a ciertas herramientas?

- **2.4. Manejo de Errores Estándar:**

  - Definir una estructura común para las respuestas de error del
    Servidor MCP.

  - **Ejemplo para JSON-RPC con MCP:**  
    {  
    "jsonrpc": "2.0",  
    "id": "\[id_de_la_peticion_original\]",  
    "error": {  
    "code": "\[codigo_de_error_numerico_estandarizado\]", // Ej. -32602
    (Invalid params), -32000 (Error específico del servidor)  
    "message": "\[mensaje_descriptivo_del_error_para_humanos\]",  
    "data": { // Opcional, para información adicional del error  
    "details":
    "\[detalles_adicionales_o_stack_trace_para_desarrollo\]",  
    "errorCodeInternal":
    "\[codigo_error_interno_del_proyecto_ej_AUTH_USER_NOT_FOUND\]"  
    }  
    }  
    }

  - Listar los códigos de error internos (errorCodeInternal) comunes y
    su significado (ver Anexo A de este documento).

- **2.5. Versionado de la API/MCP (si aplica):**

  - ¿Cómo se gestionarán los cambios en el contrato que rompan la
    compatibilidad? \[Ej. a través de la URL base del Servidor MCP
    (/v1/mcp, /v2/mcp), o mediante cabeceras\].

## **3. Definición de Herramientas (Métodos) del Servidor MCP**

Para cada herramienta expuesta por el Servidor MCP:

**Herramienta: \[nombreModulo.accionVerbo\]**

- **3.X.1. Descripción:**

  - ¿Qué hace esta herramienta? ¿Cuál es su propósito funcional?

  - Referencia a los Requisitos Funcionales (RF) en MAIDO-TPL-03 que
    esta herramienta ayuda a implementar.

- **3.X.2. Endpoint (si no es puramente JSON-RPC por método):**

  - \[Ej. /rpc y el método se especifica en el payload JSON-RPC. Si
    fuera REST, sería /modulo/recurso\].

- **3.X.3. Método HTTP (si es REST):**

  - \[Ej. POST, GET, PUT, DELETE\]. *Para JSON-RPC, usualmente siempre
    es POST.*

- **3.X.4. Parámetros de Entrada (Request Payload):**

  - Describir la estructura del objeto de parámetros esperado.

  - Para cada parámetro:

    - **Nombre:** (camelCase recomendado para el JSON).

    - **Tipo de Dato:** (Ej. string, number, boolean, array, object,
      UUID).

    - **¿Obligatorio?:** (Sí/No).

    - **Descripción:** ¿Qué representa este parámetro?

    - **Validaciones/Restricciones:** (Ej. longitud máxima, formato
      específico, rango de valores).

  - **Ejemplo de Payload (JSON):**  
    {  
    "parametroUno": "valorEjemplo",  
    "parametroDosOpcional": 123  
    }

- **3.X.5. Respuesta Exitosa (Response Payload - result en JSON-RPC):**

  - Describir la estructura del objeto de resultado esperado en caso de
    éxito.

  - Para cada propiedad:

    - **Nombre:** (camelCase recomendado).

    - **Tipo de Dato:**

    - **Descripción:**

  - **Ejemplo de Payload de Respuesta Exitosa (JSON, contenido del
    result):**  
    {  
    "idCreado": "uuid-generado-aqui",  
    "mensajeConfirmacion": "Operación realizada con éxito."  
    }

  - **(Crucial para herramientas que devuelven listas o estructuras
    complejas):** Incluir un **JSON de ejemplo validado o un Esquema
    JSON** que represente la respuesta exacta.

- **3.X.6. Respuestas de Error Específicas de la Herramienta:**

  - Listar los errorCodeInternal específicos que esta herramienta podría
    devolver, además de los errores estándar.

  - ¿En qué condiciones se devuelven?

- **3.X.7. Consideraciones de Seguridad/Permisos:**

  - ¿Requiere un rol de usuario específico para ser invocada?

  - ¿Hay alguna política RLS de Supabase particularmente relevante para
    esta herramienta?

- **3.X.8. Lógica de Consumo de Créditos (si aplica, para proyectos con
  monetización basada en créditos):**

  - ¿Esta herramienta consume "Créditos de Claridad" (o la moneda del
    proyecto)?

  - ¿Cómo se calcula el consumo? (Ej. fijo por llamada, basado en
    parámetros, basado en la respuesta del LLM).

  - ¿Qué sucede si el usuario no tiene suficientes créditos? (Devolver
    un error MCP específico).

**(Repetir la estructura anterior para cada Herramienta MCP del
proyecto)**

**Ejemplo de Nombres de Herramientas (adaptar al proyecto):**

- auth.login

- auth.register

- authProfile.getProfile

- authProfile.updateProfile

- workItems.create

- workItems.get

- workItems.list

- workItems.update

- workItems.delete

- workItems.updateStatus

- agendaEvents.create

- agendaEvents.list

- zerebroMemory.addEco

- zerebroMemory.query

- domainPreferences.list

- domainPreferences.update

- aiAgent.invoke\[NombreAgente\]

- projectLog.addEntryToMAIDO62x (Herramienta MCP para actualizar el log
  de feedback)

- githubAccess.updateFileContent (Herramienta MCP para interactuar con
  GitHub)

- githubAccess.createPullRequest

- githubAccess.initiateMicrotaskPR

## **Anexo A: Códigos de Error Internos Estandarizados (errorCodeInternal)**

- AUTH_INVALID_CREDENTIALS: Credenciales de inicio de sesión
  incorrectas.

- AUTH_USER_NOT_FOUND: Usuario no encontrado.

- AUTH_EMAIL_ALREADY_EXISTS: El correo electrónico ya está registrado.

- AUTH_UNAUTHORIZED: El usuario no tiene permisos para esta acción.

- VALIDATION_ERROR: Error en la validación de los parámetros de entrada.

- RESOURCE_NOT_FOUND: El recurso solicitado no existe (ej. un work_item
  específico).

- INSUFFICIENT_CREDITS: El usuario no tiene suficientes créditos para
  realizar la acción.

- EXTERNAL_API_ERROR: Error al comunicarse con una API externa (ej.
  LLM).

- GITHUB_API_ERROR: Error al comunicarse con la API de GitHub.

- SERVER_UNEXPECTED_ERROR: Error interno inesperado en el servidor.

- \[Otros_Codigos_Especificos_del_Proyecto\]

## **Anexo B: Tipos de Datos Comunes y Estructuras (Data Transfer Objects - DTOs)**

- Definir aquí las estructuras de objetos JSON que se reutilizan
  frecuentemente en los parámetros de entrada o en las respuestas de las
  herramientas MCP.

- **Ejemplo DTO WorkItemInput:**  
  {  
  "titulo": "string (obligatorio)",  
  "descripcion": "string (opcional)",  
  "itemType": "string (obligatorio, Enum: \['reto', 'mision', ...\])",  
  // ... otros campos comunes para la creación/actualización de work
  items  
  }

- **Ejemplo DTO WorkItemOutput:**  
  {  
  "id": "UUID",  
  "titulo": "string",  
  "descripcion": "string \| null",  
  "itemType": "string",  
  "status": "string",  
  "createdAt": "string (ISO 8601 datetime)",  
  "updatedAt": "string (ISO 8601 datetime)",  
  // ... otros campos  
  }

## **6. Historial de Versiones de este Documento**

- **v1.0 (\[Fecha\]):** Creación inicial.

- **vX.Y (\[Fecha\]):** \[Breve descripción del cambio\].
