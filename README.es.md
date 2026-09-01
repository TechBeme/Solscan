<div align="center">

# 🔗 Solscan Transaction Viewer

**Una aplicación web Flask para visualizar y exportar transacciones de blockchain Solana**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com/)
[![Solana](https://img.shields.io/badge/Solana-Blockchain-9945FF?logo=solana)](https://solana.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Características](#-características) • [Inicio Rápido](#-inicio-rápido) • [Uso](#-uso) • [API](#-api) • [Stack Tecnológico](#%EF%B8%8F-stack-tecnológico) • [Licencia](#-licencia)

**Idiomas:** [🇺🇸 English](README.md) • [🇧🇷 Português](README.pt-BR.md)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Características](#-características)
- [Inicio Rápido](#-inicio-rápido)
- [Uso](#-uso)
- [API](#-api)
- [Stack Tecnológico](#%EF%B8%8F-stack-tecnológico)
- [Configuración](#%EF%B8%8F-configuración)
- [Contribuyendo](#-contribuyendo)
- [Licencia](#-licencia)

---

## 🎯 Descripción General

**Solscan Transaction Viewer** es una aplicación web Flask ligera que obtiene y muestra el historial de transacciones de cualquier dirección de billetera Solana usando la API de Solscan. Proporciona una vista de tabla interactiva y buscable con capacidades de ordenamiento y exportación a CSV.

Casos de uso:
- 📊 Analizar el historial de transacciones de billeteras
- 🔍 Buscar y filtrar transacciones
- 📥 Exportar datos de transacciones a CSV
- 📈 Rastrear actividad en blockchain

---

## ✨ Características

### Visualización de Datos
- **DataTable Interactiva**: Busque, ordene y filtre transacciones con facilidad
- **Detalles de Transacción**: Vea firma, número de bloque, marca de tiempo, instrucciones, firmantes y tarifas
- **Datos en Tiempo Real**: Obtiene datos de transacciones actualizados de la API de Solscan
- **Diseño Responsivo**: Funciona en escritorio y dispositivos móviles

### Capacidades de Exportación
- **Exportación CSV**: Descargue datos de transacciones en formato CSV delimitado por tabulaciones
- **Datos Formateados**: Tarifas SOL correctamente formateadas (9 decimales)
- **Historial de Transacciones**: Exporte todas las transacciones de una vez

### Características Técnicas
- **Consultas de Alto Límite**: Obtiene hasta 99.999.999 transacciones por dirección
- **Análisis de Instrucciones**: Agrupa y muestra tipos de instrucciones analizadas
- **Conversión de Tarifas**: Conversión automática de lamports a SOL
- **Almacenamiento en Memoria**: Genera el CSV en memoria antes de devolver la descarga

---

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes Python)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TechBeme/Solscan.git
cd Solscan

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutando la Aplicación

```bash
# Modo desarrollo
python flask-solscan.py

# Modo producción con Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 flask-solscan:app
```

La aplicación iniciará en `http://localhost:5000` (desarrollo) o `http://localhost:8000` (producción).

---

## 📖 Uso

### Visualizando Transacciones

1. Abra su navegador y navegue a:
   ```
   http://localhost:5000/<DIRECCIÓN_BILLETERA>
   ```
   Reemplace `<DIRECCIÓN_BILLETERA>` con cualquier dirección de billetera Solana válida.

2. La página mostrará una tabla interactiva con todas las transacciones de esa dirección.

### Usando la DataTable

- **Buscar**: Use el cuadro de búsqueda para filtrar transacciones por cualquier campo
- **Ordenar**: Haga clic en los encabezados de columna para ordenar ascendente/descendente
- **Paginación**: Navegue por las páginas de transacciones
- **Elementos por página**: Ajuste cuántas transacciones mostrar a la vez

### Exportando Datos

Haga clic en el botón **"Download CSV"** en la parte inferior de la página para descargar todos los datos de transacciones en formato CSV con delimitadores de tabulación.

---

## 🔌 API

### Endpoints

#### `GET /<address>`

Obtiene y muestra transacciones para la dirección de billetera Solana especificada.

**Parámetros:**
- `address` (parámetro de ruta): Dirección de billetera Solana

**Respuesta:**
- Página HTML con DataTable interactiva

**Ejemplo:**
```
http://localhost:5000/DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK
```

#### `GET /download/<address>`

Descarga datos de transacciones como un archivo CSV.

**Parámetros:**
- `address` (parámetro de ruta): Dirección de billetera Solana (debe haber sido consultada previamente)

**Respuesta:**
- Archivo CSV con datos de transacciones delimitados por tabulación

**Ejemplo:**
```
http://localhost:5000/download/DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK
```

---

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Propósito |
|------------|---------|----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.8+ | Lenguaje de programación principal |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) | 3.0+ | Framework web |
| **Requests** | 2.31+ | Cliente HTTP para llamadas de API |
| **Pandas** | 2.0+ | Procesamiento de datos y generación de CSV |
| **Gunicorn** | 21.0+ | Servidor WSGI de producción |
| **jQuery** | 3.6.0 | Biblioteca JavaScript |
| **DataTables** | 1.11.5 | Plugin de tabla interactiva |
| **Solscan API** | v2 | Datos de transacciones blockchain |

---

## ⚙️ Configuración

### Variables de Entorno

No se requieren variables de entorno para el uso básico. La aplicación usa la API pública de Solscan.

### Puerto Personalizado

Para ejecutar en un puerto diferente:

```bash
# Desarrollo
flask --app flask-solscan run --port 8080

# Producción
gunicorn -w 4 -b 0.0.0.0:8080 flask-solscan:app
```

### Configuración de Workers

Para despliegues en producción, ajuste los workers de Gunicorn según su servidor:

```bash
# Fórmula: (2 x CPU_CORES) + 1
gunicorn -w 9 -b 0.0.0.0:8000 flask-solscan:app  # Para CPU de 4 núcleos
```

---

## 🤝 Contribuyendo

¡Las contribuciones son bienvenidas! Así es como puedes ayudar:

1. Haz un fork del repositorio
2. Crea una rama de característica (`git checkout -b feature/caracteristica-increible`)
3. Haz commit de tus cambios (`git commit -m 'Agrega filtro de exportación'`)
4. Haz push a la rama (`git push origin feature/caracteristica-increible`)
5. Abre un Pull Request

### Reportando Problemas

Por favor, reporte errores y solicite características a través de [GitHub Issues](https://github.com/TechBeme/Solscan/issues).

---

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - vea el archivo [LICENSE](LICENSE) para detalles.

```
Licencia MIT

Copyright (c) 2026 Rafael Vieira (TechBeme)

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar
en el Software sin restricciones, incluidos, entre otros, los derechos
de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender
copias del Software, y permitir que las personas a quienes se les proporcione el Software
lo hagan, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas
las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS
AUTORES O TITULARES DE DERECHOS DE AUTOR SERÁN RESPONSABLES DE CUALQUIER RECLAMO, DAÑOS U OTRA
RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRA MANERA, QUE SURJA DE,
FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL
SOFTWARE.
```

---

## ⚠️ Descargo de Responsabilidad

Este proyecto es **independiente** y **no está afiliado con Solscan o Solana**. Es una herramienta de terceros que usa datos públicamente disponibles de la API de Solscan con fines educativos y analíticos.

- Usa endpoints de API públicamente disponibles
- Respeta límites de tasa y términos de API
- Sin garantía o garantía de precisión de datos
- Los usuarios son responsables del cumplimiento de las leyes aplicables

---

<div align="center">

**Desarrollado por [Rafael Vieira (TechBeme)](https://github.com/TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

⭐ ¡Dale una estrella a este repo si te resulta útil!

</div>
