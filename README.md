Host-Based Intrusion Detection System (HIDS)
A Python-based intrusion detection system utilizing a producer-consumer architecture to simulate and detect SSH brute-force attacks in real-time. Designed to demonstrate core Security Information and Event Management (SIEM) logic, this tool utilizes state-tracking and Regular Expressions (RegEx) to parse unstructured log data and flag malicious actors based on strict failure thresholds.

Installation
Clone the repository to your local machine. This project relies entirely on standard Python libraries, requiring no external dependencies or virtual environments.

git clone (https://github.com/kean216/IDSpy.git)


Usage
This project requires two terminal windows to run simultaneously, simulating an active server environment and the corresponding security monitor.

Terminal 1: Start the Log Generator
Generates background authentication noise and injects randomized brute-force bursts into a local server_logs.txt file.

Bash
python attackgen.py

Terminal 2: Start the IDS Monitor
Continuously tails the log file, parsing signatures and tracking IP failure counts in real time.

Bash
python ids_detector.py

Sample Output:


<img width="1800" height="291" alt="gitids" src="https://github.com/user-attachments/assets/349ed4a7-988e-4ed5-9a7c-4445da40c2f7" />




Quirks and Limitations

The current iteration runs in a simulated environment using a local text file; it does not natively bind to live system logs or require root privileges to execute.

Active network mitigation (e.g., automatically banning flagged IPs via firewall rules) is intentionally omitted to keep the tool strictly focused on detection and log parsing logic.

Geolocation API resolution for attacking IPs is planned but not yet active in the core loop.
