from cfenv import AppEnv
import os
env = AppEnv()



# DB defaults
HANA_DB_ADDRESS = 'zeus.hana.prod.eu-central-1.whitney.dbaas.ondemand.com'
HANA_DB_PORT = 30755
HANA_DB_USER = 'DB_USER'
HANA_DB_PASSWORD = 'Test1234'
HANA_DB_CERT = ''
TRAINING_SCHEDULER_UNIT='seconds'
TRAINING_SCHEDULER_TIME_INTERVAL=86400
TRAINING_SCHEDULER_TIME='2020-06-24 22:00:00'

PREDITCION_SCHEDULER_UNIT='seconds'
PREDICTION_SCHEDULER_TIME_INTERVAL=70
PREDICTION_SCHEDULER_TIME='2020-06-24 21:00:00'



if os.getenv('VCAP_APPLICATION'):
    print("Getting values from Cloud Environment")
    TRAINING_SCHEDULER_UNIT=os.getenv('TRAINING_SCHEDULER_UNIT')
    TRAINING_SCHEDULER_UNIT = TRAINING_SCHEDULER_UNIT.strip()
    TRAINING_SCHEDULER_UNIT= TRAINING_SCHEDULER_UNIT.lower()
    TRAINING_SCHEDULER_TIME_INTERVAL=os.getenv('TRAINING_SCHEDULER_TIME_INTERVAL')
    if TRAINING_SCHEDULER_UNIT == 'hour':
        TRAINING_SCHEDULER_TIME_INTERVAL =int(TRAINING_SCHEDULER_TIME_INTERVAL) *60 *60
   
    PREDITCION_SCHEDULER_UNIT=os.getenv('PREDITCION_SCHEDULER_UNIT')
    PREDITCION_SCHEDULER_UNIT = PREDITCION_SCHEDULER_UNIT.strip()
    PREDITCION_SCHEDULER_UNIT = PREDITCION_SCHEDULER_UNIT.lower()
    PREDICTION_SCHEDULER_TIME_INTERVAL=os.getenv('PREDICTION_SCHEDULER_TIME_INTERVAL')
    if PREDITCION_SCHEDULER_UNIT == 'hour':
        PREDICTION_SCHEDULER_TIME_INTERVAL =int(PREDICTION_SCHEDULER_TIME_INTERVAL) *60 *60
    SCHEDULER_SERVICE=os.getenv('SCHEDULER_SERVICE')
    TRAINING_SCHEDULER_TIME=os.getenv('TRAINING_SCHEDULER_TIME')
    PREDICTION_SCHEDULER_TIME=os.getenv('PREDICTION_SCHEDULER_TIME')



    ## DB Configurations
    hanaDBService = env.get_service(label='hana')
    HANA_DB_ADDRESS = hanaDBService.credentials['host']
    # print(HANA_DB_ADDRESS)
    HANA_DB_PORT = int(hanaDBService.credentials['port'])
    # print(HANA_DB_PORT)
    HANA_DB_USER = hanaDBService.credentials['user']
    # print(HANA_DB_USER)
    HANA_DB_PASSWORD = hanaDBService.credentials['password']
    # print(HANA_DB_ADDRESS)
    HANA_DB_CERT = hanaDBService.credentials['certificate']

