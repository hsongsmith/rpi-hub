import time
import netifaces

t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
print(start_time)

interface = netifaces.ifaddresses('wlan0')

print(interface[netifaces.AF_INET])
