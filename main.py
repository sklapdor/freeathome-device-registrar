import getpass
import sys
import time
from freeathome.register_devices import register_device

if len(sys.argv) != 3:
    print("Usage: python main.py <devices_file> <accesspoint_url>")
    print("Example: python main.py devices.txt http://192.168.100.104")
    sys.exit(1)

devices_file = sys.argv[1]
base_url = sys.argv[2]
password = getpass.getpass("Please enter the installer password: ")

with open(devices_file, encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) != 3:
            print(f"⚠️ Zeile übersprungen wegen ungültigem Format: {line.strip()}")
            continue
        device_id, device_type, display_name = map(str.strip, parts)
        register_device(device_id, device_type, display_name, base_url, password)
        time.sleep(2)