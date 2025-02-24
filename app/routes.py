from flask import Blueprint, render_template, request
from services.weather_service import WeatherService

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    clima = None
    error = None
    if request.method == 'POST':
        ciudad = request.form['ciudad']
        weather_service = WeatherService()
        clima = weather_service.get_weather(ciudad)
        if not clima:
            error = "Ciudad no encontrada. Intenta de nuevo."
    return render_template('index.html', clima=clima, error=error)