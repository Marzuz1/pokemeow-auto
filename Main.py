import requests
import json
import time
from playsound import playsound

auth = '' #Put your Discord's Token here

channelid = '' #Put your channelid to play

def pb(channelid):
    headers = {
        'authorization': auth
        }
    payload1 = {
        'content' : "pb"
    }
    r1 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=payload1 ,headers=headers)

def gb(channelid):
    headers = {
        'authorization': auth
        }
    payload2 = {
        'content' : "gb"
    }
    r2 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=payload2 ,headers=headers)

def ub(channelid):
    headers = {
        'authorization': auth
    }
    payload3 = {
        'content' : "ub"
    }
    r3 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=payload3 ,headers=headers)

def mb(channelid):
    headers = {
        'authorization': auth
    }
    payload4 = {
        'content' : "mb"
    }
    r4 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=payload4 ,headers=headers)
    
def prb(channelid):
    headers = {
        'authorization': auth
    }
    payload5 = {
        'content' : "prb"
    }
    r5 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=payload5 ,headers=headers)

def khokho(channelid):
    headers = {
        'authorization': auth
    }
    purge = {
        'content' : "-purge all"
    }
    r11 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=purge ,headers=headers)

def throwball(channelid):
    headers = {
        'authorization': auth
    }
    purge = {
        'content' : ";p"
    }
    r2 = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=purge ,headers=headers)


def batdau(channelid):
    headers = {
        'authorization': auth
        }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages',headers=headers)
    message = json.loads(r.text)
    a = str(message)
    with open("test1.txt", "w", encoding="utf-8") as b:
        b.write(a)
    b.close()

    
   

    Common = "Common"
    Uncommon = "Uncommon"
    Rare = "Rare"
    SuperRare = "Super"
    Legendary = "Legendary"
    Shiny = "Shiny"
    with open("test1.txt", "r", encoding="utf-8") as b:
     if b.mode == "r":
        contest =  b.read()
        if Shiny in contest:
            print("Shiny <=====")
            prb(channelid)
            time.sleep(11.5)
            khokho(channelid)
            time.sleep(1)
            nole(channelid)
        elif Legendary in contest:
            print("Legendary <=====")
            mb(channelid)
            time.sleep(11)
            khokho(channelid)
            time.sleep(1)
            nole(channelid)
        elif SuperRare in contest:
            print("Super Rare")
            ub(channelid)
            time.sleep(10.5)
            khokho(channelid)
            time.sleep(1)
            nole(channelid)
        elif Rare in contest:
            print("Rare")
            pb(channelid)
            time.sleep(10)
            khokho(channelid)
            time.sleep(1)
            nole(channelid)
        elif Uncommon in contest:
            print("Uncommon")
            pb(channelid)
            time.sleep(9.5)
            khokho(channelid)
            time.sleep(1)
            nole(channelid)
        elif Common in contest:
            print("Common")
            pb(channelid)
            time.sleep(9)
            khokho(channelid)
            time.sleep(1)
            nole(channelid)
            
def checkcaptcha(captchadm, channelid):
    headers = {
    'authorization': auth
    }
    rr = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages',headers=headers)
    message2 = json.loads(rr.text)
    aa = str(message2)
    with open("test2.txt", "w", encoding="utf-8") as bb:
        bb.write(aa)
    bb.close()

    dm = "captcha!"
    with open("test2.txt", "r", encoding="utf-8") as bb:
     if bb.mode == "r":
        contest2 =  bb.read()
        if dm in contest2:
            #playsound('/Users/annb/Downloads/2000y.mp3')
            exit()

def main():
    captchadm = 0
    while captchadm == 0:
        batdau(channelid)
        checkcaptcha(captchadm, channelid)
main()


