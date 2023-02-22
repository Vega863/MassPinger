import requests
import threading
from colorama import Fore
from time import sleep
import pystyle
from pystyle import *
import os


__Creator__ = ('Brigade Anti-420 !!#7274, !! Warnohe !!#5854')
__Github__ = 'https://github.com/Vega863'
__discord__ = 'https://discord.io/Vega863'

banner = """
███╗   ███╗ █████╗ ███████╗███████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║███████╗███████╗██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║╚════██║██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║███████║██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝v1.0
                        https://discord.io/Vega863


"""


def nuke(usertoken, message_Content, channelID, nb):
    if threading.active_count() <= 100:
        t = threading.Thread(target=None, args=(usertoken, ))
        t.start()

    headers = {'Authorization': usertoken}
    print(f"\n[Sent a Message to : {channelID} channel !")
    try:
        for i in range(nb):
            requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages',
                          headers=headers,
                          data={"content": f"{message_Content}"})
            sleep(0.4)
        print(f"\t[{Fore.LIGHTGREEN_EX }!] Messaged ID: {channelID}")
    except Exception as error:
        print(
            f"\t[{Fore.LIGHTRED_EX }!] The following error has been encountered and is being ignored: {error}")


def nukee(usertoken, message_Content):
    if threading.active_count() <= 100:
        t = threading.Thread(target=None, args=(usertoken, ))
        t.start()

    headers = {'Authorization': usertoken}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels",
                              headers={'Authorization': usertoken}).json()
    print("\n[+] Sent a Message to all available friends")
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                          headers=headers,
                          data={"content": f"{message_Content}"})
            print(f"\t[{Fore.LIGHTGREEN_EX }!] Messaged ID: "+channel['id'])
            sleep(0.4)
        except Exception as e:
            print(
                f"\t[{Fore.LIGHTRED_EX }!]The following error has been encountered and is being ignored: {e}")


def setup():
    white = Col.white
    print(Colors.red + (Center.XCenter(banner)))
    token = str(input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                      white + "Enter your discord token : "))
    message = str(input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                        white + "Enter your message you want to spam : "))
    banner2 = '''''' + Colors.yellow + ''' [''' + white + '''>''' + Colors.yellow + ''']''' + Colors.white + '''1 : Spam all channel with 1 message\n''' + \
        Colors.yellow + ''' [''' + white + '''>''' + Colors.yellow + ''']''' + \
        Colors.white + '''2 : Spam only 1 channel but as many times as you want'''
    print(banner2)
    a = input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
              white + "What do you want ? : ")
    try:
        a = int(a)
    except:
        print(Colors.red + ' [' + white + '!' + Colors.red + '] ' +
              white + "invalid number")
        sleep(2)
        os.system("cls")
        setup()
    if a == 2:
        nombre = input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                       white + "How many time you want to spam ? : ")
        try:
            nombre = int(nombre)
        except:
            print(Colors.red + ' [' + white + '!' + Colors.red + '] ' +
                  white + "invalid number")
            sleep(2)
            os.system("cls")
            setup()
        channel_id = input(Colors.red + ' [' + white + '?' + Colors.red + '] ' +
                           white + "Enter the channel id : ")
        try:
            channel_id = int(channel_id)
        except:
            print(Colors.red + ' [' + white + '!' + Colors.red + '] ' +
                  white + "invalid number")
            sleep(2)
            os.system("cls")
            setup()

        nuke(token, message, channel_id, nombre)
    elif a == 1:
        nukee(token, message)


if __name__ == "__main__":
    setup()
