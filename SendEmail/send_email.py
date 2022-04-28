import smtplib # To connect to Gmail server
import ssl # Secure Socket Layer
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python"
sender_email = "rokyuto@gmail.com"
receiver_email = "viktorvalerievasenov6@gmail.com"
password = input("Enter a password: ")

# Build the email || Create Email object
message = EmailMessage()
message["From"] = sender_email 
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

# HTML Formated Body in the email
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html") # Add the html to the email

# Secure CONNECTION
context = ssl.create_default_context()

print("Sending email!")

# Connect SMPT with SSL and connect to the server
with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(sender_email, password) # login in the email account (sender_email) and server
    # Send Email     SENDER         Receiver     Message as String
    server.sendmail(sender_email, receiver_email, message.as_string())
print("SUCCESS")