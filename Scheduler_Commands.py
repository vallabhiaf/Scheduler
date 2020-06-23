#!/usr/bin/python3
#author-Vallabh

from apscheduler.schedulers.background import BackgroundScheduler


from flask import Flask
import schedule
import time
import requests
import datetime
import os
from cfenv import AppEnv
from SAP_weibullPDMS_1 import test_1
from SAP_weibullCALLPROC_2 import test_2
from SAP_postToWeibull_3 import test_3
from SAP_weibullTrainBasedonMacID_4 import test_4
from SAP_WeibullTrainWithoutMacID_5 import test_5
from CONSTANTS import TRAINING_SCHEDULER_TIME,PREDICTION_SCHEDULER_TIME

# TRAINING_SCHEDULER_UNIT='seconds'
# TRAINING_SCHEDULER_TIME_INTERVAL=60

# PREDITCION_SCHEDULER_UNIT='seconds'
# PREDICTION_SCHEDULER_TIME_INTERVAL=30
# #SCHEDULER_SERVICE=1
# #env = AppEnv()



# # # DB defaults
# # HANA_DB_ADDRESS = 'zeus.hana.prod.eu-central-1.whitney.dbaas.ondemand.com'
# # HANA_DB_PORT = 30755
# # HANA_DB_USER = 'DB_USER'
# # HANA_DB_PASSWORD = 'Test1234'
# # HANA_DB_CERT = ''


# if os.getenv('VCAP_APPLICATION'):
#     print("Getting values from Cloud Environment")
#     TRAINING_SCHEDULER_UNIT=os.getenv('TRAINING_SCHEDULER_UNIT')
#     TRAINING_SCHEDULER_UNIT = TRAINING_SCHEDULER_UNIT.strip()
#     TRAINING_SCHEDULER_UNIT= TRAINING_SCHEDULER_UNIT.lower()
#     TRAINING_SCHEDULER_TIME_INTERVAL=os.getenv('TRAINING_SCHEDULER_TIME_INTERVAL')
#     if TRAINING_SCHEDULER_UNIT == 'hour':
#         TRAINING_SCHEDULER_TIME_INTERVAL =TRAINING_SCHEDULER_TIME_INTERVAL *60 *60
   
#     PREDITCION_SCHEDULER_UNIT=os.getenv('PREDITCION_SCHEDULER_UNIT')
#     PREDITCION_SCHEDULER_UNIT = PREDITCION_SCHEDULER_UNIT.strip()
#     PREDITCION_SCHEDULER_UNIT = PREDITCION_SCHEDULER_UNIT.lower()
#     PREDICTION_SCHEDULER_TIME_INTERVAL=os.getenv('PREDICTION_SCHEDULER_TIME_INTERVAL')
#     if PREDITCION_SCHEDULER_UNIT == 'hour':
#         PREDICTION_SCHEDULER_TIME_INTERVAL =PREDICTION_SCHEDULER_TIME_INTERVAL *60 *60
#     SCHEDULER_SERVICE=os.getenv('SCHEDULER_SERVICE')
#     ## DB Configurations
#     # hanaDBService = env.get_service(label='hana')
#     # HANA_DB_ADDRESS = hanaDBService.credentials['host']
#     # # print(HANA_DB_ADDRESS)
#     # HANA_DB_PORT = int(hanaDBService.credentials['port'])
#     # # print(HANA_DB_PORT)
#     # HANA_DB_USER = hanaDBService.credentials['user']
#     # # print(HANA_DB_USER)
#     # HANA_DB_PASSWORD = hanaDBService.credentials['password']
#     # # print(HANA_DB_ADDRESS)
#     # HANA_DB_CERT = hanaDBService.credentials['certificate']



def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")


app = Flask(__name__)
cf_port = os.getenv("PORT")


@app.route("/USD")
def main_system():
    print("Main system started")
    #from caller import final_1
    test_1()
    print("first done")
    test_2()
    print("second done")
    test_3()
    print("third done")
    test_4()
    print("fourth done")
    test_5()
    print("fifth done")
    
        #final_1()
               

# @app.route("/GBP")
# def bit_coin1():
#                 url ="https://api.coindesk.com/v1/bpi/currentprice.json" 
#                 page=requests.get(url)
#                 data=page.json()
#                 #print("bitcoin price")
#                 result=data['bpi']['GBP']
               
#                 #if SCHEDULER_SERVICE == 0:
#                  #  print("The task is being removed ....")
#                   # sched.remove_job('my_job_id_2')
#                 print('Timestamp: {:%Y-%m-%d %H:%M:%S} for GBP'.format(datetime.datetime.now()))
#                 print(result)
#                 return str(result)
    

# #schedule.every().day.at(TRAINING_SCHEDULER_TIME).do(main_system)
# #schedule.every(1).minutes.do(sensor)
# scheduler = BackgroundScheduler(daemon=True)
# # Run every minute at 22 o'clock a day job Method
# scheduler.add_job(sensor, 'cron', hour=14, minute='*/31')
# # Run once a day at 22 and 23:25 job Method
# #scheduler.add_job(job, 'cron', hour='22-23', minute='25', args=['job2'])

# scheduler.start()

# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)

sched = BackgroundScheduler(daemon=True)
 # #if SCHEDULER_SERVICE == 1:
# sched.add_job(sensor,'interval',seconds=10)
sched.add_job(sensor, 'interval', seconds=10, start_date='2020-06-23 15:25:00')
# sched.add_job(main_system,'interval',seconds=int(TRAINING_SCHEDULER_TIME_INTERVAL),id='my_job_id_1')
sched.start()
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

##for a specific date 
# The job will be executed on November 6th, 2009
#exec_date = date(2009, 11, 6)

# Store the job in a variable in case we want to cancel it
#job = sched.add_date_job(my_job, exec_date, ['text'])
if __name__ == "__main__":
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)
        
    
