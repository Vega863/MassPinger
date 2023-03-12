import threading
from time import sleep
import os
from getpass import getpass

__Creator__ = ('Brigade Anti-420 !!#7274, !! Warnohe !!#5854')
__Github__ = 'https://github.com/Vega863'
__discord__ = 'https://discord.io/Vega863'

banner = """
███╗   ███╗ █████╗ ███████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║███████╗███████╗██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║╚════██║██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║███████║██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝v1.2
                        https://discord.io/Vega863


"""

try:
    import requests
except:
    os.system("pip install requests")
try:
    from pystyle import *
except:
    os.system("pip install pystyle")


def nuke(usertoken, message_Content, channelID, nb,sp):
    if threading.active_count() <= 100:
        t = threading.Thread(target=None, args=(usertoken, ))
        t.start()

    headers = {'Authorization': usertoken}
    print(f"\n[Sent a Message to : {channelID} channel !] : ")
    try:
        message = 0
        a = 0
        failnb = 0
        totalfailnb = 0
        for i in range(nb):
            response = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages',
                                     headers=headers,
                                     data={"content": f"{message_Content}"})
            sleep(sp)
            if response.status_code == 200:

                if a ==1:
                    message += 1
                    print("                                                                                              ",end="")
                    print(Colors.green + f"\x1B[F\t[!] Messaged Send : {message}", end="\r")
                    a=0
                else:
                    message += 1
                    print(Colors.green + f"\t[!] Messaged Send : {message}", end="\r")

            else:   
                if a == 1:
                    failnb += 1
                    totalfailnb += 1
                    print(Colors.red+"\tError sending message. Status code: ",
                          response.status_code,f" x{failnb}",end="\r")
                    
                else:
                    failnb = 1
                    totalfailnb += 1
                    print(Colors.red+"\n\tError sending message. Status code: ",
                          response.status_code,f" x{failnb}",end="\r")   
                    a=1         

    except Exception as error:
        print(
            Colors.red + f"\t[!] The following error has been encountered and is being ignored: {error}]")
        sleep(5)
        exit()

    print(Colors.green + f"\tTotal message send : {message}                                                                        ")
    print(Colors.red + f"\tTotal message failed to send : {totalfailnb}")
    input(Colors.white+"Programme end\nYou can close this windows")


def nukee(usertoken, message_Content,sp):
    if threading.active_count() <= 100:
        t = threading.Thread(target=None, args=(usertoken, ))
        t.start()

    headers = {'Authorization': usertoken}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels",
                              headers={'Authorization': usertoken}).json()
    print("\n[+] Sent a Message to all available friends")
    message = 0
    a=0
    failnb = 0
    totalfailnb = 0
    for channel in channelIds:
        try:
            response = requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                                     headers=headers,
                                     data={"content": f"{message_Content}"})
            sleep(sp)
            if response.status_code == 200:
                if a ==1:
                    message += 1
                    print("                                                                                              ",end="")
                    print(Colors.green + f"\x1B[F\t[!] Messaged ID: "+channel['id'], end="\r")
                    a=0
                else:
                    message += 1
                    print(Colors.green + f"\t[!] Messaged ID: "+channel['id'], end="\r")

            else:   
                if a == 1:
                    failnb += 1
                    totalfailnb += 1 
                    print(Colors.red+"\tError sending message. Status code: ",
                          response.status_code,f" x{failnb}",end="\r")
                    
                else:
                    failnb = 1
                    totalfailnb += 1
                    print(Colors.red+"\n\tError sending message. Status code: ",
                          response.status_code,f" x{failnb}",end="\r")   
                    a=1 
        except Exception as e:
            print(
                Colors.red + f"\t[!]The following error has been encountered and is being ignored: {e}]")
            sleep(5)
            exit()

    print(Colors.green + f"\tTotal message send : {message}                                                                     ")
    print(Colors.red + f"\tTotal message failed to send : {totalfailnb}")
    input(Colors.white+"Programme end\nYou can close this windows")


def invalidnum():
    print(Colors.red + ' [' + Colors.white + '!' + Colors.red + '] ' +
          Colors.white + "\ainvalid number")
    sleep(2)


def setup():
    white = Colors.white
    print(Colors.red + (Center.XCenter(banner)))
    token = str(getpass(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                      white + "Enter your discord token : "))
    message = str(input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                        white + "Enter your message you want to spam : "))
    
    while True :
        sleep = str(input(Colors.red + " [" + white + "?" + Colors.red + "]" +
                          white + " How message per second (example : 0.4): ")) 
        try:
            sleep = float(sleep)
            break
        except:
            invalidnum()
            pass



    banner2 = Colors.yellow + " [" + white + ">" + Colors.yellow + "]" + Colors.white + " 1 : Spam all channel with 1 message\n" + \
        Colors.yellow + " [" + white + ">" + Colors.yellow + "]" + \
        Colors.white + " 2 : Spam only 1 channel but as many times as you want"
    print(banner2)
    while True:

        a = input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                  white + "What do you want ? : ")
        try:
            a = float(a)
            if a == 1 or a == 2:
                break
            else:
                invalidnum()
                pass
        except:
            invalidnum()
            pass

    if a == 2:
        while True:
            nombre = input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                           white + "How many time you want to spam ? : ")
            try:
                nombre = int(nombre)
                break
            except:
                invalidnum()
                pass

        while True:
            channel_id = input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                               white + "Enter the channel id : ")
            try:
                channel_id = int(channel_id)
                break
            except:
                invalidnum()
                pass

        nuke(token, message, channel_id, nombre,sleep)
    elif a == 1:
        nukee(token, message,sleep)


if __name__ == "__main__":
    setup()
