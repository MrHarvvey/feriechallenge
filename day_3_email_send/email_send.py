import pandas
import os
import glob
import time
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib

#imporing environment variables to connect with email

try:
    login = os.getenv('EMAIL_LOGIN')
    password = os.getenv('EMAIL_PASS')
except Exception as e:
    print(f'You need to add environment variables EMAIL_LOGIN and EMAIL_PASS. Error: {e}')

#checking connection with your email server

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(login, password)
except Exception as e:
    print(f'Something went wrong: {e}')

#importing CSV file

try:
    df = pandas.read_csv('Untitled 1.csv')
except Exception as e:
    print(f'incorrect data download from excel file{e}')

#changing .png file in scrit location to name and surname

def change_attachment_name(name, surname):
    try:
        filename = glob.glob('*.png')[0]
        os.rename(filename, f'{name}_{surname}.png')
    except Exception as e:
        print(f'File does not exist{e}')

#sending content

def sending_email(html):
    for i in range(0, len(df['imie_nazwisko'])):
        imie_nazwisko = df['imie_nazwisko'][i]
        first, last = imie_nazwisko.split()
        email = df['email'][i]
        message = f'Hi {first}! it’s file generated for you'
        change_attachment_name(first, last)
        msg = MIMEMultipart()
        img_data = MIMEImage(open(glob.glob('*.png')[0], 'rb').read())
        img_data.add_header('Content-Disposition', "attachment; filename= %s" % glob.glob('*.png')[0])
        msg.attach(img_data)
        messege1 = MIMEText(message, 'plain')
        html1 = MIMEText(html, 'html')
        msg.attach(messege1)
        msg.attach(html1)
        msg['Subject'] = 'Your image'
        server.sendmail(login, email, msg.as_string())
        time.sleep(2)
    server.quit()


html = """
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""


sending_email(html)



