import os

class Config:
    SECRET_KEY = os.urandom(24)  # Clave secreta para sesiones
    FACEBOOK_APP_ID = 'your_facebook_app_id'
    FACEBOOK_APP_SECRET = 'your_facebook_app_secret'
    TWITTER_API_KEY = 'your_twitter_api_key'
    TWITTER_API_SECRET = 'your_twitter_api_secret'
