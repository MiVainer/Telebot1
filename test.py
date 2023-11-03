import datetime
import os
import psutil
from subprocess import check_output

a = check_output(args ='cat /proc/cpuinfo', shell = True)
print(a)

b = psutil.getloadavg()
b = list(b)
print(b[0:3])

c = psutil.disk_usage('/')
print(c)
c = list(psutil.disk_usage('/'))
print(c)
c = f'Диск занят на - {c[3]} %, доступно {int(c[2]/1024/1024/1024)} Гб'

print(c)

e = check_output(args='uptime -p', shell=True)
print(e)