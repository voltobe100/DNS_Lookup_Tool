import socket
import argparse
import json
import datetime

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return {"domain": domain, "ip_address": ip_address}
    except socket.gaierror:
        return {"domain": domain, "error": "Unable to resolve"}

def reverse_lookup(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return {"ip_address": ip, "reverse_lookup": host[0]}
    except socket.herror:
        return {"ip_address": ip, "error": "Reverse lookup failed"}

def save_log(results):
    with open("dns_lookup.log", "a") as log_file:
        log_file.write(json.dumps(results) + "\n")

def main():
    parser = argparse.ArgumentParser(description="DNS Lookup Tool")
    parser.add_argument("--domain", nargs="+", help="Resolve domain names to IP addresses")
    parser.add_argument("--reverse", help="Perform reverse lookup on an IP address")
    parser.add_argument("--log", action="store_true", help="Save results to a log file")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()
    results = []

    if args.domain:
        for domain in args.domain:
            results.append(resolve_domain(domain))

    if args.reverse:
        results.append(reverse_lookup(args.reverse))

    if args.json:
        print(json.dumps(results, indent=4))
    else:
        for result in results:
            print("\n".join([f"{key.replace('_', ' ').title()}: {value}" for key, value in result.items()]))
            print("-" * 40)

    if args.log:
        save_log(results)

if __name__ == "__main__":
    main()
