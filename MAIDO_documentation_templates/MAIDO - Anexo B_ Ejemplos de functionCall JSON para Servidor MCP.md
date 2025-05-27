# **MAIDO - Anexo B: Ejemplos de functionCall JSON para Servidor MCP**

Versión del Anexo: 1.0

Fecha: 27 de Mayo de 2025

Referencia al Documento Central MAIDO: v1.3

## **1. Propósito de este Anexo**

Este anexo proporciona ejemplos concretos de la estructura JSON
(functionCall) que el AI Orquester (el orquestador) generaría para ser
enviada al Servidor MCP de un proyecto. Estos ejemplos ilustran cómo el
orquestador instruye al Servidor MCP para realizar acciones
automatizadas, principalmente relacionadas con la interacción con el
repositorio Git del proyecto (ej. GitHub).

El Product Visionary tomaría este JSON generado por el orquestador y lo
enviaría al endpoint correspondiente del Servidor MCP del proyecto
utilizando una herramienta cliente HTTP (como Postman, un script simple,
o la "Interfaz Web Simplificada" sugerida en MAIDO).

## **2. Formato General de la functionCall (JSON-RPC 2.0 como base)**

Aunque el Model Context Protocol (MCP) puede tener sus propias
especificidades, a menudo se basa o es compatible con JSON-RPC 2.0 para
la estructura de las llamadas a herramientas. El AI Orquester, al
generar una functionCall, produciría un objeto JSON que el Servidor MCP
espera.

La parte crucial que el orquestador genera y que el Servidor MCP
interpreta como la "herramienta a llamar y sus argumentos" podría verse
así (este es el contenido que el Product Visionary copiaría):

{  
"tool_name": "namespace.toolName", // Nombre de la herramienta MCP  
"args": { // Argumentos para la herramienta  
"parametro1": "valor1",  
"parametro2": 123,  
"objetoParametro": {  
"subParam1": true  
}  
}  
}

Este JSON sería típicamente el valor del campo params en una petición
JSON-RPC 2.0 completa, o directamente el cuerpo de una petición POST a
un endpoint RESTful simple de tu Servidor MCP. Para simplificar, los
ejemplos se centrarán en este payload de "tool_name" y "args".

## **3. Ejemplos de functionCall JSON**

A continuación, se presentan ejemplos para algunas de las herramientas
MCP conceptuales que se han mencionado en MAIDO y que un Servidor MCP
podría exponer para interactuar con GitHub.

### **3.1. Ejemplo para githubAccess.updateFileContent**

Esta herramienta se usaría para crear o actualizar un archivo específico
en el repositorio Git del proyecto, en una rama determinada, con un
mensaje de commit.

**functionCall JSON generada por el Orquestador:**

{  
"tool_name": "githubAccess.updateFileContent",  
"args": {  
"repositoryTarget": { // Objeto opcional para especificar repo si el
Servidor MCP maneja múltiples  
"owner": "\[nombre_dueño_repo_en_github\]",  
"repoName": "\[nombre_repo_proyecto\]"  
},  
"branchName": "docs/actualizar-vision-alcance-v1-1", // Rama donde se
aplicará el cambio  
"filePath":
"documentos_maestros/MAIDO-TPL-01-Vision_Alcance_Proyecto_LuziaCloud.md",
// Ruta completa del archivo en el repo  
"newContent": "# MAIDO-TPL-01: Visión y Alcance del Proyecto - Luzia
Cloud\n\n\*\*Versión:\*\* 1.1\n...", // Contenido completo y actualizado
del archivo  
"commitMessage": "Docs: Actualizada Visión y Alcance a v1.1 según
feedback microtarea M-DOC-003",  
"committer": { // Opcional, si el Servidor MCP lo soporta para la
autoría del commit  
"name": "AI Orquestador (MAIDO)",  
"email": "orquestador@tuproyecto.com"  
}  
}  
}

**El Servidor MCP al recibir esto debería:**

1.  Asegurar que la rama docs/actualizar-vision-alcance-v1-1 exista (o
    crearla si esa es la lógica de la herramienta).

2.  Escribir (o sobreescribir) el archivo en filePath con newContent.

3.  Realizar un commit con el commitMessage.

4.  Hacer push de la rama al repositorio remoto.

### **3.2. Ejemplo para githubAccess.createPullRequest**

Esta herramienta crearía una Pull Request en GitHub desde una rama
origen a una rama destino.

**functionCall JSON generada por el Orquestador:**

{  
"tool_name": "githubAccess.createPullRequest",  
"args": {  
"repositoryTarget": {  
"owner": "\[nombre_dueño_repo_en_github\]",  
"repoName": "\[nombre_repo_proyecto\]"  
},  
"sourceBranch": "docs/actualizar-vision-alcance-v1-1", // Rama con los
cambios  
"targetBranch": "develop", // Rama a la que se quiere fusionar  
"title": "Docs: Actualización Visión y Alcance v1.1 (M-DOC-003)",  
"body": "Esta PR actualiza el Documento de Visión y Alcance a la versión
1.1, incorporando el feedback de la microtarea M-DOC-003.\n\nCambios
principales:\n- Sección 3.2 actualizada.\n- Añadido objetivo
4.1.c.\n\nSolicito revisión del Product Visionary.",  
"assignees": \["\[usuario_github_product_visionary\]"\], // Opcional  
"reviewers": \["\[usuario_github_product_visionary\]"\], // Opcional  
"labels": \["documentacion", "requiere-revision"\] // Opcional  
}  
}

**El Servidor MCP al recibir esto debería:**

1.  Usar la API de GitHub para crear una Pull Request con los detalles
    proporcionados.

### **3.3. Ejemplo para githubAccess.initiateMicrotaskPR**

Esta herramienta de más alto nivel podría crear una rama y una PR
inicial (quizás con un archivo placeholder o el prompt) para una nueva
microtarea de codificación.

**functionCall JSON generada por el Orquestador:**

{  
"tool_name": "githubAccess.initiateMicrotaskPR",  
"args": {  
"repositoryTarget": {  
"owner": "\[nombre_dueño_repo_en_github\]",  
"repoName": "\[nombre_repo_proyecto\]"  
},  
"baseBranch": "develop", // Rama desde la cual se creará la nueva rama
de feature  
"newBranchName": "feature/MVP1-AUTH-F005-login-ui", // Nombre sugerido
para la nueva rama  
"prTitle": "Feature: MVP1-AUTH-F005 - Implementación UI de Login",  
"prBodyTemplate": "## Microtarea: MVP1-AUTH-F005\n\n\*\*Objetivo:\*\*
Implementar la interfaz de usuario para la pantalla de inicio de sesión
según las especificaciones del Paquete de Tarea Inteligente adjunto (o
referenciado).\n\n\*\*Criterios de Aceptación Clave:\*\*\n- \[Criterio
1\]\n- \[Criterio 2\]\n\n\*\*Archivos Placeholder Creados:\*\*\n-
\`src/features/auth/components/LoginForm.tsx\` (esqueleto
inicial)\n\n\*\*Asignado a:\*\* LLM de Codificación (vía Product
Visionary)",  
"placeholderFiles": \[ // Opcional: el Servidor MCP podría crear estos
archivos  
{  
"filePath": "src/features/auth/components/LoginForm.tsx",  
"content": "// TODO: Implementar LoginForm según Paquete de Tarea
MVP1-AUTH-F005\nexport default function LoginForm() { return null; }"  
}  
\],  
"commitMessageInitial": "feat: Iniciar estructura para microtarea
MVP1-AUTH-F005 (Login UI)",  
"labels": \["feature", "requiere-desarrollo-ia"\]  
}  
}

**El Servidor MCP al recibir esto debería:**

1.  Crear la rama feature/MVP1-AUTH-F005-login-ui a partir de develop.

2.  (Opcional) Commitear los placeholderFiles a la nueva rama con el
    commitMessageInitial.

3.  Crear una Pull Request desde feature/MVP1-AUTH-F005-login-ui hacia
    develop con el título, cuerpo y etiquetas proporcionados.

### **3.4. Ejemplo para projectLog.addEntryToMAIDO62x**

Esta herramienta actualizaría el archivo de Log de Cambios y
Aprendizajes Estructurado (MAIDO-6.2.x) del proyecto.

**functionCall JSON generada por el Orquestador (después de que el
Product Visionary apruebe el contenido del feedback):**

{  
"tool_name": "projectLog.addEntryToMAIDO62x",  
"args": {  
"repositoryTarget": {  
"owner": "\[nombre_dueño_repo_en_github\]",  
"repoName": "\[nombre_repo_proyecto\]"  
},  
"logFilePath": "maido_logs/MAIDO-6.2.1-ProyectoX_MVP1.md", // Ruta al
archivo de log específico  
"entryData": { // Payload estructurado según MAIDO-STRUCT-6.2.x  
"microtarea_id": "MVP1-AUTH-F005",  
"titulo_microtarea": "Implementación UI de Login",  
"fecha_completitud_product_visionary": "2025-05-28",  
"feedback_implementador": {  
"desviaciones_instrucciones_originales": "Ninguna.",  
"informacion_util_faltante_al_inicio": "El Paquete de Tarea fue muy
completo.",  
"aprendizajes_clave_desafios_tecnicos": "La integración con el
componente X requirió un ajuste en Y.",  
"sugerencias_mejora_futuros_prompts_documentacion": "Considerar incluir
ejemplos de Z en los prompts para este tipo de UI."  
},  
"implementacion_detalles": {  
"decisiones_notables_tomadas": "Se utilizó el patrón X para el manejo de
estado del formulario.",  
"guia_verificacion_proporcionada_resumen": "Guía de verificación cubrió
todos los Criterios de Aceptación.",  
"artefactos_creados": \[  
{"tipo": "Frontend Component", "ruta_o_nombre":
"src/features/auth/components/LoginForm.tsx", "descripcion_breve":
"Formulario de inicio de sesión"}  
\],  
"artefactos_modificados_significativamente": \[  
{"tipo": "Frontend Page", "ruta_o_nombre": "src/pages/LoginPage.tsx",
"descripcion_cambio": "Integrado LoginForm"}  
\],  
"versiones_librerias_clave_usadas_asumidas": "react@18.2.0"  
},  
"impacto_documental_identificado": \[  
{  
"doc_id_afectado":
"MAIDO-TPL-03-Especificaciones_Funcionales_ProyectoX.md",  
"version_actual_doc": "v1.2",  
"secciones_afectadas": "Sección de Autenticación, RF-AUTH-001.",  
"cambio_sugerido_resumen": "Añadir detalle sobre el flujo de 'Recordar
Contraseña'."  
}  
\],  
"seguimiento_maido": {  
"pr_principal_asociada":
"https://github.com/\[owner\]/\[repo\]/pull/123",  
"consolidacion_documental_requerida": "Si",  
"procesado_por_orquestador_para_impacto": "Pendiente",  
"notas_adicionales_product_visionary": "Excelente implementación.
Proceder con la consolidación documental para Doc 3."  
}  
},  
"commitMessage": "Log: Añadida entrada de feedback para microtarea
MVP1-AUTH-F005",  
"branchNameForLogUpdate": "log/update-mvp1-auth-f005-feedback" //
Servidor MCP creará esta rama, commiteará y creará PR para el log  
}  
}

**El Servidor MCP al recibir esto debería:**

1.  Crear la rama log/update-mvp1-auth-f005-feedback (o una similar).

2.  Leer el contenido actual del archivo MAIDO-6.2.x especificado.

3.  Añadir la nueva entrada (formateada como YAML o JSON dentro del
    Markdown, según la convención del proyecto).

4.  Commitear el cambio con el commitMessage.

5.  Crear una PR para fusionar esta actualización del log a la rama
    principal de documentación/desarrollo.

Estos ejemplos deberían darte una idea clara de cómo el orquestador
puede instruir a tu Servidor MCP para realizar acciones complejas de
manera estructurada, minimizando la intervención manual del Product
Visionary.
