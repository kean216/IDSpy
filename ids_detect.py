

import time
import re
import os

# Try to import requests, but don't crash if it's missing
try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Run: pip install requests")
    exit()

# CONFIGURATION
LOG_FILE = "server_logs.txt"
THRESHOLD = 5

def get_ip_location(ip):
    """
    Queries a free Geolocation API to find the Country of an IP.
    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=2)
        data = response.json()
        if data['status'] == 'success':
            return f"{data['city']}, {data['country']}"
        else:
            return "Unknown Location"
    except Exception as e:
        return "Location Lookup Failed"

def ids_main():
    # 1. Wait for the log file to exist
    if not os.path.exists(LOG_FILE):
        print(f"WAITING: {LOG_FILE} not found. Start the log_generator.py first!")
        while not os.path.exists(LOG_FILE):
            time.sleep(1)

    print(f"Monitoring {LOG_FILE} for NEW attacks...", flush=True)
    
    # 2. "Live Mode" - Jump to the end of the file immediately
    try:
        with open(LOG_FILE, "r") as f:
            f.seek(0, 2) # 0 bytes from the end (2)
            current_position = f.tell() # Save this position
    except FileNotFoundError:
        current_position = 0

    ip_counts = {} 

    try:
        while True:
            # Check if file exists (in case it gets deleted)
            if not os.path.exists(LOG_FILE):
                time.sleep(1)
                continue

            with open(LOG_FILE, "r") as file:
                # Go to where we last stopped reading
                file.seek(current_position)
                lines = file.readlines()
                current_position = file.tell() # Update position

            for line in lines:
                line = line.strip()
                if not line: continue

                if "Failed password" in line:
                    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                    
                    if ip_match:
                        ip = ip_match.group(1)
                        
                        # Count the failure
                        if ip in ip_counts:
                            ip_counts[ip] += 1
                        else:
                            ip_counts[ip] = 1

                        current_count = ip_counts[ip]

                        # --- ALERT LOGIC ---
                        if current_count == THRESHOLD:
                            print("\n-------------------------------------------")
                            print(f"🚨 CRITICAL ALERT: Brute Force Detected!")
                            print(f"❌ Suspect IP: {ip}")
                            print(f"❌ Failure Count: {current_count}")
                            
                            print("🌍 Locating...", end=" ", flush=True)
                            loc = get_ip_location(ip)
                            print(f"FOUND: {loc}")
                            print("-------------------------------------------\n")

                        elif current_count > THRESHOLD:
                            print(f"⚠️  Ongoing Attack from {ip}! (Count: {current_count})")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping IDS Detector.")

if __name__ == "__main__":
    ids_main()