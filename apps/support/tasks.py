from config.celery import app
from apps.base.services import send


@app.task
def send_new_ticket_email(user_email, message):
    send(user_email, 'Dear admin, a new ticket has arrived', message)


@app.task
def send_update_ticket_email(user_email, message):
    send(user_email, 'Dear admin, the ticket update has arrived', message)


@app.task
def send_new_answer_email(user_email, message):
    send(user_email, 'Dear admin, a new answer has arrived', message)
