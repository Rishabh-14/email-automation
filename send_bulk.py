import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For TLS
email = 'rishabhkharyal3@gmail.com'  # Replace with your email
password = 'Srikrishna@13'  # Replace with your password

# Email details
subject = 'Hello, this is a test email'
body = 'This is the body of the email.'
recipients = ['rishabhkharyal@gmail.com', 'sanjeevkharyal4@gmail.com']  # Replace with actual email addresses

# Create server object with SSL option
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Start TLS encryption

# Login to email
server.login(email, password)

# Loop through each recipient
for recipient in recipients:
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.sendmail(email, recipient, msg.as_string())

# Quit the server
server.quit()
