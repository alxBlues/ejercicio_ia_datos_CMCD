# 📌 APRENDE Y MEJORA - CONSTRUCCIÓN Y MANIPULACIÓN DE CONJUNTOS DE DATOS - UNIDAD 1

## 📝 Descripción
Este proyecto tiene como objetivo aprender a importar y manipular datos desde distintos formatos (CSV y JSON) utilizando **Python y Pandas**. Además, se ha estructurado el proyecto de forma modular para facilitar su mantenimiento y ejecución.

## 📂 Estructura del Proyecto

El directorio del proyecto se organiza de la siguiente manera:

```
📁 aprende_mejora_datos
│── 📁 src                # Contiene los módulos de procesamiento de datos
│── ├── 📁 files              # Archivos de datos CSV y JSON
│── ├── ├── paises.csv       # Archivo de datos en formato CSV
│── ├── ├── peliculas.json   # Archivo de datos en formato JSON
│── ├── 📁 dist               # Carpeta donde se genera el archivo ejecutable
│── ├── ├── main             # Archivo ejecutable generado con pip install
├── ├── main.py           # Contiene el script principal de ejecución
│── requirements.txt      # Dependencias necesarias para ejecutar el proyecto
│── README.md            # Documentación del proyecto
```

## 📥 Instalación y Configuración

Para ejecutar este proyecto, siga los siguientes pasos:

### 🔹 1. Clonar el Repositorio
```sh
$ git clone https://github.com/tuusuario/aprende_mejora_datos.git
$ cd aprende_mejora_datos
```

### 🔹 2. Crear un Entorno Virtual (Opcional, pero Recomendado)
```sh
$ python -m venv venv
$ source venv/bin/activate  # En macOS/Linux
$ venv\Scripts\activate     # En Windows
```

### 🔹 3. Instalar Dependencias

Ejecute el siguiente comando para instalar todas las dependencias necesarias:
```sh
$ pip install -r requirements.txt
```

### 🔹 4. Crear el Archivo Ejecutable

Gracias a la configuración de `pipinstal`, se ha generado un archivo ejecutable en la carpeta `dist/main`. Para generarlo manualmente, puede ejecutar:
```sh
$ python setup.py install
```

### 🔹 5. Ejecutar el Proyecto

Para ejecutar el proyecto, utilice:
```sh
$ python main/main.py
```

O si desea ejecutar el archivo compilado:
```sh
$ ./dist/main
```

## 📜 Funcionalidades Implementadas

✅ Creación de un entorno de trabajo estructurado con `mkdir` para organizar `main`, `src` y `files`.
✅ Importación de datos desde archivos CSV y JSON usando Pandas.
✅ Combinación de datos en un único DataFrame para su análisis.
✅ Instalador `setup.py` para simplificar la ejecución.
✅ Archivo `requirements.txt` para instalación rápida de dependencias.
✅ Generación de un archivo ejecutable en `dist/main` para facilitar su distribución.
✅ Visualización de estadísticas con `df.head()`, `df.info()` y `df.describe()`.

## 📊 Análisis de Datos
El proyecto permite analizar los datos de los archivos `paises.csv` y `peliculas.json`:
- **paises.csv** contiene información estructurada de países.
- **peliculas.json** almacena datos en formato JSON sobre películas.

Los datos se combinan en un único DataFrame para su posterior análisis.

## 🛠 Tecnologías Utilizadas
- **Python** 🐍
- **Pandas** 📊
- **NumPy** 🔢

## 📌 Autor
**Luis Alexander Castaño Reyes** - luis-castano1 luis-castano1@upc.edu.co

📅 **Última actualización:** 20/03/2025

