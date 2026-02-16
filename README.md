# HTTP Packet Sniffer

A lightweight Python script that captures and analyzes HTTP packets using the **Scapy** library.

## ⚠️ Disclaimer

**EDUCATIONAL PURPOSE ONLY.**

This tool is intended for **network analysis, debugging, and educational purposes** to understand how unencrypted HTTP traffic works.

* Do not use this tool to intercept traffic on networks you do not own or have explicit permission to test.
* The developer assumes **no liability** for any misuse or damage caused by this program.

## Features

* **Packet Sniffing:** Listens for traffic on TCP Port 80.
* **Request Analysis:** Extracts and displays the `Host` and `Path` of the URL.
* **Data Capture:** Attempts to decode and display `Raw` data (useful for viewing unencrypted POST bodies).

## Prerequisites

To run this script, you need:

1.  **Python 3.x**
2.  **Scapy Library**
3.  **Root/Administrator Privileges** (Required to access the network interface).

## Installation

1.  Clone this repository.
2.  Install the required Python dependency:

    ```bash
    pip install scapy
    ```

## Usage

Since packet sniffing requires access to the network card, you must run the script with administrative privileges.

### Linux / macOS
Run with `sudo`:

    sudo python http.py

### Windows
Open your Command Prompt (CMD) or PowerShell as **Administrator** and run:

    python http.py

## Limitations

* **HTTP Only:** This tool only captures unencrypted HTTP traffic (Port 80). It **cannot** decrypt or read HTTPS traffic (Port 443).
