from pythonping import ping
import time

t = time.localtime()
start_time = time.strftime("%H:%M:%S", t)
print(start_time)

rootIP = "192.168.1."

i = 1
while i <= 255:
    testIP = rootIP + str(i)
    sentPing = ping(testIP, count=4, timeout=0.25)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Time: " + current_time + " | IP: " + str(testIP) + " | Response: " + str(sentPing.rtt_avg_ms))
    i += 1
