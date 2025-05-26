# freeathome/register_devices.py
import time
import requests
from requests.auth import HTTPBasicAuth

def register_device(device_id, device_type, display_name, base_url, password):
    url = f"{base_url}/fhapi/v1/api/rest/virtualdevice/00000000-0000-0000-0000-000000000000/{device_id}"
    payload = {
        "type": device_type,
        "properties":{
            "ttl": "-1",
            "displayname": display_name    
        }
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    auth = HTTPBasicAuth('installer', password)

    try:
        response = requests.put(url, json=payload, headers=headers, auth=auth, timeout=10)
        print(f"✅ {device_id} ({display_name}): {response.status_code} – {response.text}")
    except Exception as e:
       print(f"❌ Fehler bei {device_id}: {e}")