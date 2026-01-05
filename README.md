# 🛡️ Web Security Scraper & OWASP Auditor

Este proyecto es una herramienta de automatización construida con **Python** y **GitHub Actions**. Realiza un monitoreo diario de sitios web para extraer información básica y auditar el cumplimiento de cabeceras de seguridad basadas en los estándares de **OWASP**.

## 🚀 Funcionalidades
* **Web Scraping Automático:** Extrae títulos y estados de conexión de una lista de URLs.
* **Auditoría de Seguridad OWASP:** Verifica la presencia de cabeceras críticas (CSP, HSTS, X-Frame-Options, etc.).
* **Ejecución Programada:** Configurado para correr automáticamente cada 24 horas mediante GitHub Actions.
* **Historial de Datos:** Genera y actualiza archivos `.csv` con los resultados de cada análisis.

## 📊 Tecnologías Utilizadas
* **Lenguaje:** Python 3.9
* **Librerías:** `requests`, `beautifulsoup4`
* **CI/CD:** GitHub Actions
* **Formato de salida:** CSV (Valores separados por comas)

## 🛠️ Estructura del Proyecto
* `scraper.py`: Script encargado de la extracción de datos generales.
* `security_scan.py`: Script de auditoría de seguridad OWASP.
* `.github/workflows/main.yml`: Configuración del flujo de trabajo automatizado.
* `auditoria_seguridad.csv`: Reporte histórico de las cabeceras de seguridad.

## 🔒 Cabeceras Auditadas
El sistema verifica las siguientes directivas de seguridad recomendadas por OWASP para prevenir ataques como XSS y Clickjacking:
1. `Content-Security-Policy`
2. `X-Frame-Options`
3. `X-Content-Type-Options`
4. `Strict-Transport-Security`
5. `Referrer-Policy`

## ⚙️ Instalación y Uso Local
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/Jan0890/python-scraper-automation.git](https://github.com/Jan0890/python-scraper-automation.git)