import socket
from datetime import datetime

def scan_ports(host, port_range):
    print(f"Starting scan on host: {host}")
    # Begin time tracking
    start_time = datetime.now()

    # Scan the specified port range
    for port in range(*port_range):  # The '*' allows us to unpack the tuple range
        try:
            # Create a new socket for each port
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Timeout for each socket attempt
                connection = s.connect_ex((host, port))  # Returns an error indicator
                if connection == 0:
                    print(f"Port {port}: Open")
        except KeyboardInterrupt:
            print("Exiting program.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Couldn't connect to server.")
            break

    # Calculate and print the total scanned time
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scanning completed in: {total_time}")

# Replace 'your_target_host' with the host you want to scan
HOST_TO_SCAN = 'your_target_host'  # e.g., '127.0.0.1' for localhost
PORT_RANGE = (1, 1025)  # Standard range includes ports 1 through 1024

if __name__ == "__main__":
    scan_ports(HOST_TO_SCAN, PORT_RANGE)
