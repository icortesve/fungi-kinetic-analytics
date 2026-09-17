# 🍄 Fungi Kinetic Analytics Pipeline

Pipeline automatizado y de alto rendimiento para el análisis, modelado matemático y visualización interactiva de la cinética de crecimiento fúngico (10+ aislados) mediante Python, SciPy y Plotly Express.

---

## 📂 Estructura del Proyecto

```text
fungi-kinetic-analytics/
│
├── data/
│   ├── Datos_Fermentacion_Completo.xlsx   # Archivo único con las series de tiempo (hojas por cepa)
│   └── Resultados_Cineticos.xlsx          # Reporte consolidado con parámetros y ranking
│
├── notebooks/
│   └── fungi_kinetic_analysis.ipynb       # Cuaderno interactivo principal
│
├── src/
│   └── utils.py                           # Funciones modulares (Modelo logístico y ajuste curve_fit)
│
├── requirements.txt                       # Dependencias del entorno
└── README.md                              # Documentación del proyecto
```

---

## 🚀 Tecnologías y Stack Científico
- **Python 3.x**
- **Pandas & NumPy:** Manipulación y estructuración eficiente de series de datos.
- **SciPy (curve_fit):** Ajuste de mínimos cuadrados no lineales basado en el modelo logístico sigmoideo.
- **Scikit-learn (r2_score):** Evaluación de la bondad de ajuste de los modelos.
- **Plotly Express:** Visualización interactiva avanzada (exploración de curvas y mapa cinético).

---

## 📊 Metodología y Criterio de Desempeño

1. **Modelado Cinético:** Se ajustan los datos experimentales de tiempo vs. biomasa al modelo logístico sigmoideo: $K / (1 + ((K - N_0) / N_0) \cdot e^{-\mu t})$, permitiendo extraer la tasa específica de crecimiento ($\mu$) y la capacidad de carga ($K$).
2. **Matriz de Selección ($\mu \times K$):** Para identificar cepas "super-productoras", se calcula un índice ponderado que equilibra la velocidad de desarrollo con el rendimiento máximo de biomasa, penalizando los extremos ineficientes y clasificando automáticamente a las mejores cepas del set.

---

## 🛠️ Instrucciones de Instalación y Uso

1. Clona o ubícate en la carpeta del repositorio.
2. Instala las dependencias necesarias ejecutando en tu terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. Abre el entorno de Jupyter e inicia el cuaderno ejecutando:
   ```bash
   jupyter notebook notebooks/fungi_kinetic_analysis.ipynb
   ```
4. Ejecuta las celdas secuencialmente para generar los datos sintéticos, correr el ajuste no lineal y desplegar los gráficos interactivos y el reporte ejecutivo.

---

## 👤 Autor y Contacto

Desarrollado como parte de proyectos orientados a la integración de bioinformática, ingeniería de bioprocesos y análisis avanzado de datos.

- **GitHub:** [icortesve](https://github.com/icortesve)

---
*Este proyecto se encuentra bajo los términos de la Licencia MIT.*