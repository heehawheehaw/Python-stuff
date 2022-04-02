import smtplib
sender = "md.ai.rayn@gmail.com"
receiver = "rashida.riona@gmail.com"
password = "RFqU2Vsk95P%2UVCcmnkk%cKP"
subject = "Email Testing"
body =  "I wrote an email :D"

#this is header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
try:
    server.login("md.ai.rayn@gmail.com","RFqU2Vsk95P%2UVCcmnkk%cKP")
    print("Logged in..")
    server.sendmail(sender,receiver,message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to send email!")