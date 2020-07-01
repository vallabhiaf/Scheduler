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
from CONSTANTS import TRAINING_SCHEDULER_TIME,PREDICTION_SCHEDULER_TIME,TRAINING_SCHEDULER_UNIT,TRAINING_SCHEDULER_TIME_INTERVAL,PREDITCION_SCHEDULER_UNIT,PREDICTION_SCHEDULER_TIME_INTERVAL







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
    


sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=int(PREDICTION_SCHEDULER_TIME_INTERVAL),start_date=PREDICTION_SCHEDULER_TIME)
sched.add_job(main_system, 'interval', seconds=int(TRAINING_SCHEDULER_TIME_INTERVAL), start_date=TRAINING_SCHEDULER_TIME)
# sched.add_job(main_system,'interval',seconds=int(TRAINING_SCHEDULER_TIME_INTERVAL),id='my_job_id_1')
sched.start()
#
if __name__ == "__main__":
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=False)
        
    