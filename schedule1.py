import schedule
import time
import requests
time1="20:02"
currency='USD'
def job():
    print("I'm working...")
    
def bit_coin(currency):
           url ="https://api.coindesk.com/v1/bpi/currentprice.json" 
           page=requests.get(url)
           data=page.json()
           print("bitcoin price")
           result=data['bpi'][currency]
           print(result)
           
 
schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at(time1).do(bit_coin,currency)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
 
while True:
    schedule.run_pending()
    time.sleep(1)