import openai
import os
import urllib.request



import requests
import http.client
wsftpflr  = 'http://mdcgenius.000webhostapp.com/'
userFolder = 'admin/'
smtp_idx = 123

if 1== 1:
    url = wsftpflr + userFolder.strip('\n') +  '/mail_counter.log'
    print ('=======' + url )
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            counter = int(content.strip())
    except urllib.error.URLError:
        counter = 0
    print ("counter =" + str(counter) + "##")
    #try:
    #    with open("mail_counter.log", "r", encoding="utf-8") as f:
    ##        counter = int(f.readline())
    #except FileNotFoundError:
    #    counter = 0
# 讀取SMTP發送記錄
    url = wsftpflr + userFolder.strip('\n') +  '/smtp_send_counter.log'

    print ('=======' + url )
    try:
        with urllib.request.urlopen(url) as response:
            smtp_idx = response.read().decode('utf-8')
            smtp_idx = int(content.strip())
    except urllib.error.URLError:
        smtp_idx = 0
    print("smtp idx =" + str(smtp_idx))

    exit()




try:
    conn = http.client.HTTPConnection(url)
    conn.request('POST', path, str(smtp_idx))
    response = conn.getresponse()
    if response.status != 200:
        print(f'Error: Unable to write to file: {response.reason}')
    conn.close()
except http.client.HTTPException as e:
    print(f'Error: Unable to write to file: {e}')




url = 'https://mdcgenius.000webhostapp.com/admin/smtp_send_counter.log' 
smtp_idx = 123

try:
    response = requests.post(url, data=str(smtp_idx))
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f'Error: Unable to write to file: {e}')
exit()


url = 'https://mdcgenius.000webhostapp.com/admin/smtp_send_counter.log' 
data = str(123)


try:
    req = urllib.request.Request(url, data.encode('utf-8'), method='PUT')
    urllib.request.urlopen(req)
except urllib.error.URLError:
    print('Error: Unable to write to file')  
exit()


url = 'https://mdcgenius.000webhostapp.com/key.txt'   #githuburl + "key.txt"
filename = 'key.txt'
urllib.request.urlretrieve(url, filename)
#取得 系統 KEY 

print("========================= " + url )
file = open('key.txt','r',encoding="utf-8")
xx=file.read()
print("##" + xx + "##")
exit() 
# 设置OpenAI API密钥
# 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
api_key = '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'  #os.environ['OPENAI_API_KEY']
print(api_key)
openai.api_key = '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'
# 撰寫輸入的提示語句
prompt = "請列舉出糖尿病患者的飲食禁忌："
prompt = "請列舉出MyDAILYCHOICE 公司的產品項目："

# 設定要求模型輸出的最大字數
max_tokens = 256

# 設定輸出結果的格式
model_engine = "text-davinci-002"

# 使用 OpenAI API 輸出模型預測的結果
output = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=0.5,
    n=1,
    stop=None,
)

# 從輸出結果中取得模型預測的文本內容
result = output.choices[0].text.strip()

# 輸出模型預測的結果
print(result)