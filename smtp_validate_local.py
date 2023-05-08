# for upload file
import urllib.request

import sys
#
import os  
import json
import csv
import datetime
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# LINT BOT API
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot import LineBotApi, WebhookHandler
#from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from flask import Flask, request, abort
# LINEＢＯＴ　ＡＰＩ

 
from flask import Flask
#app = Flask(__name__)
#@app.route('/')
 #================= for send mail =================
print("api connect")
smtp_idx = 0
wsfail = ''
wsc = 1
with open('smtp.csv', 'r', newline='', encoding='utf-8') as input_file:
        reader = csv.reader(input_file)
        reader = csv.reader(input_file)
        for row in reader:
          
                wsUSER_ID = row[0]
                wssmtp = row[0]
    
                smtp_server = "smtp.office365.com"
                smtp_port = 587

 
                smtp_username = row[0]
                smtp_password = row[1]
                smtp_idx = smtp_idx + 1
                if wsfail == 'Y':
                    wserrmsg = ("第 " + str(smtp_idx) + "-"  "  登錄中 ：" +  smtp_username )
                #    print(wserrmsg)
                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()
                #    print("login " + str(smtp_idx) + " " + smtp_username )
                    server.login(smtp_username,       smtp_password)
                    time.sleep(0.5)
                    server.quit()
                    time.sleep(2)

                except :
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    print("Exception Type:===>", exc_type)
                    print("Exception Value:", exc_value)
                    print("Traceback Object:", exc_traceback)
           
                #    print("第 " + str(smtp_idx) + " 登錄失敗 ：" +  smtp_username )
                    wsfail = "Y"
                    wserrmsg = ("第 " + str(smtp_idx) + " 登錄失敗 ：" +  smtp_username  + " " + smtp_password )
                    print (wserrmsg)
                    try :
                        server.quit()
                    except :
                    #    print('server quit finish')    
                    #    wserrmsg = ("Server Quit Complete wait 2sec" )
                    #    print (wserrmsg)
                        time.sleep(2)
                    wserrmsg = ("sleep return " )
                    message = TextSendMessage(text=wserrmsg )
                    print (wserrmsg)     
                if wsfail == 'Y' : 
                    wserrmsg = ("continue " )
                    print (wserrmsg)       
                if wsc == 3 :
                    wserrmsg = ("第 " + str(smtp_idx) + "-"  + "  測試紀錄 ：" +  smtp_username )
                    print (wserrmsg)
                    wsc = 0

                time.sleep(2)
           
                wsc = wsc +1

                
