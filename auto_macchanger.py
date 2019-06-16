import os
import time
import random
os.system('clear')

print("""
              _        
  __ _ _   _| |_ ___  
 / _` | | | | __/ _ \ 
| (_| | |_| | || (_) |
 \__,_|\__,_|\__\___/ 
                     
 _ __ ___   __ _  ___ 
| '_ ` _ \ / _` |/ __|
| | | | | | (_| | (__ 
|_| |_| |_|\__,_|\___|
     _                                 
  ___| |__   __ _ _ __   __ _  ___ _ __ 
 / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|
| (__| | | | (_| | | | | (_| |  __/ |   
 \___|_| |_|\__,_|_| |_|\__, |\___|_|   
                        |___/           

""")
print("                      Script By : Engima D7ooM Al-kurdi")
print("                           Snapchat:@scorpion.egram")
request = input("You need tool to launch this tool you have tool(Y/N)?:")
if request == 'Y' or 'y':
    os.system('sudo apt-get install macchanger')
    time.sleep(2)
    print("tool been installed !")
    print ("Start To Change !")
if request == 'N' or 'n':
    print ("Start To Change !")
ready = input("if you ready type (Y):")
if ready == 'Y' or 'y':
    change = input("type of how many change mac address ?:")
    change = int(change)
    daqa = input('Type oF Change Mac Addres In Secend Example:60:')
    daqa = int(daqa)
    for i in range(change):
        print ("we are volcano greyy team !")
        time.sleep(daqa)
        daqa = int(daqa)
        os.system('ifconfig wlan0 down')
        os.system('macchanger --random wlan0')
        os.system('ifconfig wlan0 up')