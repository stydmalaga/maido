import os
from pathlib import Path
import pypandoc # Importamos pypandoc

def convertir_docx_a_md_en_carpeta():
    """
    Convierte todos los archivos .docx en una carpeta de entrada especificada
    a archivos .md en una carpeta de salida especificada usando Pandoc.
    """
    print("--- Conversor de DOCX a Markdown (usando Pandoc) ---")

    # (El código para solicitar las carpetas de entrada y salida es el mismo)
    while True:
        ruta_carpeta_entrada_str = input("Por favor, introduce la ruta de la carpeta que contiene los archivos .docx: ")
        carpeta_entrada = Path(ruta_carpeta_entrada_str)
        if carpeta_entrada.is_dir():
            break
        else:
            print("La ruta introducida no es una carpeta válida. Inténtalo de nuevo.")

    while True:
        ruta_carpeta_salida_str = input("Por favor, introduce la ruta de la carpeta donde se guardarán los archivos .md: ")
        carpeta_salida = Path(ruta_carpeta_salida_str)
        if not carpeta_salida.exists() or carpeta_salida.is_dir():
            break
        else:
            print("La ruta de salida no es válida (debe ser una carpeta o no existir aún). Inténtalo de nuevo.")

    try:
        carpeta_salida.mkdir(parents=True, exist_ok=True)
        print(f"Carpeta de salida '{carpeta_salida.resolve()}' asegurada.")
    except OSError as e:
        print(f"Error al crear la carpeta de salida '{carpeta_salida.resolve()}': {e}")
        return

    print(f"\nBuscando archivos .docx en: {carpeta_entrada.resolve()}")
    archivos_docx_encontrados = list(carpeta_entrada.glob('*.docx'))

    if not archivos_docx_encontrados:
        print("No se encontraron archivos .docx en la carpeta de entrada.")
        return

    print(f"Se encontraron {len(archivos_docx_encontrados)} archivo(s) .docx para convertir.")
    archivos_convertidos = 0
    archivos_fallidos = 0

    for archivo_docx_path in archivos_docx_encontrados:
        nombre_archivo_sin_extension = archivo_docx_path.stem
        archivo_md_path = carpeta_salida / f"{nombre_archivo_sin_extension}.md"

        print(f"\nConvirtiendo '{archivo_docx_path.name}' a '{archivo_md_path.name}'...")
        try:
            # Usar pypandoc para la conversión
            # 'gfm' es GitHub Flavored Markdown, una opción común y buena.
            # Puedes usar 'markdown' para Markdown estándar o explorar otros formatos de salida de Pandoc.
            output = pypandoc.convert_file(
                str(archivo_docx_path.resolve()),
                'gfm', # o 'markdown_strict', 'commonmark', etc.
                outputfile=str(archivo_md_path.resolve()),
                encoding='utf-8' # Especificar codificación
            )
            assert output == "" # convert_file devuelve una cadena vacía si outputfile se especifica y tiene éxito
            print(f"Éxito: '{archivo_md_path.name}' guardado en '{carpeta_salida.resolve()}'.")
            archivos_convertidos += 1
        except Exception as e:
            # pypandoc puede lanzar pypandoc.PandocMissingError si Pandoc no está instalado o no se encuentra.
            print(f"Error al convertir '{archivo_docx_path.name}': {e}")
            if "PandocMissingError" in str(type(e)):
                print("ASEGÚRATE DE QUE PANDOC ESTÉ INSTALADO Y EN EL PATH DEL SISTEMA.")
                print("Puedes descargarlo desde https://pandoc.org/installing.html")
            archivos_fallidos += 1

    print("\n--- Resumen de la conversión ---")
    print(f"Archivos .docx procesados: {len(archivos_docx_encontrados)}")
    print(f"Archivos convertidos exitosamente a .md: {archivos_convertidos}")
    print(f"Archivos con error en la conversión: {archivos_fallidos}")
    if archivos_fallidos > 0:
        print("Revisa los mensajes de error anteriores para más detalles.")
    print("Proceso completado.")

if __name__ == "__main__":
    convertir_docx_a_md_en_carpeta()