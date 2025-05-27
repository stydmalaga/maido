# **MAIDO-TPL-08: Nomenclaturas y Convenciones del Proyecto - \[Nombre_del_Proyecto\]**

Versión: 1.0

Fecha: \[Fecha_Creacion_o_Ultima_Modificacion\]

Estado: Borrador / Consolidado

Proyecto: \[Nombre_del_Proyecto\]

ID del Proyecto (si aplica): \[ID_Proyecto\]

## **1. Propósito de este Documento**

- Establecer un conjunto de nomenclaturas y convenciones de
  codificación, diseño y documentación para el proyecto
  "\[Nombre_del_Proyecto\]".

- Asegurar la consistencia, legibilidad y mantenibilidad del código
  fuente, la documentación, los artefactos de diseño y la comunicación
  dentro del equipo (Product Visionary, orquestador IA, LLM de
  codificación).

- Reducir la ambigüedad y facilitar la integración de diferentes partes
  del sistema.

- Este documento debe ser consultado y seguido por todos los
  involucrados en el desarrollo del proyecto.

## **2. Alcance**

Estas nomenclaturas y convenciones se aplican a:

- Código fuente (frontend, backend, scripts).

- Nombres de archivos y directorios.

- Nombres de variables, funciones, clases, componentes, módulos.

- Nombres de tablas y columnas de la base de datos.

- Endpoints de API y parámetros/propiedades de payloads MCP/JSON.

- Mensajes de commit en Git.

- Nombres de ramas en Git.

- Documentación técnica y de usuario.

- Terminología específica del proyecto (referenciar MAIDO-TPL-02 si
  aplica para el lore).

## **3. Convenciones Generales de Nomenclatura**

- **3.1. Idioma Principal:**

  - \[Ej. Inglés para código, nombres de archivos, base de datos, API.
    Español para documentación de usuario y comentarios si se
    prefiere\]. *MAIDO recomienda usar inglés para todos los artefactos
    de código y técnicos para mayor universalidad y compatibilidad con
    herramientas, y el idioma del Product Visionary para la
    documentación de alto nivel y comentarios si facilita la
    comprensión.*

- **3.2. Estilos de Capitalización (Case Styles):**

  - **camelCase:** \[Ej. nombreDeVariable, funcionPrincipal\]. Usado
    para \[Ej. variables, nombres de funciones en JavaScript/TypeScript,
    propiedades JSON en payloads MCP/API\].

  - **PascalCase (o UpperCamelCase):** \[Ej. NombreDeClase,
    ComponenteReact\]. Usado para \[Ej. nombres de clases, nombres de
    componentes React/Vue/Angular, tipos e interfaces en TypeScript\].

  - **snake_case:** \[Ej. nombre_de_columna_db, variable_entorno\].
    Usado para \[Ej. nombres de tablas y columnas en bases de datos
    PostgreSQL/MySQL, variables de entorno, a veces nombres de
    archivos\].

  - **kebab-case:** \[Ej. nombre-de-archivo.css, clase-css-principal\].
    Usado para \[Ej. nombres de archivos (especialmente CSS, HTML,
    Markdown), clases CSS, URLs amigables\].

  - **UPPER_CASE_SNAKE_CASE (o SCREAMING_SNAKE_CASE):** \[Ej.
    CONSTANTE_GLOBAL, TIPO_DE_ACCION_REDUX\]. Usado para \[Ej.
    constantes globales, tipos de acciones en Redux/Zustand, valores de
    enums en algunos lenguajes\].

- **3.3. Claridad y Descriptividad:**

  - Los nombres deben ser lo suficientemente descriptivos para entender
    su propósito sin necesidad de buscar su definición.

  - Evitar abreviaturas excesivas o ambiguas.

  - Preferir la legibilidad sobre la brevedad extrema.

- **3.4. Consistencia:**

  - Una vez elegida una convención para un tipo de artefacto, mantenerla
    consistentemente en todo el proyecto.

## **4. Convenciones Específicas por Tipo de Artefacto**

- **4.1. Nombres de Archivos y Directorios:**

  - Estilo: \[Ej. kebab-case.extension para archivos, kebab-case o
    snake_case para directorios\].

  - Convención para componentes (si aplica): \[Ej. NombreComponente.tsx
    (PascalCase) o nombre-componente.tsx (kebab-case)\].

  - Convención para archivos de utilidades, servicios, etc.

- **4.2. Variables:**

  - Estilo: \[Ej. camelCase\].

  - Prefijos/Sufijos (si aplica): \[Ej. is o has para booleanos
    (isValid, hasPermission), \_ para variables privadas en clases
    (convención)\].

- **4.3. Funciones/Métodos:**

  - Estilo: \[Ej. camelCase\].

  - Verbos de Acción: Usar verbos que describan la acción (ej.
    getUserData(), calculateTotalPrice(), handleSubmit()).

- **4.4. Clases/Interfaces/Tipos:**

  - Estilo: \[Ej. PascalCase\].

  - Sufijos (si aplica): \[Ej. Interface o Type para tipos
    (UserDataInterface, UserProfileType), Service para clases de
    servicio (AuthService)\].

- **4.5. Componentes UI (React, Vue, Angular, etc.):**

  - Estilo de Nombre de Componente: \[Ej. PascalCase\].

  - Estilo de Nombre de Archivo del Componente: \[Ej.
    NombreComponente.tsx\].

  - Estructura de directorios para componentes.

- **4.6. Base de Datos (Tablas y Columnas):**

  - Estilo para Nombres de Tablas: \[Ej. snake_case, plural (users,
    work_items)\].

  - Estilo para Nombres de Columnas: \[Ej. snake_case (user_id,
    created_at)\].

  - Claves Primarias: \[Ej. id (UUID o serial)\].

  - Claves Foráneas: \[Ej. \[tabla_referenciada_singular\]\_id (ej.
    user_id en la tabla work_items que referencia a users.id)\].

- **4.7. Endpoints API / Herramientas MCP:**

  - Estilo para Nombres de Herramientas MCP: \[Ej.
    nombreModulo.accionVerbo (ej. authProfile.getProfile)\].

  - Estilo para Parámetros y Propiedades JSON en Payloads: \[Ej.
    camelCase\].

  - (Si es RESTful) Estilo para Rutas URL: \[Ej. kebab-case, plural para
    colecciones (/api/v1/work-items)\].

- **4.8. Mensajes de Commit en Git:**

  - Formato: \[Ej. Seguir el estándar de Conventional Commits
    (\<tipo\>(\<alcance\>): \<descripción\>)\].

    - Tipos comunes: feat (nueva funcionalidad), fix (corrección de
      bug), docs (cambios en documentación), style (formato, sin cambios
      de código), refactor, test, chore (mantenimiento).

  - Idioma: \[Ej. Inglés\].

- **4.9. Nombres de Ramas en Git:**

  - Formato: \[Ej. feature/\<nombre-descriptivo-kebab-case\>,
    fix/\<issue-id\>-\<descripcion-kebab-case\>,
    docs/\<tema-kebab-case\>\].

  - Ramas principales: \[Ej. main, develop, staging\].

- **4.10. Clases CSS y Selectores (si no se usa Tailwind CSS u otro
  framework similar que lo abstraiga):**

  - Estilo: \[Ej. kebab-case, metodología BEM
    (block\_\_element--modifier)\].

- **4.11. Variables de Entorno:**

  - Estilo: \[Ej. UPPER_CASE_SNAKE_CASE (DATABASE_URL,
    API_KEY_SERVICIO_EXTERNO)\].

## **5. Convenciones de Codificación (Específicas del Lenguaje)**

- **5.1. \[Lenguaje Principal, ej. TypeScript/JavaScript\]:**

  - Referencia a Guías de Estilo Externas: \[Ej. Airbnb JavaScript Style
    Guide, Google TypeScript Style Guide\].

  - Formateo: \[Ej. Uso de Prettier con configuración X, ESLint con
    conjunto de reglas Y\].

  - Comentarios: \[Ej. Estilo JSDoc/TSDoc para funciones públicas y
    clases, comentarios en línea para lógica compleja\].

  - Manejo de Errores: \[Ej. Uso de try...catch, promesas con .catch(),
    tipos de error personalizados\].

  - Organización de Importaciones.

  - Patrones de Diseño Preferidos (si aplica).

  - (Otras convenciones específicas del lenguaje).

- **5.2. \[Otro Lenguaje, ej. Python para scripts o backend si
  aplica\]:**

  - Referencia a Guías de Estilo: \[Ej. PEP 8\].

  - (Otras convenciones).

## **6. Convenciones de Documentación**

- **6.1. Documentos Maestros del Proyecto (basados en plantillas
  MAIDO):**

  - Formato: \[Ej. Markdown\].

  - Estructura de Secciones: Seguir las plantillas MAIDO.

  - Nivel de Detalle.

- **6.2. Comentarios en el Código:**

  - Cuándo y cómo comentar.

- **6.3. Documentación de API/MCP (si no está completamente en
  MAIDO-TPL-05):**

  - Herramientas (ej. Swagger/OpenAPI para REST, o la propia estructura
    del MAIDO-TPL-05 para MCP).

## **7. Herramientas de Soporte para Convenciones**

- **Linters:** \[Ej. ESLint, Stylelint, Pylint\].

- **Formateadores:** \[Ej. Prettier, Black\].

- **Hooks de Git (pre-commit):** \[Ej. Husky con lint-staged para
  ejecutar linters/formateadores antes de cada commit\].

- **Configuraciones Compartidas (ej. .editorconfig, tsconfig.json,
  .eslintrc.js, prettier.config.js).**

## **8. Proceso de Actualización de estas Convenciones**

- ¿Quién puede proponer cambios a estas convenciones?

- ¿Cómo se aprueban y comunican los cambios?

- Este documento es vivo y puede evolucionar.

## **9. Historial de Versiones de este Documento**

- **v1.0 (\[Fecha\]):** Creación inicial.

- **vX.Y (\[Fecha\]):** \[Breve descripción del cambio\].
