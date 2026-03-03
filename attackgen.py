import time
import random
from datetime import datetime

# CONFIGURATION
LOG_FILE = "server_logs.txt"
ATTACK_PROBABILITY = 0.1  # 10% chance to start an attack burst
MIN_ATTACK_ATTEMPTS = 5   # Minimum failures in a burst
MAX_ATTACK_ATTEMPTS = 15  # Maximum failures in a burst

# SAMPLE DATA
USERS = ["admin", "root", "user", "guest", "support", "jdoe", "msmith"]
IPS = [f"192.168.1.{i}" for i in range(10, 20)]  # "Safe" internal IPs
ATTACKER_IPS = ["45.33.22.11", "103.201.150.11", "221.192.11.80"] # "Scary" external IPs

def get_timestamp():
    """Generates a syslog-style timestamp (e.g., 'Oct 12 10:15:32')"""
    return datetime.now().strftime("%b %d %H:%M:%S")

def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{message}\n")
    print(f"LOGGED: {message.strip()}")

def generate_normal_traffic():
    """Simulates random valid or accidental failed logins"""
    timestamp = get_timestamp()
    user = random.choice(USERS)
    ip = random.choice(IPS)
    
    # 90% success rate for normal traffic
    if random.random() < 0.9:
        msg = f"{timestamp} server sshd[1234]: Accepted password for {user} from {ip} port 22 ssh2"
    else:
        msg = f"{timestamp} server sshd[1234]: Failed password for {user} from {ip} port 22 ssh2"
    
    write_log(msg)

def generate_attack_burst():
    """Simulates a brute force attack: fast failures from one IP"""
    timestamp = get_timestamp()
    target_user = "admin" # Attackers usually target admin/root
    attacker_ip = random.choice(ATTACKER_IPS)
    num_attempts = random.randint(MIN_ATTACK_ATTEMPTS, MAX_ATTACK_ATTEMPTS)
    
    print(f"\n--- ⚠️ STARTING ATTACK SIMULATION FROM {attacker_ip} ---\n")
    
    for _ in range(num_attempts):
        msg = f"{timestamp} server sshd[9999]: Failed password for {target_user} from {attacker_ip} port 22 ssh2"
        write_log(msg)
        time.sleep(0.2) # Fast burst, but not instant

    print(f"\n--- 🛑 ATTACK ENDED ---\n")

if __name__ == "__main__":
    print(f"Generating logs to {LOG_FILE}... (Press Ctrl+C to stop)")
    try:
        while True:
            if random.random() < ATTACK_PROBABILITY:
                generate_attack_burst()
            else:
                generate_normal_traffic()
            
            # Pause between log entries to mimic real-time traffic
            time.sleep(random.uniform(0.5, 2.0))
            
    except KeyboardInterrupt:
        print("\nStopping log generator.")