import subprocess
import time
import statistics

# Configuration
TARGET_HOST = "8.8.8.8"  # Google DNS, can be changed
PING_COUNT = 5  # Number of pings per check
THRESHOLD_LOSS = 20  # % packet loss to consider network unstable
THRESHOLD_LATENCY = 200  # ms latency threshold
THRESHOLD_JITTER = 50  # ms jitter threshold
CHECK_INTERVAL = 10  # Time between checks in seconds

def ping_host(host, count=5):
    """Ping a host and return packet loss and latency stats."""
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), host], capture_output=True, text=True
        )
        output = result.stdout

        # Extract packet loss
        loss_line = [line for line in output.split("\n") if "packet loss" in line]
        if loss_line:
            loss_percent = int(loss_line[0].split("%")[0].split()[-1])
        else:
            loss_percent = 100  # Assume full loss if no response

        # Extract latencies
        latency_line = [line for line in output.split("\n") if "min/avg/max/mdev" in line]
        if latency_line:
            latencies = list(map(float, latency_line[0].split("=")[1].split("/")[0:4]))
            avg_latency, jitter = latencies[1], latencies[3]
        else:
            avg_latency, jitter = float('inf'), float('inf')

        return loss_percent, avg_latency, jitter

    except Exception as e:
        print("Error executing ping:", e)
        return 100, float('inf'), float('inf')  # Assume worst case if error

def check_network():
    """Monitors network stability."""
    while True:
        print("\nChecking network stability...")
        loss, latency, jitter = ping_host(TARGET_HOST, PING_COUNT)

        print(f"Packet Loss: {loss}%")
        print(f"Average Latency: {latency} ms")
        print(f"Jitter: {jitter} ms")

        if loss > THRESHOLD_LOSS:
            print("⚠ Unstable Network: High packet loss detected!")
        elif latency > THRESHOLD_LATENCY:
            print("⚠ Unstable Network: High latency detected!")
        elif jitter > THRESHOLD_JITTER:
            print("⚠ Unstable Network: High jitter detected!")
        else:
            print("✅ Network is stable.")

        time.sleep(CHECK_INTERVAL)

# Run network check
check_network()
