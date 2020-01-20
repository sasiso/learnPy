from ptv.client import PTVClient
DEV_ID = '3000810'
API_KEY = '105EEA7920D3DD198687344A0824D49FC25588B6'
client = PTVClient(DEV_ID, API_KEY)
client.get_departures_from_stop(0, 1071)