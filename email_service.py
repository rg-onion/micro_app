import yagmail


def send_email(email, subject, message):
    yag = yagmail.SMTP('YourEmail', 'YourPassword')
    yag.send(email, subject, message)
