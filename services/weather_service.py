import requests
from config import API_KEY, BASE_URL, ICON_URL


class WeatherService:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.icon_url = ICON_URL

    def get_weather(self, city):
        if not city:
            raise ValueError("El nombre de la ciudad no puede estar vacío")

        parameters = {"q": city, "appid": self.api_key, "units": "metric", "lang": "es"}

        try:
            res = requests.get(self.base_url, params=parameters)
            res.raise_for_status()
            data = res.json()

            if res.status_code == 200:
                # Agregar la URL del icono al diccionario de datos
                icon_code = data["weather"][0]["icon"]
                icon_url = f"{self.icon_url}{icon_code}@2x.png"  # URL del icono de alta resolución
                data["icon_url"] = icon_url  # Agregar la URL del icono al diccionario de respuesta
                return data
            else:
                print(f"Error: {data.get('message', 'No se pudo obtener los datos del clima.')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return None