import pika
import numpy as np
import smtplib
from email.message import EmailMessage
import os, json
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv("FROM_EMAIL")
EMAIL_PWD = os.getenv("EMAIL_PWD")

print(FROM_EMAIL, EMAIL_PWD)
def generate_otp():
    return np.random.randint(1000, 9999)

def send_otp(user_name, to_email):
    otp = generate_otp()
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(FROM_EMAIL, EMAIL_PWD)

            msg = EmailMessage()
            msg["Subject"] = "OTP Verification"
            msg["From"] = FROM_EMAIL
            msg["To"] = to_email

            msg.set_content(
                f"Hello {user_name},\n\n"
                f"We received a request to verify your email: {to_email}.\n"
                f"Your One-Time Password (OTP) is: {otp}\n\n"
                "Please enter this code to continue.\n\n"
                "Best regards,\n"
                "Suraj Gupta"
            )

            server.send_message(msg)
            print("OTP Sent Succefully...")
        return otp
    except Exception as e:
        import traceback
        print(f"Something went wrong to send otp! {str(e)}")
        traceback.print_exc()
        return None

def callback(ch, method, properties, body):
    message = body.decode()
    message = json.loads(message)
    user_name = message.get("user_name")
    email = message.get("email")

    otp = send_otp(user_name, email)
    print(otp)

params = pika.URLParameters("amqps://bvbfmndz:mg0thl9d08gagtu2oQSwIU7JDRXQjsPL@rabbit.lmq.cloudamqp.com/bvbfmndz")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="my_queue")
channel.basic_consume(queue="my_queue", on_message_callback=callback, auto_ack=True)
print("consumer ready to consume RabbitMQ queue messages")

channel.start_consuming()