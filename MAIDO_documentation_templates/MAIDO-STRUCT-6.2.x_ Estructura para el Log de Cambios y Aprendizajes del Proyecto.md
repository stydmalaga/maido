# **MAIDO-STRUCT-6.2.x: Estructura para el Log de Cambios y Aprendizajes del Proyecto - \[Nombre_del_Proyecto\]**

Versión de la Estructura: 1.0

Fecha: \[Fecha_Creacion_o_Ultima_Modificacion_de_esta_estructura\]

Metodología: MAIDO (Method for AI Developing Orchestrator)

## **1. Propósito de esta Estructura**

- Definir el formato estructurado (preferiblemente JSON o YAML dentro de
  un archivo Markdown o de texto) para cada entrada en el "Log de
  Cambios y Aprendizajes" de un proyecto que utiliza MAIDO.

- Asegurar que el feedback de cada microtarea, las decisiones de
  implementación y los aprendizajes clave se registren de manera
  consistente y detallada.

- Facilitar el procesamiento automatizado o semi-automatizado de este
  log por parte del AI Orquester (el orquestador) para:

  - Mantener su contexto actualizado.

  - Identificar el impacto en los Documentos Maestros del proyecto.

  - Proponer mejoras al proceso o al proyecto.

  - Preparar "Paquetes de Tarea Inteligente" más precisos.

- Esta estructura se utiliza para los archivos que componen el
  MAIDO-6.2.x específico de cada proyecto (ej.
  ProyectoX_Log_Cambios_MVP1.md).

## **2. Formato de Cada Entrada en el Log**

Cada entrada en el log corresponderá a una microtarea completada y
revisada. Se recomienda que cada entrada sea un bloque de texto
claramente delimitado, preferiblemente con una estructura de datos
serializada como YAML o JSON para facilitar el parseo.

**Ejemplo de Estructura de Entrada (formato YAML sugerido):**

\#-----------------------------------------------------------------------  
\# Entrada de Log para Microtarea  
\#-----------------------------------------------------------------------  
- microtarea_id: "\[ID_Unico_de_la_Microtarea_segun_Plan_Desarrollo\]"
\# Ej. MVP1-AUTH-F001  
titulo_microtarea: "\[Titulo_Descriptivo_de_la_Microtarea\]"  
fecha_completitud_product_visionary: "\[AAAA-MM-DD\]" \# Fecha en que el
Product Visionary considera la tarea cerrada tras revisión y merge  
  
\# Sección de Feedback del Implementador (LLM de Codificación o quien
haya ejecutado la tarea)  
feedback_implementador:  
desviaciones_instrucciones_originales: \|  
\[Descripción de cualquier desviación del prompt original y el porqué.  
Si no hubo desviaciones, indicar "Ninguna".\]  
informacion_util_faltante_al_inicio: \|  
\[Qué información (del prompt del orquestador, de los documentos de
contexto,  
o sobre archivos existentes no proporcionados/insuficientes) hubiera
sido útil  
tener desde el principio para agilizar o mejorar la implementación.\]  
aprendizajes_clave_desafios_tecnicos: \|  
\[Principales aprendizajes técnicos, problemas inesperados
encontrados,  
soluciones ingeniosas aplicadas, o desafíos durante la
generación/implementación  
del código/documento.\]  
sugerencias_mejora_futuros_prompts_documentacion: \|  
\[Sugerencias para mejorar futuros prompts del orquestador, la
documentación  
del proyecto, o el propio método MAIDO, basadas en la experiencia de
esta tarea.\]  
  
\# Sección de Decisiones y Resultados de Implementación  
implementacion_detalles:  
decisiones_notables_tomadas: \|  
\[Decisiones de diseño o implementación importantes tomadas por el
implementador  
(y aceptadas por el Product Visionary durante la revisión de PR) que
puedan  
ser relevantes para el futuro. Ej. elección de una librería específica
no  
prescrita, un patrón de diseño particular aplicado.\]  
guia_verificacion_proporcionada_resumen: \|  
\[Resumen breve de la guía de verificación que proporcionó el
implementador,  
o enlace a la sección de la PR donde se detalló. Confirmar si fue
efectiva.\]  
artefactos_creados: \# Lista de nuevos archivos/componentes/tablas
creados  
- tipo: "\[Ej. Frontend Component, Backend Function, DB Table,
Document\]"  
ruta_o_nombre: "\[Ruta/Completa/Al/NuevoArchivo.tsx o NombreDeTabla\]"  
descripcion_breve: "\[Propósito del nuevo artefacto\]"  
\# - ... (más artefactos creados)  
artefactos_modificados_significativamente: \# Lista de artefactos
existentes con cambios importantes  
- tipo: "\[Ej. Frontend Component, Backend Function, DB Table,
Document\]"  
ruta_o_nombre: "\[Ruta/Completa/Al/ArchivoModificado.ts o
NombreDeTabla\]"  
descripcion_cambio: "\[Resumen del cambio principal realizado\]"  
\# - ... (más artefactos modificados)  
versiones_librerias_clave_usadas_asumidas: \|  
\[Si se usaron librerías clave y sus versiones son relevantes o no
estaban  
especificadas en el prompt, listarlas aquí. Ej.
react-router-dom@6.3.0\]  
  
\# Sección de Impacto Documental (a ser evaluado/confirmado por el
Orquestador y Product Visionary)  
impacto_documental_identificado:  
- doc_id_afectado:
"\[ID_o_NombreArchivo_del_Documento_Maestro_Afectado\]" \# Ej.
MAIDO-TPL-05-Contrato_API_MCP_ProyectoX.md  
version_actual_doc: "\[Version_Actual_del_Documento_Maestro\]"  
secciones_afectadas: \|  
\[Listar secciones o puntos específicos del documento que necesitan  
actualización debido a esta microtarea.\]  
cambio_sugerido_resumen: \|  
\[Resumen del cambio que se necesita aplicar al documento maestro.\]  
\# - ... (más documentos afectados)  
  
\# Sección de Seguimiento y Estado (para el Product Visionary y
Orquestador)  
seguimiento_maido:  
pr_principal_asociada:
"\[Enlace_a_la_PR_en_GitHub_donde_se_reviso_e_integro_esta_microtarea\]"  
consolidacion_documental_requerida:
"\[Si/No/Parcialmente_Realizada_en_PR_Log\]" \# ¿Este feedback implica
que algún Doc Maestro necesita ser actualizado formalmente?  
procesado_por_orquestador_para_impacto: "\[Si/No/Pendiente\]" \# ¿El
orquestador ya analizó esta entrada para el próximo ciclo de
consolidación?  
notas_adicionales_product_visionary: \|  
\[Cualquier comentario adicional del Product Visionary sobre esta
microtarea,  
su implementación o el feedback recibido.\]  
\#-----------------------------------------------------------------------

## **3. Guía de Uso**

- **Generación de la Entrada:**

  - Idealmente, el LLM de Codificación o el Servidor MCP (para cambios
    directos) deberían generar un borrador de esta entrada estructurada
    al finalizar su parte de la tarea.

  - El orquestador puede refinar este borrador y presentarlo al Product
    Visionary.

- **Ubicación:**

  - Estas entradas se añadirán secuencialmente a uno o varios archivos
    de log dentro del repositorio Git del proyecto (ej.
    MAIDO-6.2.1-Log_ProyectoX_MVP1.md,
    MAIDO-6.2.2-Log_ProyectoX_MVP2.md).

  - La gestión de estos archivos (ej. crear uno nuevo por fase o por un
    número X de entradas) se definirá en el documento
    \[Nombre_Proyecto\]\_Adaptacion_MAIDO.md.

- **Actualización:**

  - El Product Visionary es responsable final de asegurar que la entrada
    sea correcta y completa antes de que se commitee al log.

  - La actualización del archivo de log en Git se realizará
    preferiblemente a través de una PR dedicada, creada por el Servidor
    MCP tras una functionCall del orquestador (aprobada por el Product
    Visionary).

- **Procesamiento por el Orquestador:**

  - El orquestador utilizará este formato estructurado para parsear
    fácilmente las entradas, extraer aprendizajes, identificar el
    impacto en otros documentos y mantener su contexto sobre el estado
    del proyecto.

## **4. Campos Detallados y su Significado**

- **microtarea_id**: Identificador único de la microtarea según el Plan
  de Desarrollo (MAIDO-TPL-06).

- **titulo_microtarea**: Título descriptivo de la microtarea.

- **fecha_completitud_product_visionary**: Fecha en que el Product
  Visionary considera la tarea cerrada.

- **feedback_implementador**: Contiene las observaciones directas de
  quien ejecutó la tarea.

  - **desviaciones_instrucciones_originales**: Importante para entender
    si el prompt fue claro o si se necesitaron ajustes.

  - **informacion_util_faltante_al_inicio**: Clave para mejorar futuros
    prompts y la completitud del contexto proporcionado.

  - **aprendizajes_clave_desafios_tecnicos**: Captura conocimiento
    técnico valioso y problemas resueltos.

  - **sugerencias_mejora_futuros_prompts_documentacion**: Feedback
    directo para la optimización del proceso MAIDO.

- **implementacion_detalles**: Hechos concretos sobre lo que se entregó.

  - **decisiones_notables_tomadas**: Documenta decisiones que pueden no
    estar en el prompt original pero fueron necesarias.

  - **guia_verificacion_proporcionada_resumen**: Confirma cómo se validó
    la tarea.

  - **artefactos_creados / artefactos_modificados_significativamente**:
    Esencial para el orquestador al preparar el contexto para futuras
    tareas que puedan depender de estos artefactos.

  - **versiones_librerias_clave_usadas_asumidas**: Útil para la gestión
    de dependencias y la reproducibilidad.

- **impacto_documental_identificado**: Lista de Documentos Maestros que
  necesitan ser actualizados. Crucial para el "Ciclo de Consolidación
  Documental".

- **seguimiento_maido**: Metadatos para la gestión del proceso MAIDO.

  - **pr_principal_asociada**: Para trazabilidad.

  - **consolidacion_documental_requerida**: Indicador para el
    orquestador.

  - **procesado_por_orquestador_para_impacto**: Para evitar
    reprocesamiento.

  - **notas_adicionales_product_visionary**: Espacio para el Product
    Visionary.

## **5. Historial de Versiones de esta Estructura**

- **v1.0 (\[Fecha\]):** Creación inicial.
