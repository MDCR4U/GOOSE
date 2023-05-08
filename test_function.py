import openai
import os
import urllib.request



import requests
import http.client
import json


import requests
import json

# 設定Line Bot的Channel Access Token和Channel Secret
channel_access_token = "gd2k8snxpn3PP+nC+spxDIgQF6ZTtjfS/vHmqOIEJ8W/B1bryahPh61EfFIepnHqfjTQ4zhc29120TvtHVjk4dMB5vkrJFtvcjO07389gomlkggI/rMJCoid9PCCr6O3v0dTY2R3n4FFA6IMr1D5twdB04t89/1O/w1cDnyilFU="
channel_secret = "82ab0090dc70c5f7d3a6c62fb1e09eb8"

# 設定推送訊息的URL
url = "https://api.line.me/v2/bot/message/push"

# 設定推送的消息
payload = {
    #"to": "U65614b139436a7af7d95a8fba65611d3",
    "to": "Cdc32534e703af48f09c1979ae0105999",
    "messages": [
        {
            "type": "text",
            "text": "你好，這是一條來自Line Bot的訊息！"
        }
    ]
}

# 設定Header，包括Channel Access Token和Content-Type
headers = {
    "Authorization": "Bearer " + channel_access_token,
    "Content-Type": "application/json"
}

# 發送POST請求，推送消息
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 列印回應結果
print(response.content)

exit ()


url ="https://mdcgenius.000webhostapp.com/admin/key.json" #+ wjson_file #http://www.abc.com/cust.json"
#url ="https://mdcgenius.000webhostapp.com/json/c000.json" #+ wjson_file #http://www.abc.com/cust.json"
print(url)
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
js_dta = json.loads(data)
image_url  = js_dta["line_token"]  
print(image_url)
exit() 
#gpt_token           = loaded_data["gptkey"]


wsmsg = "myjson" 
wjson_file = wsmsg + ".json"
# 讀取 JSON 檔案
with open("cbd.json" , "r") as f:
        js_dta = json.load(f)
 
print ("get cbd7.json  complete")
print ("background " + js_dta["image"] )

background_url  = js_dta["image"]                           #"https://i.ibb.co/mJfp6Nf/background.png"  #https://ibb.co/0BZHztf"
url_top_left    = js_dta["url_top_left"]                             #"https://www.youtube.com/watch?v=0kOpOqHuiGo"
url_top_right   = js_dta["url_top_right"]                            #"https://www.youtube.com/watch?v=XFvgYYHvcfE"
url_left_down   = js_dta["url_left_down"]                            #"https://www.youtube.com/watch?v=iOu5DwEQaJE"
url_right_down1 = js_dta["url_right_down1"]                          #"https://www.youtube.com/watch?v=R9cx3kgwWD0"
url_right_down2 = js_dta["url_right_down2"]                          #"https://www.youtube.com/watch?v=DAlIup87Aso&t=26s"
alt_text = js_dta ["alttxt"]  
                                 #"CBD"
base_width = js_dta["base_width"] 
base_height = js_dta["base_height"]   #2000

p1_x = js_dta["p1_x"] 
p1_y = js_dta["p1_y"]                 #0
p1_width = js_dta["p1_width"]         #1000
p1_height = js_dta["p1_height"]        #1000
    
p2_x = js_dta["p2_x"]                 #1000
p2_y = js_dta["p2_y"]                 #0
p2_width = js_dta["p2_width"]         #1000
p2_height = js_dta["p2_height"]       #1000
    
p3_x = js_dta["p3_x"]                 #0
p3_y = js_dta["p3_y"]                  #1000
p3_width = js_dta["p3_width"]         #1000
p3_height = js_dta["p3_height"]       #1000
 
p4_x = js_dta["p4_x"]                 #1000
p4_y = js_dta["p4_y"]                 #1000
p4_width = js_dta["p4_width"]         #1000
p4_height = js_dta["p4_height"]       #500
    
p5_x = js_dta["p5_x"]                 #1000
p5_y = js_dta["p5_y"]                 #1500
p5_width = js_dta["p5_width"]         #1000
p5_height = js_dta["p5_width"]        #500


print(p5_height)