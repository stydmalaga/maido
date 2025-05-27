# **MAIDO-TPL-09: Sistema de Diseño UI y Biblioteca de Componentes - \[Nombre_del_Proyecto\]**

Versión: 1.0

Fecha: \[Fecha_Creacion_o_Ultima_Modificacion\]

Estado: Borrador / En Desarrollo / Consolidado

Proyecto: \[Nombre_del_Proyecto\]

ID del Proyecto (si aplica): \[ID_Proyecto\]

## **1. Propósito de este Documento**

- Definir y documentar el sistema de diseño y la biblioteca de
  componentes de interfaz de usuario (UI) reutilizables para el proyecto
  "\[Nombre_del_Proyecto\]".

- Asegurar la consistencia visual, la coherencia en la interacción y la
  eficiencia en el desarrollo del frontend.

- Servir como una guía central para el Product Visionary, el orquestador
  IA, el LLM de codificación, diseñadores UI/UX y desarrolladores
  frontend.

- Facilitar la creación rápida de nuevas vistas y funcionalidades
  manteniendo una alta calidad estética y de experiencia de usuario.

- Este documento se basa en el
  MAIDO-TPL-02-Identidad_Lore_UX_Proyecto.md (si aplica) y complementa
  las MAIDO-TPL-03-Especificaciones_Funcionales_Proyecto.md.

## **2. Introducción al Sistema de Diseño**

- **2.1. Filosofía y Objetivos del Sistema de Diseño:**

  - ¿Cuáles son los principios que guían el diseño de la interfaz (ej.
    modularidad, accesibilidad, claridad, consistencia, eficiencia)?

  - ¿Qué se busca lograr con este sistema de diseño (ej. acelerar el
    desarrollo, mejorar la UX, mantener la identidad de marca)?

- **2.2. Audiencia:**

  - ¿Quiénes utilizarán este sistema de diseño (desarrolladores
    frontend, diseñadores, orquestador IA al generar especificaciones de
    UI)?

- **2.3. Herramientas (si aplica):**

  - ¿Se utilizará alguna herramienta específica para documentar y
    visualizar los componentes (ej. Storybook, Zeroheight, Figma como
    fuente de verdad para el diseño)?

## **3. Fundamentos del Diseño Visual (Tokens de Diseño)**

- **3.1. Paleta de Colores Detallada:**

  - Colores primarios, secundarios, de acento, de estado (error, éxito,
    advertencia, información), neutros (grises).

  - Especificar valores exactos (HEX, RGB, HSL) y nombres de variables
    (si se usan tokens CSS/JS, ej. --color-primary-500,
    theme.colors.primary).

  - Casos de uso para cada color.

- **3.2. Tipografía:**

  - Familias tipográficas para encabezados, cuerpo de texto, etiquetas,
    etc.

  - Escala tipográfica: Tamaños de fuente definidos (h1, h2, p, small),
    pesos, alturas de línea.

  - Nombres de variables para la escala tipográfica.

- **3.3. Espaciado y Cuadrícula (Layout Grid):**

  - Unidades de espaciado base (ej. 8px).

  - Escala de espaciado (márgenes, paddings).

  - (Opcional) Definición de un sistema de cuadrícula para el layout
    general de las páginas.

- **3.4. Bordes y Sombras:**

  - Estilos de borde (radios, grosores, colores).

  - Definición de sombras (elevación, profundidad).

- **3.5. Iconografía:**

  - Biblioteca de iconos seleccionada (ej. Material Icons, Font Awesome,
    Feather Icons, iconos personalizados SVG).

  - Tamaños estándar y uso.

- **3.6. Imágenes y Multimedia:**

  - Directrices para el uso de imágenes (estilo, proporciones,
    optimización).

  - (Si aplica) Estilos para elementos multimedia (vídeo, audio).

## **4. Biblioteca de Componentes UI Reutilizables**

Para cada componente de la biblioteca:

**Componente: \[NombreDelComponente\] (ej. Button, Card, Modal,
TextInput, Dropdown)**

- **4.X.1. Descripción y Propósito:**

  - ¿Qué es este componente y para qué se utiliza?

  - Casos de uso principales.

- **4.X.2. Visualización (si se usa Storybook u otra herramienta):**

  - Enlace a la historia del componente en Storybook o imagen/wireframe.

- **4.X.3. Variaciones y Estados:**

  - Diferentes variantes del componente (ej. botón primario, secundario,
    de solo texto; input con ícono, con error).

  - Estados visuales (ej. normal, hover, focus, active, disabled,
    loading, error, success).

- **4.X.4. Propiedades (Props) de Configuración:**

  - Listar las propiedades que el componente acepta para su
    personalización.

  - Para cada prop:

    - **Nombre:**

    - **Tipo de Dato:** (ej. string, number, boolean, () =\> void,
      ReactNode)

    - **¿Obligatoria?:**

    - **Valor por Defecto (si tiene):**

    - **Descripción:** ¿Qué controla esta propiedad?

    - **Valores Aceptados (si es un enum o conjunto limitado):**

- **4.X.5. Eventos Emitidos (si aplica):**

  - ¿Qué eventos personalizados emite el componente (ej. onClick,
    onChange, onClose)?

  - ¿Qué datos se pasan con el evento?

- **4.X.6. Slots o Composición (si aplica):**

  - ¿Permite el componente anidar otros componentes o contenido
    personalizado (ej. children en React, slots en Vue)?

- **4.X.7. Accesibilidad (A11Y):**

  - Consideraciones de accesibilidad específicas para este componente
    (ej. atributos ARIA, navegación por teclado).

- **4.X.8. Uso y Ejemplos de Código:**

  - Pequeños fragmentos de código mostrando cómo usar el componente con
    sus props más comunes.

  - (Opcional) Buenas y malas prácticas de uso.

- **4.X.9. Notas de Implementación (para desarrolladores):**

  - Cualquier detalle técnico relevante sobre cómo está construido o
    cómo interactúa con otros sistemas.

**Categorías de Componentes (Ejemplos):**

- **Atómicos/Base:** (Botones, Inputs, Iconos, Tipografía base, Colores)

- **Moléculas/Bloques:** (Tarjetas, Elementos de Formulario con Label y
  Error, Elementos de Lista, Barras de Navegación Simples)

- **Organismos/Secciones:** (Formularios Completos, Cabeceras de Página,
  Secciones de Dashboard, Modales Complejos)

- **Plantillas de Página (Layouts):** (Estructuras de layout comunes
  para diferentes tipos de páginas)

## **5. Patrones de Diseño de Interacción**

- Describir patrones de interacción comunes y cómo deben implementarse
  de manera consistente.

  - Ejemplos:

    - Manejo de formularios (validación, envío, mensajes de
      error/éxito).

    - Carga de datos y estados de carga.

    - Notificaciones y alertas al usuario.

    - Navegación principal y secundaria.

    - Búsqueda y filtrado.

    - Procesos de varios pasos (wizards).

## **6. Contribución y Mantenimiento del Sistema de Diseño**

- ¿Cómo se proponen nuevos componentes o cambios a los existentes?

- ¿Quién es responsable de mantener y actualizar el sistema de diseño y
  su documentación?

- Proceso de revisión y aprobación de nuevos componentes.

## **7. Historial de Versiones de este Documento**

- **v1.0 (\[Fecha\]):** Creación inicial.

- **vX.Y (\[Fecha\]):** \[Breve descripción del cambio, ej. "Añadido
  componente Modal", "Actualizada paleta de colores"\].
