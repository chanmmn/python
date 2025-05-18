import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Office 365 SMTP server configuration
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587

# Your Office 365 credentials
USERNAME = 'yourusername@yourdomain.onmicrosoft.com'
PASSWORD = 'yourpassword'

# Email details
FROM_EMAIL = USERNAME
TO_EMAIL = 'youremail@gmail.com'
SUBJECT = 'Test Email from Office 365'
BODY = 'This is a test email sent using Office 365 SMTP server.'

# Create the email message
msg = MIMEMultipart()
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT
msg.attach(MIMEText(BODY, 'plain'))

# Send the email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')
finally:
    server.quit()