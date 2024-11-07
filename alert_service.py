import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration (replace these with your actual details)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "hindukaturi@gmail.com"
EMAIL_PASSWORD = "vwkr rneo jcvq mxtv"  # Use your app password here

def send_email_alert():
    try:
        # Email content defined inside the function
        subject = "Accident Alert"
        body = "An accident has been detected. Please take necessary action."

        # Set up the MIME structure
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS  # Send email to the same address or to another address
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the Gmail SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print("Alert email sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")

# Main function where the email is triggered
if __name__ == "__main__":
    send_email_alert()  # Call the function without arguments
