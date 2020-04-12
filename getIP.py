import time
import netifaces

t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
print(start_time)

interface = netifaces.ifaddresses('wlan0') # Needs to be wlan0 for rpi // en0 for MBP

print(interface[netifaces.AF_INET][0]['addr'])
