import argparse
from utils.vt_lookup import vt_lookup
from utils.abuseipdb import check_ip
from utils.formatter import print_result

def main():
    parser = argparse.ArgumentParser(description="Threat Intelligence Checker")

    parser.add_argument("--type", required=True, choices=["ip", "domain", "hash"],
                        help="Type of IOC")
    parser.add_argument("--value", required=True,
                        help="IOC value (IP/domain/hash)")

    args = parser.parse_args()

    vt_data = vt_lookup(args.value, args.type)

    abuse_data = None
    if args.type == "ip":
        abuse_data = check_ip(args.value)

    print_result(args.value, vt_data, abuse_data)

if __name__ == "__main__":
    main()
