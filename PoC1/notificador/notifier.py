import smtplib
from flask_restful import Resource
from flask import request

sender = "Clinica ABC-Notifier <notifier@clinica-abc.com>" 
receivers = ['Anderson Santamaria <andersonsantamaria3@gmail.com>', 
    'Miguel Duque <mduquem1@gmail.com>',
    'Andres Lopez <am.lopezr1@uniandes.edu.co>', 
    'Marco Duran <ma.duran13@uniandes.edu.co>', 
    'Juan Navarro <js.navarro87@uniandes.edu.co>'
    ]

def get_email(api, status_code, description):  
    subject = "Notification error on API " + api + " - " + str(status_code)
    
    own_message = """Hi! Team<br/> <br/> 
The API <b>%s</b> has suffered the following error:
<br/> <br/>
<b>status code:</b> %s
<br/>
<b>description:</b> %s
<br/> <br/>
Please review the issue.
""" % (api, status_code, description)

    email = """From: %s 
To: %s 
MIME-Version: 1.0 
Content-type: text/html 
Subject: %s 
%s
""" % (sender, receivers, subject, own_message)
    return email

def send_notification_error(email, smtp_password):
    try: 
        s = smtplib.SMTP(host='smtp.mailgun.org', port=587)
        s.starttls()
        s.login("postmaster@sandbox5a390ccc8a52448fa5a7f8c6d603e025.mailgun.org", smtp_password)
        s.sendmail(sender, receivers, email) 
        print("email sent") 
    except Exception as e: 
        print(e)
        print("Error: the message could not be sent. Check that sendmail is installed on your system")

class VistaNotifier(Resource):
    def post(self):
        email = get_email(str(request.json["api"]), str(request.json["status_code"]), str(request.json["description"]))
        send_notification_error(email, str(request.json["smtp_password"]))
        return "email sent.", 200