from flask import Flask, render_template, redirect, url_for
from flask_oauthlib.client import OAuth
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
oauth = OAuth(app)

facebook = oauth.remote_app(
    'facebook',
    app_id=app.config['FACEBOOK_APP_ID'],
    app_secret=app.config['FACEBOOK_APP_SECRET'],
    request_token_params={
        'scope': 'email',
    },
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
)

twitter = oauth.remote_app(
    'twitter',
    app_id=app.config['TWITTER_API_KEY'],
    app_secret=app.config['TWITTER_API_SECRET'],
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/facebook')
def login_facebook():
    return facebook.authorize(callback=url_for('facebook_authorized', _external=True))

@app.route('/login/facebook/authorized')
def facebook_authorized():
    response = facebook.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied or error.'
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
