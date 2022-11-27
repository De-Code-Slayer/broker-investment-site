import requests

def send_msg(text):
   token = "5857377640:AAGfbuKiCkZ3EbQ50uDrTFnNdGgS6EDPBU0"
   chat_id = "-1001755455286"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())

