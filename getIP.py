import time
import netifaces

t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
print(start_time)

print(netifaces.interfaces())

print(netifaces.ifaddresses('wlan0'))
