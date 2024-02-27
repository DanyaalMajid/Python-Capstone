import psutil
import time
import matplotlib.pyplot as plt

def get_bandwidth_usage():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    return bytes_sent, bytes_received

def bytes_to_megabytes(bytes):
    return bytes / (1024 * 1024)

def generate_bandwidth_report(duration_minutes=60):
    start_time = time.time()
    end_time = start_time + duration_minutes * 60

    data = []
    timestamps = []

    while time.time() < end_time:
        bytes_sent, bytes_received = get_bandwidth_usage()
        total_usage = bytes_to_megabytes(bytes_sent + bytes_received)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        data.append(total_usage)
        timestamps.append(current_time)
        time.sleep(1)

    return timestamps, data

def plot_bandwidth_report(timestamps, data):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, data, marker='o', linestyle='-')
    plt.title("Bandwidth Usage Report")
    plt.xlabel("Time")
    plt.ylabel("Total Usage (MB)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("bandwidth_usage.png")
    plt.show()

def main():
    print("Bandwidth Monitor")
    duration_minutes = int(input("Enter the duration of monitoring (in minutes): "))

    timestamps, data = generate_bandwidth_report(duration_minutes)
    plot_bandwidth_report(timestamps, data)

if __name__ == "__main__":
    main()
