FakeStore Data Engineering Pipeline (Bronze → Silver → Gold)

Este proyecto implementa un pipeline completo de Data Engineering en Google Colab utilizando:

✅ Python
✅ Requests
✅ Pandas
✅ PyArrow
✅ Delta Lake (con delta-rs)
✅ Google Drive como almacenamiento tipo Data Lake

La fuente de datos es la FakeStore API, una API pública utilizada para simulación de e-commerce.
fakestore_datalake/
│
├── bronze/
│   └── products/
│
├── silver/
│   └── products/
│
└── gold/
    └── category_metrics/

 Cada capa representa un nivel de refinamiento:

* Bronze : Datos crudos tal como vienen de la API.
Formato Delta Lake.

* Silver : Datos limpios y transformados:

Tipos corregidos : Rating dividido en rate / count, Categorías normalizadas y Columnas ordenadas

* Gold : Tablas analíticas listas para BI:
* 
Precio promedio por categoría, Rating promedio, Total de reviews, Cantidad de productos.

🛠️ Tecnologías utilizadas : Python 3.12, Pandas, PyArrow, Delta Lake (delta-rs), Google Colab, Google Drive como Data Lake

y Requests.

** Pipeline Paso a Paso

1️⃣ Ingesta (Bronze) : Llamada a FakeStore API , Persistencia en Delta Lake, Copia a Google Drive, Esquema automático

2️⃣ Transformación (Silver)  : Conversión de tipos, Normalización de texto, Extracción del rating, Limpieza de columnas y

DataFrame final limpio.

3️⃣ Enriquecimiento (Gold): Agregaciones por categoría: avg_price, avg_rating, total_reviews y product_count.

| category    | avg_price | avg_rating | total_reviews | product_count |
| ----------- | --------- | ---------- | ------------- | ------------- |
| electronics | …         | …          | …             | …             |
| jewelry     | …         | …          | …             | …             |

Cada carpeta contiene:
✔ Archivos .parquet
✔ Carpeta _delta_log
✔ Tabla Delta Lake válida

⭐ Habilidades demostradas en este proyecto

Este proyecto muestra experiencia práctica en:

🔹 Construcción de pipelines ETL
🔹 Data Lake design (Bronze/Silver/Gold)
🔹 Delta Lake con delta-rs
🔹 Limpieza y transformación de datos
🔹 Pandas + PyArrow
🔹 Integración con APIs REST
🔹 Organización profesional de proyectos
🔹 Buenas prácticas en ingeniería de datos

Autora

Mónica Leiva
Analista de Datos | Data Engineer Junior
LinkedIn: (www.linkedin.com/in/monica-leiva-b008a92b0)
GitHub: (https://github.com/monica200880)



