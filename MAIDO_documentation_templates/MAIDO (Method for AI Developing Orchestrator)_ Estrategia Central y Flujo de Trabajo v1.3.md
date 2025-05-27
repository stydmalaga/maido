# **MAIDO (Method for AI Developing Orchestrator): Estrategia Central y Flujo de Trabajo v1.3**

Versión: 1.3

Fecha: 27 de Mayo de 2025

Estado: Consolidado

## **1. Introducción a MAIDO**

### **1.1. Propósito y Visión de MAIDO**

MAIDO (Method for AI Developing Orchestrator) es una metodología
diseñada para el desarrollo ágil y eficiente de proyectos de software,
con un énfasis particular en aquellos que integran profundamente la
Inteligencia Artificial (IA) a lo largo de su ciclo de vida. El núcleo
de MAIDO es la colaboración estratégica entre un **Product Visionary**
(humano) y un **AI Orchestrator** (en adelante, "el orquestador", una IA
conversacional avanzada como Gemini), que asiste y prepara tareas de
desarrollo.

El objetivo principal de MAIDO es:

- Incrementar la agilidad y la velocidad de desarrollo.

- Mejorar la calidad del software y la documentación.

- Optimizar la carga de trabajo del Product Visionary, permitiéndole
  enfocarse en la visión estratégica y la supervisión.

- Fomentar un proceso de desarrollo iterativo, adaptable y basado en el
  aprendizaje continuo.

### **1.2. Filosofía y Principios Clave**

MAIDO se sustenta en los siguientes principios:

1.  **Colaboración Humano-IA Estratégica:**

    - El Product Visionary define la visión, los objetivos de alto nivel
      y las prioridades del proyecto. Supervisa el progreso, aprueba las
      propuestas clave del orquestador y realiza la validación final
      (especialmente estética y de experiencia de usuario).

    - El orquestador IA interpreta los requisitos, procesa información,
      prepara "Paquetes de Tarea Inteligente" para la codificación (o
      genera directamente contenido/código para tareas simples), y
      gestiona proactivamente el ciclo de vida de la documentación.

2.  **"Docs-as-Code" como Fuente Única de Verdad:**

    - Toda la documentación maestra del proyecto (visión, arquitectura,
      especificaciones, planes, logs de aprendizaje) y el código fuente
      residen en un repositorio Git.

    - Esto asegura versionado granular, trazabilidad completa de
      cambios, y coherencia.

3.  **Automatización Extensiva del Ciclo de Vida:**

    - Se prioriza la automatización de builds, pruebas (unitarias,
      integración, E2E, análisis estático, regresión visual),
      despliegues y la generación de entornos de previsualización.

    - Se utilizan herramientas de Integración Continua y Despliegue
      Continuo (CI/CD).

4.  **Desarrollo Basado en Microtareas y Pull Requests (PRs):**

    - El trabajo se descompone en microtareas manejables, definidas en
      un Plan de Desarrollo Incremental específico del proyecto.

    - Cada cambio significativo (código o documentación) se integra a
      través de una Pull Request (PR), que sirve como punto central para
      la revisión automatizada y la aprobación del Product Visionary.

5.  **Feedback Continuo y Estructurado:**

    - Un "Log de Cambios y Aprendizajes Estructurado" (documento
      MAIDO-6.2.x específico del proyecto) captura de forma detallada el
      feedback de cada microtarea, las decisiones de implementación y
      los aprendizajes.

    - Este log es una fuente de información crucial para el orquestador
      y para la mejora continua del proceso y del propio método MAIDO.

6.  **Iteración Rápida y Adaptabilidad:**

    - MAIDO está diseñado para ser flexible, permitiendo la adaptación
      del método a las necesidades específicas de cada proyecto y la
      incorporación de mejoras basadas en la experiencia.

## **2. Componentes del Ecosistema MAIDO**

MAIDO opera con un conjunto de roles y herramientas interconectadas,
aplicables a cualquier proyecto que adopte esta metodología.

### **2.1. Roles Fundamentales**

- **Product Visionary (Humano):**

  - Responsabilidades: Define la visión del producto, establece
    prioridades estratégicas, aprueba las propuestas del orquestador,
    ejecuta functionCalls MCP (si es necesario), realiza la revisión
    estética/UX en Previews de Despliegue, y efectúa el merge final de
    PRs.

  - Interacción: Principalmente con el orquestador IA y la interfaz de
    GitHub (para revisión de PRs).

- **El Orquestador (IA Conversacional Avanzada, ej. Gemini en su
  interfaz de chat):**

  - Responsabilidades:

    - Interpretar directrices del Product Visionary para un proyecto
      específico.

    - Consultar el Log de Cambios (MAIDO-6.2.x del proyecto) y los
      Documentos Maestros del proyecto en Git para mantener contexto y
      realizar "pre-flight checks".

    - Considerar dependencias entre microtareas del Plan de Desarrollo
      del proyecto.

    - Utilizar **"Plantillas de Microtarea MAIDO"** (ver Anexo A) para
      tareas comunes, solicitando solo parámetros variables al Product
      Visionary.

    - Generar "Paquetes de Tarea Inteligente" para un LLM de
      codificación (o para sí mismo si la tarea es simple),
      referenciando el sistema de diseño/biblioteca de componentes del
      proyecto para tareas de UI.

    - Generar functionCalls JSON (peticiones MCP) para la interacción
      con el Servidor MCP.

    - Realizar **auto-revisión ("Revisión de Sanity")** de sus
      propuestas antes de presentarlas al Product Visionary.

    - Detectar el impacto de los aprendizajes del MAIDO-6.2.x del
      proyecto en los Documentos Maestros del proyecto.

    - Proponer y preparar "Lotes de Actualización Documental" para el
      proyecto.

- **(Opcional) LLM de Codificación Dedicado:**

  - Una instancia de LLM (puede ser el mismo orquestador u otro
    especializado) que recibe los "Paquetes de Tarea Inteligente" y
    genera el código fuente para el proyecto.

- **(Opcional) Asistente IA de Consulta Documental Dedicado:**

  - Una instancia de IA (ej. un nuevo chat de Gemini) a la que el
    Product Visionary puede recurrir para consultas específicas sobre la
    metodología MAIDO o la documentación del proyecto.

  - El Product Visionary proporciona el contexto necesario (Documento
    Central de MAIDO, documentos relevantes del proyecto) a esta
    instancia para obtener respuestas y guía, manteniendo al orquestador
    principal enfocado en las microtareas.

- **(Opcional) Asistente IA de Análisis de Métricas Dedicado:**

  - Una instancia de IA que el Product Visionary puede usar
    periódicamente para analizar el MAIDO-6.2.x del proyecto y generar
    informes sobre la "Salud del Proceso MAIDO" (métricas de eficiencia,
    patrones, etc.).

### **2.2. Herramientas y Plataformas Esenciales**

- **Repositorio Git (ej. GitHub).**

- **Plataforma de CI/CD (ej. GitHub Actions).**

- **Plataforma de Despliegue Frontend (ej. Cloudflare Pages plan
  gratuito, Netlify Plan Pro, Vercel):** *Se recomienda un plan que
  ofrezca un volumen de builds generoso (ej. 500 builds/mes de
  Cloudflare Pages gratuito o 25,000 minutos/mes de Netlify Pro) para no
  frenar el desarrollo ágil.*

- **Plataforma Backend (ej. Supabase, Firebase, o backend propio):** Con
  capacidad para crear entornos de prueba aislados por PR.

- **Servidor MCP (Model Context Protocol):**

  - Implementación propia del Product Visionary.

  - Recibe functionCalls JSON.

  - Ejecuta acciones en sistemas externos (API de GitHub).

  - **Principio de Diseño:** Desarrollar herramientas MCP de alto nivel
    que encapsulen secuencias de operaciones comunes para simplificar
    las functionCalls del orquestador.

- **Herramienta Cliente HTTP para Ejecutar functionCalls MCP:**

  - **Opción Básica:** Postman o un script simple (Python, Node.js,
    shell) utilizado por el Product Visionary.

  - **Opción Optimizada:** Una **Interfaz Web Simplificada**
    (desplegable como página estática) donde el Product Visionary pega
    el JSON de la functionCall, y la interfaz gestiona el envío al
    Servidor MCP.

- **Log de Cambios y Aprendizajes Estructurado (Archivo MAIDO-6.2.x por
  proyecto).**

- **(Recomendado) Sistema de Diseño y Biblioteca de Componentes UI:**
  Específico del proyecto, documentado (ej. con Storybook) y
  referenciado por el orquestador.

### **2.3. Continuidad y Sincronización del Orquestador**

- **Fuente Única de Verdad en Git:** La documentación maestra del
  proyecto en Git es el estado persistente.

- **Guía de Continuidad del Orquestador Específica del Proyecto
  (MAIDO-TPL-00):** Cada proyecto mantiene este documento con
  enlaces/rutas a los artefactos clave en Git (Plan de Desarrollo,
  MAIDO-6.2.x, etc.) para que el orquestador pueda "resincronizarse" en
  una nueva sesión de chat.

- **Responsabilidad del Orquestador:** Poder procesar estos documentos
  de contexto para continuar desde el último punto.

## **3. Flujo de Trabajo General de MAIDO para una Microtarea**

### **3.1. Definición de la Microtarea**

- El Product Visionary selecciona una microtarea del "Plan de Desarrollo
  Incremental" del proyecto, e instruye al orquestador.

- El orquestador considera las dependencias de esta tarea con otras,
  según el Plan de Desarrollo.

### **3.2. Preparación por el Orquestador**

- Consulta el Log de Cambios (MAIDO-6.2.x del proyecto) y los Documentos
  Maestros relevantes del proyecto en GitHub.

- Realiza **"pre-flight checks"** internos para asegurar la relevancia y
  evitar la duplicación de propuestas o el uso de información obsoleta.

- Para tareas comunes, puede utilizar **"Plantillas de Microtarea
  MAIDO"** predefinidas (ver Anexo A), solicitando al Product Visionary
  solo los parámetros variables para acelerar la preparación.

- Al generar "Paquetes de Tarea Inteligente" para UI, referencia
  componentes y estilos del **Sistema de Diseño/Biblioteca de
  Componentes** del proyecto.

- **Auto-Revisión ("Revisión de Sanity"):** Antes de presentar la
  propuesta al Product Visionary, el orquestador realiza una
  auto-revisión de la completitud, claridad y corrección de su "Paquete
  de Tarea Inteligente" o functionCall MCP.

- Genera una propuesta para el Product Visionary:

  - **Opción A (Tarea de Codificación):** Un "Paquete de Tarea
    Inteligente".

  - **Opción B (Actualización Directa):** El contenido del archivo a
    modificar y la functionCall JSON (petición MCP).

### **3.3. Revisión y Aprobación por el Product Visionary**

- Revisa la propuesta del orquestador (sanity check). Aprueba para
  proceder.

### **3.4. Ejecución de la Tarea**

- **Opción A (Codificación):**

  1.  (Opcional pero Recomendado) El orquestador puede generar una
      functionCall MCP para una herramienta del Servidor MCP (ej.
      githubAccess.initiateMicrotaskPR) que cree la rama y una PR
      inicial (con un placeholder o el prompt). El Product Visionary
      ejecuta esta functionCall.

  2.  El Product Visionary (o un script bajo su control) pasa el
      "Paquete de Tarea" al LLM de Codificación.

  3.  El código resultante es integrado (commiteado y pusheado) por el
      Product Visionary (o un script) a la rama creada en el paso
      anterior (o una nueva si el paso 1 no se realizó). Si no se creó
      una PR en el paso 1, se crea ahora.

- **Opción B (Actualización Directa):** El Product Visionary ejecuta la
  functionCall MCP (vía la **Interfaz Web Simplificada** o
  Postman/script) al Servidor MCP. El Servidor MCP crea una nueva rama,
  aplica los cambios al archivo en GitHub y crea una PR automáticamente.

### **3.5. Revisión de Pull Request (PR) en GitHub**

- **Revisión Automatizada (vía GitHub Actions):** Pruebas y análisis se
  ejecutan y reportan en la PR.

- **Revisión Asistida por IA (Opcional pero Recomendada):**

  - El Product Visionary puede instruir al orquestador para que realice
    una pre-revisión del "diff" de la PR contra los objetivos de la
    microtarea.

  - El orquestador puede proporcionar un resumen, señalar desviaciones o
    áreas que requieran atención especial.

- **Revisión Manual-Estratégica por el Product Visionary:**

  - Verifica resultados de pruebas automatizadas y el resumen de la
    revisión asistida por IA.

  - Interactúa con la "Preview de Despliegue" (considerando el **Sistema
    de Diseño** para la consistencia de la UI).

  - Revisa concisamente el "diff".

### **3.6. Merge de la PR**

- Product Visionary fusiona la PR.

### **3.7. Registro de Feedback Estructurado en MAIDO-6.2.x**

- Se genera un borrador de entrada para el MAIDO-6.2.x del proyecto (por
  el LLM de codificación o Servidor MCP).

- **Flujo Optimizado:** El Servidor MCP podría **directamente crear una
  PR separada con la actualización del MAIDO-6.2.x**.

- El Product Visionary revisa y aprueba/fusiona esta PR del log, o (si
  el flujo anterior no está implementado) aprueba el borrador del
  orquestador y ejecuta la functionCall MCP para actualizar el log.

## **4. Gestión de la Documentación Maestra con MAIDO ("Docs-as-Code")**

*(Sin cambios significativos en los sub-apartados 4.1 a 4.4 respecto a
versiones anteriores, se enfatiza que el "Lote de Actualización
Documental" debe ser manejado por herramientas MCP de alto nivel si es
posible).*

## **5. Configuración del Pipeline de CI/CD y Pruebas Automatizadas en MAIDO**

*(Sin cambios significativos en los sub-apartados 5.1 a 5.3 respecto a
versiones anteriores).*

## **6. Adaptación, Instanciación y Mejora Continua de MAIDO**

### **6.1. "Instanciación" de MAIDO para un Nuevo Proyecto**

*(Sin cambios).*

### **6.2. Documento de Adaptación de MAIDO Específico del Proyecto**

*(Sin cambios).*

### **6.3. Configuración del Orquestador IA para el Proyecto**

*(Sin cambios).*

### **6.4. Desarrollo/Adaptación del Servidor MCP para el Proyecto**

*(Incluye la optimización continua de herramientas MCP de más alto
nivel).*

### **6.5. Monitorización y Mejora del Proceso MAIDO**

- **Análisis Periódico de Métricas:** Utilizar un "Asistente IA de
  Análisis de Métricas Dedicado" (ver 2.1) para procesar el MAIDO-6.2.x
  del proyecto y generar informes sobre la eficiencia del proceso.

- **Sesiones de Retrospectiva (Opcional):** El Product Visionary puede
  usar estos informes para reflexionar sobre la aplicación de MAIDO en
  el proyecto.

- **Propuestas de Mejora Proactiva del Orquestador:** El orquestador
  principal puede ser instruido para, al detectar patrones recurrentes
  en el MAIDO-6.2.x, sugerir mejoras al proceso MAIDO aplicado al
  proyecto, a la documentación, o a componentes reutilizables.

## **Anexo A: Plantillas de Documentos Clave Sugeridas por MAIDO (Ejemplos)**

- MAIDO-TPL-00-Guia_Continuidad_Orquestador_Proyecto.md

- MAIDO-TPL-01-Vision_Alcance_Proyecto.md

- MAIDO-TPL-02-Identidad_Lore_UX_Proyecto.md

- MAIDO-TPL-03-Especificaciones_Funcionales_Proyecto.md

- MAIDO-TPL-04-Arquitectura_Tecnica_Proyecto.md

- MAIDO-TPL-05-Contrato_API_MCP_Proyecto.md

- MAIDO-TPL-06-Plan_Desarrollo_Incremental_Proyecto.md *(Enfatizar la
  necesidad de definir dependencias entre tareas y la posibilidad de
  usar "Plantillas de Microtarea MAIDO" para tipos comunes).*

- MAIDO-TPL-07-Estrategia_Monetizacion_Proyecto.md

- MAIDO-TPL-08-Nomenclaturas_Convenciones_Proyecto.md

- MAIDO-TPL-09-Sistema_Diseño_UI_Componentes_Proyecto.md

- MAIDO-STRUCT-6.2.x-Log_Cambios_Aprendizajes_Proyecto.md (Define la
  estructura JSON/YAML)

- MAIDO-TPL-MT-Plantilla_Microtarea_CRUD_Completo.md (Ejemplo de
  Plantilla de Microtarea)

## **Anexo B: Ejemplos de functionCall JSON para Interacciones Comunes con el Servidor MCP**

- Ejemplo para githubAccess.updateFileContent (incluye ruta, nuevo
  contenido, mensaje de commit, rama).

- Ejemplo para githubAccess.createPullRequest (incluye rama origen, rama
  destino, título, cuerpo).

- Ejemplo para githubAccess.initiateMicrotaskPR (incluye nombre de rama
  sugerido, título de PR, cuerpo de PR con referencia a la microtarea).

- Ejemplo para projectLog.addEntryToMAIDO62x (incluye el payload
  estructurado del feedback).
