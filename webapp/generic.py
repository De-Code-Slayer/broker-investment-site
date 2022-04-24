from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import json
import requests
from . import app

from .import app, mail


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    print(app.config["MAIL_SERVER"])
    mail.send(msg)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email



def get_btc(coin):
    # Import libraries
    coin = coin.upper()

    # defining key/request url
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # print(f"{data['symbol']} price is {data['price']}")
    return data['price']


