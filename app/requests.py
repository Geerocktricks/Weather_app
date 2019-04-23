import urllib.request, json

api_key=None
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['WEATHER_API_KEY']
    base_url=app.config['WEATHER_API_BASE_URL']