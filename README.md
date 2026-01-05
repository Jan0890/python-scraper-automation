# 🚀 Python Web Automation & Security Monitor

Este proyecto es un sistema automatizado de **Integración Continua (CI)** que monitorea la disponibilidad y la seguridad de sitios web de forma diaria.

## 🛠️ Tecnologías Utilizadas
* **Python 3.9**: Lógica principal y scraping.
* **Pytest**: Pruebas de conectividad web.
* **GitHub Actions**: Automatización total y ejecución programada.
* **BeautifulSoup4 & Requests**: Análisis de datos y cabeceras HTTP.

## 📋 Flujo de Trabajo (Pipeline)
1. **Connectivity Test**: Verifica que las URLs respondan (Status 200).
2. **Security Audit**: Escanea cabeceras de seguridad (HSTS, CSP, X-Frame-Options).
3. **Data Logging**: Si todo pasa, guarda los resultados en `auditoria_seguridad.csv`.
4. **Auto-Commit**: El bot actualiza el repositorio con los nuevos hallazgos.

## 📊 Resultados de Seguridad
Los informes se generan automáticamente. Puedes ver el historial en:
* `auditoria_seguridad.csv` (Registro técnico de cabeceras).

## ⚙️ Instalación y Uso Local
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/Jan0890/python-scraper-automation.git](https://github.com/Jan0890/python-scraper-automation.git)