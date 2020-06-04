import os
basedir = os.path.abspath(os.path.dirname(__file__))#treat this file as a native citizen in this OS.When in Rome, do as Romans do.

#Windows = Documents\codingtemple-may2020\week5\in-class\config.py

#create our object that will put everything together for us
class Config():
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you will never guess...'  #call on this to create encrypton key for our forms; adds security to form submission.
    
    # os.environ.get means go into the terminal and find an environment variable called SECRET KEY and use it. Otherwise, use this string and create a secret key from that (string will be taken out when put into production because we only want it to run when SECRET KEY is present)

    #Has be to in all caps otherwise when we go to create our database it won't do anything.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Tell Flask what mail server it should be communicating with and sending information from (Sendgrid)

    #set up mail server
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('SENDGRID_API_KEY')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    # Twilio article how to send an email in Sendgrid for this info

