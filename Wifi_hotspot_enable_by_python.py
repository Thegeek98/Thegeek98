# Wi-Fi Hostspot enabler for window
# Programmer :  Zin KO
# Date :        7.10.2020

import os
os.system('cls')
print('\n\n\n')
print('Burmese Geek Wifi Hostspot')
print('(c) 2020 Burmese Geek Group. All right reserved.')
print()

ssid = input("Please Enter Wi-Fi Name: ")
passwd = int(input("Please Give the Password: "))
cmd = '0'
while cmd !='3':
    print('1. Start Hotspot')
    print('2. Stop Hotspot')
    print('3. Exit')
    cmd = input('Please Enter Your Choice (1,2,3): ')
    if cmd == '1':
        print("Starting Wi-Fi Hotspot ..... ")
        os.system("netsh wlan set hostednetwork mode=allow ssid="+ ssid + " key=" +passwd )
        os.system("netsh wlan start hostednetwork")
    elif cmd == '2':
        print("Stoping Wi-Fi Hotspot ..... ")
        os.system("netsh wlan stop hostednetwork")
    elif cmd == '3':
        print("Exiting program .... ")
        exit()
    else:
        print("Bad input! Please try again (only 1,2,3)")
        os.system('pause')

