from selenium import webdriver
import time
import smtplib, ssl
import requests
import json
from datetime import date
import datetime

from selenium.common.exceptions import NoSuchElementException

available_slots = []

def check_available_api(pincode,age_group,dose):
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin'
    nextDay = date.today() + datetime.timedelta(days=1)
    date_param = nextDay.strftime('%d-%m-%Y')
    print("Checking For Slot for Date ", date_param)
    params = {"pincode": pincode, "date": date_param}
    res = requests.get(url, params)
    res_body = res.json()
    res_ses = res_body['sessions']
    for data in res_ses:
        if data['min_age_limit'] == age_group:
            global available_slots
            available_slots = data['slots']
            available_capacity_dose1 = data['available_capacity_dose1']
            available_capacity_dose2 = data['available_capacity_dose2']
            vaccine = data['vaccine']
            if dose == 1:
                if available_capacity_dose1 > 0:
                    return True
            else:
                if available_capacity_dose2 > 0:
                    return True
            return False
        else:
            return False


def send_email(sender_email,sender_password,receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    messageMain = "-----------Slot Available HURRY!!!!!!!!---"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, messageMain)




def run_code(pincode,age_group,dose,sender_email,sender_password,receiver_email):
    if check_available_api(pincode,age_group,dose):
        print("Slot Available, Sending Email")
        send_email(sender_email,sender_password,receiver_email)
        exit()
    else:
        print("Slot not Available, Re-running Script After 30 Sec")
        time.sleep(30)
        run_code(pincode,age_group,dose,sender_email,sender_password,receiver_email)


pincode = input("Enter pincode")
age_group = input("Enter Age Group [18 - for 18 above and 45 for 45 above]")
dose = input("Enter dose : 1 for Dose 1 and 2 for Dose 2")
sender_email = input("Enter sender's email")
sender_password = input("Enter sender's password")
receiver_email = input("Enter receiver's email")
run_code(pincode,age_group,dose,sender_email,sender_password,receiver_email)
