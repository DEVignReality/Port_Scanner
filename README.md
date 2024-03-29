Basic Port Scanner

This Basic Port Scanner is a Python-based tool designed to identify open ports on a given host. This is particularly useful for security analysis and network maintenance.
Features

  Scans specified port ranges on a host.
  Outputs the status of each port scanned.
  Times the duration of the scan.

Requirements:

Python 3.x installed on your system.

Usage:

Modify the port_scanner.py script to specify the target host by changing HOST_TO_SCAN to the desired IP address or hostname.

HOST_TO_SCAN = 'your_target_host'  # e.g., '192.168.1.1'

Set the PORT_RANGE in the script to the range of ports you wish to scan (default is 1 to 1025).

Run the script from the terminal or command prompt:

bash

    python3 port_scanner.py

  Observe the output in the terminal for open ports.

Troubleshooting

  No Results: If the script starts but no results are shown, ensure the host is reachable and not blocking your scanning attempts.

  Firewalls: If you're scanning remote hosts and getting no results, the host's firewall might be blocking incoming connections. Try scanning a local service that you know is open.

  Timeout Settings: If connections are timing out, consider increasing the timeout duration in the script.

  Permissions and Policies: Ensure you have the necessary permissions for network scanning, and you're not violating any network policies.

Disclaimer

Use this tool responsibly and ethically. Do not scan networks or hosts without explicit permission. Unauthorized scanning can lead to legal repercussions and is considered unethical behavior.
