from flask import request
from app import app, celery
import tasks


@app.route('/send_email/', methods=['POST'])
def send_email():
    data = request.json
    task = tasks.send_email.delay(data)
    return {'message': 'Email is being sent', 'task_id': str(task.id)}


@app.route('/send_sms/', methods=['POST'])
def send_sms():
    data = request.json
    task = tasks.send_sms.delay(data)
    return {'message': 'SMS is being sent', 'task_id': str(task.id)}
