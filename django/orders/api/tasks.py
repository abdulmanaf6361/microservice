from celery import shared_task
import requests

@shared_task
def send_email(email, total, name):
    try:
        response = requests.post("http://nginx/api/v1/emails/send/", data={
            "receiver": email,
            "subject": "Order Created",
            "body": f"Hello {name}, your order has been created. Total of: {total}. Thanks"
        })
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send email: {e}")
