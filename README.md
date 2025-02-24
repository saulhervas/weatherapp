# Clima App

Una sencilla aplicación web que muestra el clima actual de una ciudad usando datos de una API. La app muestra la temperatura, descripción del clima, y un icono correspondiente al clima (soleado, nublado, lluvioso, etc.).

## Características

- Consultar el clima actual de una ciudad.
- Ver detalles como la temperatura, la descripción del clima y la humedad.
- Mostrar iconos de acuerdo al clima (soleado, nublado, lluvioso, etc.).
- Desarrollada con Python y Flask para el backend.
- Utiliza una API pública para obtener los datos del clima.

## Tecnologías usadas

- **Backend**: Python, Flask
- **API del clima**: [WeatherAPI](https://www.weatherapi.com/) o la que hayas elegido.
- **Frontend**: HTML, CSS, JavaScript (plantilla básica)

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados:

- Python 3.x
- pip (gestor de paquetes de Python)
- Una clave de API de WeatherAPI (o la API que decidas usar)

## Instalación

1. **Clonar el repositorio**

   Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu-usuario/clima-app.git
   cd clima-app
2. **Instalar las dependencias**
   Asegúrate de tener pip instalado y luego instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
3. **Configurar la clave de la API**
   Regístrate en la API de WeatherAPI (o la API que estés utilizando) y consigue una clave de API. Luego, crea un archivo .env en la raíz de tu proyecto y agrega tu clave de la siguiente forma:
   ```bash
   API_KEY=tu_clave_de_api
4. **Ejecutar la aplicación**
   Una vez que todo esté configurado, puedes ejecutar el servidor Flask con el siguiente comando:
   ```bash
   python app.py

Esto iniciará el servidor localmente en http://127.0.0.1:5000/. Abre ese enlace en tu navegador para ver la aplicación en funcionamiento.
