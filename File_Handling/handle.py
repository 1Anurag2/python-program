import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    from_password = "your_email_password"

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
        session.starttls()  # Enable security
        session.login(from_email, from_password)  # Login with mail_id and password
        text = message.as_string()
        session.sendmail(from_email, to_email, text)
        session.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
def generate_report():
    # Dummy report content
    report_content = "This is your daily report content."
    return report_content
def job():
    subject = "Daily Report"
    body = generate_report()
    to_email = "recipient_email@example.com"
    send_email(subject, body, to_email)

schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
