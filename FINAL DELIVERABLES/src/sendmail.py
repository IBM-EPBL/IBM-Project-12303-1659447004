import sendgrid
from sendgrid.helpers.mail import Mail
import configparser
config = configparser.ConfigParser()
import base64
config.read('mail.env')
# APIKEY = config.get('API', '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'
api = sendgrid.SendGridAPIClient('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')
FROM_EMAIL = 'rakshan486@gmail.com'
def sendemail(user,type):
    TO_EMAIL = user
    if type == 'Account_creation':
        mail = Mail(from_email=FROM_EMAIL,to_emails=TO_EMAIL,subject='Account Created successfully',html_content='<strong>Account created Successfully</strong>')
    if type == 'complaint_creation':
        mail = Mail(from_email=FROM_EMAIL,to_emails=TO_EMAIL,subject='Complaint Created successfully',html_content='<strong>Compliant created Successfully</strong>')
    response = api.send(mail)
    print(response.status_code)
    print(response.headers)    

def forget_password_mail(user,otp):
    TO_EMAIL = user
    mail = Mail(from_email=FROM_EMAIL,
            to_emails=TO_EMAIL,
            subject='Your Customer care Passowrd reset request',
            html_content="<h2 style='text-align:center;'>Your One Time Password</h2><br><h1><strong style='text-align:center;'>"+str(otp)+"</strong></h1>")
    response = api.send(mail)
    print(response.status_code)
    print(response.headers)

def updated_password_mail(user):
    TO_EMAIL = user
    mail = Mail(from_email=FROM_EMAIL,
            to_emails=TO_EMAIL,
            subject='Your Password reset successfully.',
            html_content="<h2 style='text-align:center;'>Your Password Reset Successfully.</h2>")
    response = api.send(mail)
    print(response.status_code)
    print(response.headers)

def solve_mail(user,who):
    SUB = ''
    HC = ''
    if who == 'user':
        SUB='Your Problem has been solved'
        HC="<h2 style='text-align:center;'>Your Complaint is solved.you have any problems complaint us we have solve</h2>"
    else:
        SUB='AGENT ALLOTMENT'
        HC="<h2 style='text-align:center;'>Your Complaint is proccessing.Now we have agent alloted your problem solve in two days.</h2>"
    TO_EMAIL = user
    mail = Mail(from_email=FROM_EMAIL,to_emails=TO_EMAIL,subject=SUB,html_content=HC)
    response = api.send(mail)
    print(response.status_code)
    print(response.headers)