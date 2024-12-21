# SlowWeb - Distributed Denial of Service (DDoS) Tool

## Description

SlowWeb is a simple Distributed Denial of Service (DDoS) tool developed in Python. It simulates a "Slowloris"-style attack using multiple threads to target web servers. The tool checks for required dependencies (`ping` and `nmap`), installs them if necessary, and allows the user to target a website for testing purposes.

## Features

- **Check Dependencies**: Verifies if `ping` and `nmap` are installed. Installs them if not.
- **IP and Port Detection**: Automatically detects the target's IP address using `ping` and scans open ports using `nmap`.
- **Thread Management**: Allows users to specify the number of threads to use for the attack.
- **DDoS Attack Simulation**: Simulates a DDoS attack using a large number of threads.

## Installation

1. **Install dependencies**:

    The tool requires the following Python libraries:
    - `colorama` (for color output in the terminal)

    You can install the dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

2. **Ensure system dependencies**:

    The tool requires the following system utilities:
    - `ping`
    - `nmap`

    To check if these are installed, the tool will attempt to run them and prompt you to install them if missing. For Linux, you can install them manually using:

    ```bash
    sudo apt update
    sudo apt install iputils-ping nmap -y
    ```

## Usage

1. **Run the tool**:

    After installing the dependencies, run the tool using:

    ```bash
    python3 ddos.py
    ```

2. **Follow the prompts**:
    - Enter the website URL (e.g., `example.com`).
    - The tool will automatically resolve the IP address and scan for open ports (80 and 443).
    - Select the port you want to attack (usually 80 for HTTP).
    - Enter the number of threads to use.

3. **Monitoring the attack**:
    - The tool will start the attack and provide a live update on the attack status.
    - Press `Ctrl+C` to stop the attack.

## Disclaimer

**WARNING**: This tool should only be used for educational purposes and testing on servers you own or have explicit permission to test. Using this tool to attack websites or services without authorization is illegal and unethical.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
