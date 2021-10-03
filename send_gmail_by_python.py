import smtplib

origin = """origin mail"""
password = """password"""
goal = """goal mail"""

def send_email(subject, msg):
    try :
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(origin, password)
        message = f'subject: {subject}\n\n{msg}'
        server.sendmail(origin, goal, message)
        server.quit()
        print("Success: Email send!")
    except:
        print("Email failed to send.")


subject = "the subject"
msg = "hello every one"

send_email(subject, msg)
