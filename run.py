import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configuration
    sender_email = 'your_email@gmail.com'  # Your email address
    receiver_email = 'recipient_email@gmail.com'  # Recipient's email address
    password = 'your_password'  # Your email password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Daily Report'

    # Email body
    body = "This is your daily report email."

    msg.attach(MIMEText(body, 'plain'))

    # Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Schedule the email to be sent daily at a specific time
schedule.every().day.at("08:00").do(send_email)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
