import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Lista de sitios a analizar
sites = [
    "https://www.example.com",
    "https://www.python.org"
]

# Nombre del archivo donde se guardarán los datos
filename = "resultados_scraper.csv"

# Preparamos los headers para parecer un navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Abrimos el archivo en modo "append" (añadir al final)
with open(filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Si el archivo está vacío, escribimos la cabecera
    if file.tell() == 0:
        writer.writerow(["Fecha", "URL", "Titulo", "Estado"])

    for url in sites:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string.strip() if soup.title else "Sin título"
                writer.writerow([fecha_actual, url, title, "OK"])
                print(f"Guardado: {url}")
            else:
                writer.writerow([fecha_actual, url, "N/A", f"Error {response.status_code}"])
                
        except Exception as e:
            writer.writerow([datetime.now(), url, "Error", str(e)])
            print(f"Error en {url}: {e}")