# 🛡️ Host-Based Intrusion Detection System (HIDS)

## 📌 Project Overview
This project is a lightweight **Host-Based Intrusion Detection System (HIDS)** built in Python. It simulates a real-time security monitoring environment where the system actively watches server logs, detects suspicious behavior (specifically SSH Brute Force attacks), and triggers alerts based on predefined security thresholds.

The goal of this project was to understand the core logic behind SIEM (Security Information and Event Management) tools and how signature-based detection works at the code level.

## 🎯 Key Features
* **Real-Time Log Monitoring:** The script uses a "tail" approach to read log files continuously as they are written.
* **Signature Detection:** Uses **Regular Expressions (RegEx)** to parse unstructured log data and identify specific threat patterns (e.g., "Failed password").
* **Threshold Logic:** Implements a state-tracking mechanism to distinguish between user error and malicious intent (e.g., flagging an IP only after 5 failed attempts).
* **Attack Simulation:** Includes a custom "Chaos Script" that generates realistic SSH logs and injects random brute-force bursts to test the detector.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Concepts:** File I/O, Regular Expressions (RegEx), Dictionary/Hash Map Data Structures, Anomaly Detection Logic.
* **Environment:** Visual Studio Code (Split Terminal for Simulation).

## 📸 Screenshots
**1. The Attack & Defense in Action**
*Left: The generator creating traffic. Right: The IDS detecting the Brute Force burst.*

![Insert Screenshot of your VS Code Split Terminal Here]
*(Note: Take a screenshot of your VS Code window showing the "ALERT" messages and paste it here)*

## 🚀 How It Works
The project consists of two main components acting in a Producer-Consumer relationship:

1.  **The Generator (`log_generator.py`):**
    * Creates a dummy `server_logs.txt` file.
    * Writes normal "background noise" (valid logins).
    * Randomly triggers "attack bursts" (rapid failed logins from a single IP).

2.  **The Detector (`ids_detector.py`):**
    * Tails the `server_logs.txt` file in real-time.
    * Parses every line looking for the "Failed password" signature.
    * Extracts IP addresses using RegEx.
    * Maintains a count of failures per IP.
    * Triggers an **ALERT** if failures > 5.

## 💻 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/simple-python-ids.git](https://github.com/yourusername/simple-python-ids.git)
    ```
2.  **Open two terminal windows.**
3.  **Start the Log Generator (Terminal 1):**
    ```bash
    python log_generator.py
    ```
4.  **Start the IDS (Terminal 2):**
    ```bash
    python ids_detector.py
    ```
5.  **Watch the magic:** Wait for the generator to trigger an attack and watch the IDS flag it.

## 🔮 Future Improvements
* **Geolocation:** Integrate an API to resolve attacker IPs to physical locations (Country/City).
* **Email Alerts:** Add SMTP functionality to send an email notification when an attack is detected.
* **Blocking:** Integrate with system firewalls (like `iptables`) to automatically ban the malicious IP.