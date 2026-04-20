# Análisis Cinético de Crecimiento Fúngico

Este repositorio contiene las herramientas necesarias para procesar, modelar y analizar datos cinéticos de crecimiento fúngico obtenidos a partir de experimentos experimentales.

## Descripción del Proyecto
El objetivo principal es automatizar el ajuste de datos experimentales de biomasa vs. tiempo a un **modelo logístico (sigmoideo)**, permitiendo obtener parámetros cinéticos clave de forma rápida y reproducible.

## Características principales
- **Procesamiento automático:** Lectura y análisis de múltiples archivos CSV.
- **Modelado Cinético:** Ajuste de curvas mediante modelos logísticos para calcular:
    - `mu` ($\mu$): Tasa de crecimiento específico.
    - `K`: Capacidad de carga máxima.
    - Bondad de ajuste (R² y RMSE).
- **Reporte Automático:** Generación de un archivo Excel (`Resultados_Cineticos.xlsx`) con los parámetros obtenidos para todos los aislamientos analizados.

## Estructura del Repositorio
- `analisis.ipynb`: Notebook principal con el flujo de análisis.
- `utils.py`: Funciones de soporte para el cálculo cinético.
- `.gitignore`: Configuración para excluir archivos innecesarios o sensibles.

## Nota sobre los Datos
Para mantener la integridad y limpieza del repositorio, **la carpeta `data` y los archivos de datos crudos (`.csv`) han sido excluidos del control de versiones mediante `.gitignore`**. 

Si deseas ejecutar este análisis con tus propios datos:
1. Crea una carpeta llamada `data` en el directorio raíz.
2. Coloca tus archivos `.csv` (con columnas `tiempo` y `biomasa`) dentro de esa carpeta.
3. Ejecuta el notebook `analisis.ipynb`.

## Requisitos
El proyecto requiere Python 3 y las siguientes librerías:
- `pandas`
- `numpy`
- `scipy`
- `sklearn`
- `openpyxl`