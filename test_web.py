import requests
import pytest


SITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.dhoconstrucciones.com/"
]

@pytest.mark.parametrize("url", SITES)
def test_sitio_esta_online(url):
    """Verifica que el sitio responda correctamente"""
    try:
        response = requests.get(url, timeout=10)
        assert response.status_code == 200
    except requests.exceptions.RequestException as e:
        pytest.fail(f"El sitio {url} no es accesible: {e}")