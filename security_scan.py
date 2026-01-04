import requests
import csv
from datetime import datetime

sites = [
    "https://www.google.com",
    "https://www.python.org"
]

# Cabeceras que vamos a auditar (Estándar OWASP)
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]

filename = "auditoria_seguridad.csv"

with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["Fecha", "URL", "Cabecera", "Estado", "Valor"])

    for url in sites:
        try:
            response = requests.get(url, timeout=10)
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            for header in SECURITY_HEADERS:
                valor = response.headers.get(header)
                estado = "PRESENTE" if valor else "FALTA (RIESGO)"
                writer.writerow([fecha, url, header, estado, valor if valor else "N/A"])
            
            print(f"Auditoría completada para: {url}")
        except Exception as e:
            print(f"Error analizando {url}: {e}")