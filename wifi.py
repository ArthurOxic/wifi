# wifi_scanner.py
import os
os.systen('clear')
os.systen('pip install jsons')
os.systen('pip install subprocess.run')
os.systen('pip install jsonlib')
os.systen('clear')
import subprocess
import json

def scan_wifi():
    cmd = "termux-wifi-scaninfo"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print("Error:", error.decode())
        return None

    wifi_data = json.loads(output)
    return wifi_data

def main():
    print("Scanning WiFi networks...")
    wifi_data = scan_wifi()
    if wifi_data:
        for wifi in wifi_data:
            print("SSID:", wifi["ssid"])
            print("BSSID:", wifi["bssid"])
            print("Signal Level:", wifi["rssi"])
            print("Frequency:", wifi["frequency_mhz"])
            print("-" * 30)

if __name__ == "__main__":
    main()
    