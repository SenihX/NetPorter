import socket
from concurrent.futures import ThreadPoolExecutor
import time

def scan_port(ip, port):
    """Scan a single port on a given IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Connection timeout
            s.connect((ip, port))
            return port
    except:
        return None

def main():
    print(" ")
    print("NetPorter - Coder By SenihX")
    print("Github: https://github.com/SenihX")
    print(" ")
    target_ip = input("Enter the target IP address: ").strip()
    start_port = int(input("Enter the starting port (default 1): ") or 1)
    end_port = int(input("Enter the ending port (default 65535): ") or 65535)

    # Bitiş portu uyarısı
    if end_port > 10000:
        cont = input("The ending port is quite high. This process may take a long time. Do you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("Operation cancelled by the user.")
            return

    print(f"\nScanning {target_ip} for open ports from {start_port} to {end_port}...\n")
    print("This process may take some time, please be patient.\n")

    open_ports = []
    total_ports = end_port - start_port + 1
    scanned_ports = 0

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}

        for future in futures:
            port = future.result()
            scanned_ports += 1

            # Progress tracking
            elapsed_time = time.time() - start_time
            ports_left = total_ports - scanned_ports
            estimated_time = (elapsed_time / scanned_ports) * ports_left if scanned_ports > 0 else 0

            if port:
                open_ports.append(port)
                print(f"Port {port} is open (Scanned {scanned_ports}/{total_ports})")

            print(f"Progress: {scanned_ports}/{total_ports} ports scanned. Estimated time left: {int(estimated_time)} seconds.", end='\r')

    print("\n\nScan completed!")
    if open_ports:
        print(f"Open ports on {target_ip}:")
        for port in open_ports:
            print(f" - Port {port} is open")
    else:
        print("No open ports found.")

    print("\nFor Your Wishes and Complaints: senihx01@gmail.com")

if __name__ == "__main__":
    main()
