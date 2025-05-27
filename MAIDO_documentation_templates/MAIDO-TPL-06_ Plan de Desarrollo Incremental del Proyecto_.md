# **MAIDO-TPL-06: Plan de Desarrollo Incremental del Proyecto - \[Nombre_del_Proyecto\]**

Versión: 1.0

Fecha: \[Fecha_Creacion_o_Ultima_Modificacion\]

Estado: Borrador / En Progreso / Consolidado

Proyecto: \[Nombre_del_Proyecto\]

ID del Proyecto (si aplica): \[ID_Proyecto\]

## **1. Propósito de este Documento**

- Desglosar el desarrollo del proyecto "\[Nombre_del_Proyecto\]" (o una
  fase/MVP específico del mismo) en fases, subfases y microtareas
  manejables.

- Servir como la hoja de ruta principal para el Product Visionary y el
  orquestador IA en la selección y preparación de las próximas
  microtareas a desarrollar.

- Facilitar el seguimiento del progreso y la gestión de dependencias
  entre tareas.

- Asegurar que cada microtarea contribuya de manera incremental a los
  objetivos definidos en la "Visión y Alcance del Proyecto"
  (MAIDO-TPL-01) y las "Especificaciones Funcionales" (MAIDO-TPL-03).

- Este documento es vivo y se actualizará continuamente a medida que se
  completen tareas, se identifiquen nuevas o cambien las prioridades.

## **2. Documentos de Referencia Principales (Específicos del Proyecto)**

- \[Nombre_Doc_Vision_Alcance_Proyecto\].md (Basado en MAIDO-TPL-01)

- \[Nombre_Doc_Especificaciones_Funcionales_Proyecto\].md (Basado en
  MAIDO-TPL-03)

- \[Nombre_Doc_Arquitectura_Tecnica_Proyecto\].md (Basado en
  MAIDO-TPL-04)

- (Otros documentos relevantes del proyecto)

## **3. Nomenclatura de IDs de Microtareas (Sugerencia MAIDO)**

MAIDO sugiere un formato para los IDs de microtareas para facilitar su
seguimiento y referencia. Esta nomenclatura puede adaptarse a las
necesidades del proyecto.

- **Formato Sugerido:**
  \[FASE_PROYECTO\]-\[MODULO_o_SUBFASE\]-\[TIPO\]\[NUMERO_SECUENCIAL\]

  - **\[FASE_PROYECTO\]:** Identificador de la fase principal del
    proyecto (ej. MVP1, V2_0, P0, P1).

  - **\[MODULO_o_SUBFASE\]:** Identificador corto del módulo funcional
    principal (ej. AUTH para autenticación, WI para Work Items, AGENDA,
    ZEREBRO) o una subfase lógica.

  - **\[TIPO\]:** Indica la naturaleza de la tarea:

    - F: Frontend

    - B: Backend

    - BF: Implica tanto Frontend como Backend

    - D: Documentación, Definición o Investigación

    - T: Pruebas (si se definen como microtareas separadas)

    - C: Configuración o Infraestructura

  - **\[NUMERO_SECUENCIAL\]:** Un número secuencial para la tarea dentro
    de su categoría. Se pueden usar sufijos como X para tareas
    identificadas pero pendientes de secuenciación exacta o detalle
    completo.

- **Ejemplo (para un proyecto hipotético):** MVP1-AUTH-F001,
  MVP1-WI-B003, V2_FEATURE_X-BF001

## **4. Plan de Desarrollo por Fases y Microtareas**

**(Esta es la sección principal del documento y se rellenará
iterativamente)**

**Fase: \[Nombre_o_Numero_de_la_Fase_Principal_1\]**

- **Objetivo de la Fase:** \[Describir brevemente qué se espera lograr
  al completar esta fase\]

- **Duración Estimada (Opcional):** \[Ej. 2 semanas, 1 mes\]  
  **Subfase/Módulo: \[Nombre_del_Modulo_o_Subfase_1.1\]**

  - **Microtarea: \[ID_Microtarea_1.1.1\]**

    - **Título Descriptivo:** \[Título claro y conciso de la
      microtarea\]

    - **Objetivo Principal:** \[Qué se logrará con esta microtarea
      específica\]

    - **Descripción Breve/Alcance:** \[Detalles adicionales si son
      necesarios para entender la tarea a alto nivel\]

    - **Dependencias (IDs de otras microtareas):** \[Ej. MVP1-AUTH-B001,
      MVP1-WI-F002\] *(Crucial para el orquestador)*

    - **Prioridad:** (Ej. Muy Alta, Alta, Media, Baja)

    - **Estimación de Esfuerzo (Opcional):** (Ej. Pequeña, Mediana,
      Grande; o Puntos de Historia)

    - **Responsable (si aplica en equipos más grandes):** \[Product
      Visionary para definición, luego el sistema automatizado/LLM para
      ejecución\]

    - **Documentos de Referencia Específicos:** (Además de los
      generales, ej. una sección particular del MAIDO-TPL-03 o
      MAIDO-TPL-04)

    - **Criterios de Aceptación de Alto Nivel:** (¿Cómo sabremos que
      esta microtarea está "hecha" desde una perspectiva funcional?)

    - **Estado:** (PENDIENTE, EN_PROGRESO_DEFINICION,
      LISTA_PARA_EJECUCION, EN_EJECUCION, EN_REVISION_PR, COMPLETADA,
      BLOQUEADA, CANCELADA)

    - **Fecha de Última Actualización del Estado:** \[Fecha\]

    - **Enlace a PR (cuando aplique):** \[Enlace_a_GitHub_PR\]

    - **Notas/Comentarios Adicionales:**

  - **Microtarea: \[ID_Microtarea_1.1.2\]**

    - ... (repetir estructura)

> **Subfase/Módulo: \[Nombre_del_Modulo_o_Subfase_1.2\]**

- **Microtarea: \[ID_Microtarea_1.2.1\]**

  - ... (repetir estructura)

**Fase: \[Nombre_o_Numero_de_la_Fase_Principal_2\]**

- **Objetivo de la Fase:** ...  
  **Subfase/Módulo: \[Nombre_del_Modulo_o_Subfase_2.1\]**

  - **Microtarea: \[ID_Microtarea_2.1.1\]**

    - ... (repetir estructura)

**(Continuar con todas las fases y microtareas planificadas para el
alcance actual del proyecto o MVP)**

## **5. Backlog de Microtareas (Tareas Identificadas pero No Priorizadas/Secuenciadas)**

- Listar aquí microtareas que se han identificado como necesarias o
  deseables pero que aún no tienen una prioridad o secuencia definida
  dentro de las fases actuales.

  - **Microtarea: \[ID_Microtarea_BACKLOG_X001\]**

    - **Título Descriptivo:**

    - **Descripción Breve:**

    - **Notas:**

## **6. Consideraciones para la Planificación y Priorización**

- ¿Cómo se decidirá la prioridad de las microtareas?

- ¿Con qué frecuencia se revisará y actualizará este plan?

- ¿Cómo se manejarán los cambios de alcance o las nuevas tareas
  identificadas?

## **7. Historial de Versiones de este Documento**

- **v1.0 (\[Fecha\]):** Creación inicial con las primeras fases del
  \[MVP/Versión_Inicial\].

- **vX.Y (\[Fecha\]):** \[Breve descripción del cambio, ej. "Añadidas
  microtareas para Fase 3", "Actualizado estado de tareas de Fase 1",
  "Repriorizadas tareas del backlog"\].
