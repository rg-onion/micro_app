from app import celery
import email_service
import sms_service


@celery.task
def send_email(data):
    email_service.send_email(data['email'], data['subject'], data['message'])


@celery.task
def send_sms(data):
    sms_service.send_sms(data['phone'], data['message'])
