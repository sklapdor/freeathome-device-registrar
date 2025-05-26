import sys
import time
from freeathome.register_devices import register_device

if len(sys.argv) != 4:
    print("Usage: python main.py <devices_file> <accesspoint_url> <installer_password>")
    print("Example: python main.py devices.txt http://192.168.1.204 meinPasswort123")
    sys.exit(1)

devices_file = sys.argv[1]
base_url = sys.argv[2]
password = sys.argv[3]

with open(devices_file, encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) != 3:
            print(f"⚠️ Zeile übersprungen wegen ungültigem Format: {line.strip()}")
            continue
        device_id, device_type, display_name = map(str.strip, parts)
        register_device(device_id, device_type, display_name, base_url, password)
        time.sleep(2)