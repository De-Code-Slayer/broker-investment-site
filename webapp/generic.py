from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
import requests
from . import app
from .import mail
from forex_python.converter import CurrencyRates

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender="veronicapage232@gmail.com"
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
  try:
    # Import libraries
    coin = coin.upper()

    # defining key/request url
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # print(data,'---------->>>>')
  except Exception as e:
    print({"error":f"{e}"})
    # print(f"{data['symbol']} price is {data['price']}")
#   return data[u'price']
  return 51603.58000000


# def update_balance(current_user):
#     balance = current_user.balance
#     interest = current_user.interest



#     interest_amount = (balance * interest)/100


    # return interest_amount

def forex():

    # c = CurrencyRates()
    # xauusd = c.get_rate('USD', 'INR')
    # gbpusd = c.get_rate('GBP', 'USD')
    # eurusd = c.get_rate('EUR', 'USD')
    # usdjpy = c.get_rate('USD', 'JPY')
    # usdcad = c.get_rate('USD', 'CAD')
    # usdchf = c.get_rate('USD', 'CHF')
    # audusd = c.get_rate('AUD', 'USD')
    # gbpjpy = c.get_rate('GBP', 'JPY')
    
    
    # currencies = {"USDINR":xauusd,"GBPUSD":gbpusd,"EURUSD":eurusd,"USDJPY":usdjpy,"USDCAD":usdcad,"USDCHF":usdchf,"AUDUSD":audusd,"GBPJPY":gbpjpy}
    return ""# currencies

def sndmail(receiver,subject,message,file=None):
    from mailer import Mailer

    mail = Mailer(email='veronicapage23@gmail.com', password='nlevlvdrriimjxdh')
    mail.send(receiver=receiver, subject=subject, message=message,file=file)
    print(mail.status)
    return mail.status


def smtpmailer():
    import smtplib

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("veronicapage232@gmail.com", "wopsoowlmvlqzzvu")

    # message to be sent
    message = "Message_you_need_to_send"

    # sending the mail
    s.sendmail("veronicapage232@gmail.com", "chukwujapheth232@gmail.com", message)

    # terminating the session
    s.quit()



def get_coin(coin):
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    try:
       # /simple/price endpoint with the required parameters
       btc = cg.get_price(ids='bitcoin', vs_currencies='usd')
       eth = cg.get_price(ids='ethereum', vs_currencies='usd')

       if coin == "BTC":
          return btc[u'bitcoin'][u'usd']
       return eth[u'ethereum'][u'usd']
    except Exception as e:
      print({"error":f"{e}"})
    






