import boto3


def send_sms(phone, message):
    client = boto3.client('sns')
    response = client.publish(
        PhoneNumber=phone,
        Message=message
    )
    return response
