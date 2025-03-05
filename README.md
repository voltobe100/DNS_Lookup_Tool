# DNS Lookup Tool – Resolve Domain Names to IPs & Reverse Lookup

## Overview

This is a simple command-line tool to resolve domain names to their respective IP addresses and perform reverse lookups (finding the domain name associated with an IP address). It is useful for network troubleshooting, security analysis, and general networking tasks.

## Features

- Resolve domain names to IP addresses.
- Perform reverse DNS lookups.
- Support for multiple domain queries.
- Output results in JSON format for easy integration.
- Logging feature to save lookup history.

## Installation

Ensure you have Python installed, then install the required dependencies:

```bash
pip install dnspython
```

## Usage

Run the script using the command:

```bash
python dns_lookup.py --domain example.com
```

### Additional Options

- Perform a reverse DNS lookup:
  ```bash
  python dns_lookup.py --reverse 8.8.8.8
  ```
- Query multiple domains:
  ```bash
  python dns_lookup.py --domain example.com google.com
  ```
- Save results to a log file:
  ```bash
  python dns_lookup.py --log
  ```
- Output results in JSON format:
  ```bash
  python dns_lookup.py --json
  ```

## Example Output

```bash
Domain: example.com
Resolved IP: 93.184.216.34

IP Address: 8.8.8.8
Reverse Lookup: dns.google
```

## Logging Feature

Lookup results can be saved in a `dns_lookup.log` file for reference.

## License

This project is licensed under the MIT License.
