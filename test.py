import os
import psutil

print(psutil.getloadavg())
print(psutil.disk_usage('/dev/nvme0n1p2'))
print(psutil.version_info)
print(psutil.virtual_memory())