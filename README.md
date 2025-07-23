# Proyecto de Automatización de Pruebas UI con Playwright y Python 🧪

## 🚀 Descripción General
Este proyecto es un framework de automatización de pruebas de interfaz de usuario (UI) robusto y escalable, desarrollado con Playwright y Python, utilizando Pytest como gestor de pruebas. El objetivo principal es validar exhaustivamente las funcionalidades de aplicaciones web, ofreciendo un conjunto completo de utilidades para la interacción con elementos, manejo de datos y generación de evidencias.

Este repositorio demuestra capacidades avanzadas en el diseño, desarrollo y ejecución de pruebas automatizadas, enfocándose en la modularidad, reusabilidad del código y la generación de informes detallados.

## ✨ Características Principales
El framework incluye una serie de funcionalidades diseñadas para optimizar y enriquecer el proceso de automatización:

* **Tecnología Moderna:** Implementado con Playwright, un framework rápido y confiable para la automatización de navegadores.
* **Lenguaje de Programación:** Desarrollado en Python 3.13.5 (versión recomendada, aunque puede ser compatible con otras versiones de Python 3).
* **Gestión de Pruebas:** Organización y ejecución de casos de prueba con Pytest, aprovechando su sistema de fixtures.
* **Cross-Browser & Responsive Testing:** Soporte para pruebas en Chromium, Firefox y WebKit, incluyendo emulación de dispositivos móviles como iPhone 12 y Pixel 5 para asegurar la compatibilidad y el comportamiento responsivo.
* **Manejo de Elementos y Interacciones:** Funciones globales para:
    * Validación de visibilidad de elementos.
    * Verificación de contenido de texto.
    * Relleno de campos de texto y numéricos.
    * Clics avanzados y doble clic.
    * Interacciones con radio buttons, checkboxes y dropdowns.
    * Drag and drop (métodos nativo y manual).
    * Manejo de alertas, confirmaciones y prompts.
    * Interacción con iframes y nuevas ventanas/pestañas.
    * Eventos de teclado y ratón (hover, scroll).
    * Validación de títulos de página.
* **Gestión de Archivos:** Capacidades para lectura de diversos formatos de datos:
    * Excel (.xlsx)
    * CSV (.csv)
    * JSON (.json)
    * XML
* **Generación de Evidencias:** Capturas de pantalla automáticas en puntos críticos y rutas configurables para almacenamiento de videos y trazas de ejecución.
* **Logging Configurable:** Sistema de logging detallado con niveles de salida separados para consola y archivo, facilitando la depuración y el seguimiento de la ejecución.
* **Organización del Código:** Estructura de proyecto modular que separa locators, páginas y utilidades, promoviendo la reusabilidad y mantenibilidad.

## 🛠️ Tecnologías Utilizadas
* **Playwright:** Framework de automatización de navegadores.
* **Python:** Lenguaje de programación.
* **Pytest:** Framework para la gestión y ejecución de pruebas.
* **pytest-html:** Para la generación de informes HTML autocontenidos.
* **Openpyxl:** Librería para manejar archivos .xlsx.
* **CSV:** Módulo para trabajar con archivos .csv.
* **JSON:** Módulo para manejar archivos JSON.
* **xml.etree.ElementTree:** Módulo para trabajar con archivos XML.
* **Logging:** Módulo estándar de Python para el registro de eventos.

## 📂 Estructura del Proyecto
La estructura del proyecto está diseñada para ser clara, modular y fácil de mantener:
```
.
├── PRV/
│   ├── locator/                # Contiene los localizadores de elementos web por página/componente
│   │   ├── __init__.py
│   │   ├── locator_AlertsAndPopups.py
│   │   ├── locator_barraMenu.py
│   │   ├── locator_cheBoxLista.py
│   │   ├── locator_getByAltText.py
│   │   ├── locator_getByLabel.py
│   │   ├── locator_getByPlaceholdr.py
│   │   ├── locator_getByRole.py
│   │   ├── locator_getByTestId.py
│   │   ├── locator_getByText.py
│   │   ├── locator_getByTitle.py
│   │   ├── locator_mouseAction.py
│   │   ├── locator_tablaDinamica.py
│   │   ├── locator_tablaEstatica.py
│   │   └── locator_uploadFiles.py
│   ├── pages/                  # Contiene las clases Page Object Model (POM)
│   │   ├── __init__.py
│   │   └── base_page.py        # Clase base con funciones globales de interacción
│   └── utils/                  # Utilidades como configuraciones y logger
│       ├── __init__.py
│       ├── config.py           # Configuraciones de URLs y rutas de directorios
│       └── logger.py           # Configuración del sistema de logging
├── test/
│   ├── archivos/               # Archivos de prueba (ej. para upload/download)
│   │   └── archivos_data_fuente/
│   ├── reportes/               # Directorio para almacenar evidencias de las pruebas
│   │   ├── html/               # Informes HTML
│   │   ├── video/              # Grabaciones de video de las ejecuciones
│   │   ├── traceview/          # Archivos traceview de Playwright
│   │   └── imagen/             # Capturas de pantalla
│   ├── conftest.py             # Fixtures de Pytest para configuración de tests
│   ├── test_alertsAndPopups.py
│   ├── test_cargarArchivo.py
│   ├── test_checkBoxLista.py
│   ├── test_getByAltText.py
│   ├── test_getByLabel.py
│   # ... otros archivos de prueba
├── .gitignore                  # Archivo para ignorar archivos y directorios en Git
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo
```

## ⚙️ Configuración e Instalación
**Clonar el repositorio:**

```bash
git clone https://github.com/raizengod/pruebas_interfaz_usuario_-UI-.git
cd PRV
```

**Crear y activar un entorno virtual (recomendado):**

```bash
python -m venv mv_PRV
# En Windows
.\venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

**Instalar las dependencias:**

```bash
pip install -r requirements.txt
playwright install  # Instala los navegadores necesarios (Chromium, Firefox, WebKit)
# (Asegúrate de que pytest-reporter-html1 esté incluido en requirements.txt)
```

```bash
pip install playwright pytest pytest-html openpyxl
playwright install
```

Asegurar Directorios de Evidencias: El archivo config.py define una función ensure_directories_exist() que crea automáticamente las carpetas necesarias para reportes y archivos de datos. Asegúrate de que esta función se ejecute, o créalas manualmente según la Estructura del Proyecto.

## 🚀 Uso
Para ejecutar las pruebas, asegúrate de estar en el entorno virtual activado y en la raíz del proyecto.

**Ejecución de Pruebas**

1.  **Ejecuta las pruebas y genera los resultados de reporte:**
    ```bash
    pytest PRV\test\ -s -v --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

2.  **Ejecutar todas las pruebas con Pytest:**
    ```bash
    pytest PRV\test\
    ```

3.  **Ejecutar pruebas específicas (ejemplo):**
    ```bash
    pytest PRV\test\test_home.py
    ```

4.  **Ejecutar todas las pruebas con reporte detallado y genera los resultados en reporte HTML:**:**
    ```bash
    pytest PRV\test\ -s -v --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

## 📈 Reportes y Evidencias

Todas las evidencias generadas durante la ejecución de las pruebas se almacenarán en el directorio test/reportes/:
* test/reportes/html/: Contiene los informes HTML de Pytest.
* test/reportes/video/: Videos de la ejecución de las pruebas (si están configurados en conftest.py).
* test/reportes/traceview/: Archivos de traza de Playwright para análisis detallado.
* test/reportes/imagen/: Capturas de pantalla tomadas durante la ejecución.

## 📈 Integración Continua (CI)

El proyecto está configurado con **GitHub Actions** para ejecutar las pruebas automáticamente en cada push a la rama principal y en cada pull request. El archivo de configuración se encuentra en `.github/workflows/playwright.yml`. Esto garantiza que cualquier cambio en el código se valide rápidamente, detectando regresiones de manera temprana.

## ✅ Habilidades Demostradas

A través de este proyecto, demuestro las siguientes habilidades clave en QA Automation:

* **Diseño de Frameworks de Automatización:** Implementación de una estructura de proyecto modular y escalable utilizando el patrón Page Object Model (POM).
* **Automatización de Pruebas End-to-End:** Creación de escenarios de prueba realistas que cubren flujos de usuario completos.
* **Uso Avanzado de Playwright:** Experiencia profunda en la interacción con elementos web, manejo de aserciones robustas, gestión de contextos de navegador, emulación de dispositivos y configuración de pruebas con Playwright.
* **Programación en Python:** Habilidad para escribir código limpio, legible y eficiente para la automatización, aplicando principios de diseño de software.
* **Integración Continua (CI):** Configuración y mantenimiento de pipelines de CI con GitHub Actions para una ejecución de pruebas automatizada y recurrente, esencial en el ciclo de vida del desarrollo de software.
* **Identificación y Reporte de Bugs:** Capacidad para diseñar pruebas que revelen defectos y, en un entorno de trabajo real, reportarlos adecuadamente con evidencia relevante.
* **Mantenibilidad de Código:** Organización del código para facilitar futuras actualizaciones y extensiones de las pruebas, promoviendo la colaboración y escalabilidad a largo plazo.
* **Manejo de Datos en Pruebas:** Experiencia en la lectura y escritura de datos de prueba desde/hacia archivos Excel, CSV, JSON y XML.

# 🔮 Mejoras Futuras / Roadmap

Este proyecto es una base sólida, y siempre hay espacio para la mejora continua. Algunas ideas para futuras extensiones incluyen:

* Integrar pruebas de rendimiento básicas utilizando herramientas específicas de Playwright o integraciones.
* Configurar variables de entorno para la URL base y credenciales, mejorando la seguridad y flexibilidad del framework.
* Explorar la paralelización de pruebas para reducir los tiempos de ejecución en suites grandes.
* Extender la cobertura con pruebas de APIs para una validación completa del backend (si aplica).