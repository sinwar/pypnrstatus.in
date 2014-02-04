import requests
import json

import datetime

def check_if_passengers_cnf(passengers):
    for passenger in passengers:
        if passenger['status'] != 'CNF':
            return False
    return True


def caluclate_timedelta(notification_frequency, notification_frequency_value):
    notification_frequency_value = int(notification_frequency_value)
    if notification_frequency == 'minutes':
        timedelta = datetime.timedelta(minutes=notification_frequency_value)
    elif notification_frequency == 'hours':
        timedelta = datetime.timedelta(hours=notification_frequency_value)
    elif notification_frequency == 'days':
        timedelta = datetime.timedelta(days=notification_frequency_value)
    return timedelta

def get_and_schedule_pnr_notification(pnr_notify):
    pnr_no = pnr_notify.pnr_no
    resp = requests.get('http://pnrapi.alagu.net/api/v1.0/pnr/%s'%pnr_no)
    resp = json.loads(resp.content)

    status = resp['status']
    data = resp['data']

    print data
    if resp.has_key('message'):
        return {'error': resp['message']}

    if data == {} and status == 'OK':
        return {'error': 'Something went wrong real bad! \nTry again later :)'}

    if status == "INVALID":
        return {'error': 'Invalid PNR Number!'}

    passengers = data['passenger']
    if data['chart_prepared'] or check_if_passengers_cnf(passengers):
        # The ticket is confirmed or chart prepared
        pass

    return {'pnr_no': pnr_no, 'passengers': passengers}


