import requests
token =""
header={
    'access-token': token
}
dailyCoCoUrl = 'https://cococloudapi.xyz/api/user/checkin'

res = requests.get(dailyCoCoUrl,headers=header)
text =res.content.decode('unicode-escape')
print(text)
query={
        'chat_id': '711796280',
        'text': text}
requests.get("https://api.telegram.org/bot1865904487:AAHMzMIeRkyUOVrSuwMBXEgGQJM-XCWQx0I/sendMessage",params=query)