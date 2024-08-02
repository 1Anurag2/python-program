export EMAIL_USER="your_email@example.com"
export EMAIL_PASS="your_email_password"
import os

def send_email(subject, body, to_email):
    from_email = os.getenv('EMAIL_USER')
    from_password = os.getenv('EMAIL_PASS')

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
