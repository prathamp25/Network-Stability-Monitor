# Network-Stability-Monitor
This Python script monitors network stability by periodically pinging a target host, measuring packet loss, latency, and jitter. If any metric exceeds predefined thresholds, it flags the network as unstable. The tool helps diagnose connectivity issues for troubleshooting and performance optimization.

1. The **Network Stability Monitor** is a Python-based tool that continuously checks internet connectivity.  
2. It pings a target server (default: Google DNS `8.8.8.8`) at regular intervals.  
3. The script calculates **packet loss**, **average latency**, and **jitter** from the ping responses.  
4. If packet loss exceeds **20%**, latency crosses **200ms**, or jitter exceeds **50ms**, the network is flagged as unstable.  
5. These thresholds can be modified based on user requirements.  
6. The script runs indefinitely, checking the network every **10 seconds** by default.  
7. It provides real-time feedback on network health, aiding in troubleshooting slow or unstable connections.  
8. The tool is useful for **network engineers, IT administrators, and remote workers**.  
9. The implementation relies on Python’s `subprocess` module to execute ping commands.  
10. Future improvements could include **logging, visualization, and email alerts** for proactive monitoring.
