from bs4 import BeautifulSoup
import requests

def handler(request):
    url = "https://www.cac.bcr.com.ar/es/precios-de-pizarra"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    tabla = soup.find("table", class_="table")
    precios = []

    if tabla:
        rows = tabla.find_all("tr")[1:]  # Saltar header
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                precios.append({
                    "producto": cols[0].text.strip(),
                    "entrega": cols[1].text.strip(),
                    "precio": cols[2].text.strip()
                })

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {"precios": precios}
    }
