import shutil
import psutil

du = shutil.disk_usage("/")
print(du)
print(f"Total: {du.total / (1024 ** 3):.2f} GB")
print(f"Used: {du.used / (1024 ** 3):.2f} GB")
print(f"Free: {du.free / (1024 ** 3):.2f} GB")
print(f"Percentage used: {du.used / du.total * 100:.2f}%")

psutil.cpu_percent(0.1)
for i in range(10):
    print(f"CPU usage at {i+1} seconds: {psutil.cpu_percent(interval=1)}%")

print(f"CPU count: {psutil.cpu_count(logical=True)}")
print(f"Memory usage: {psutil.virtual_memory().percent}%")
print(f"Swap usage: {psutil.swap_memory().percent}%")
