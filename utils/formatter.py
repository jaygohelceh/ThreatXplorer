from colorama import Fore, Style

def print_result(value, vt_data, abuse_data=None):
    print(f"\n[+] Checking: {value}\n")

    if vt_data:
        print("VirusTotal:")
        print(f"  Malicious: {vt_data.get('malicious', 0)}")
        print(f"  Suspicious: {vt_data.get('suspicious', 0)}")

    if abuse_data:
        print("\nAbuseIPDB:")
        print(f"  Abuse Score: {abuse_data['abuse_score']}")
        print(f"  Reports: {abuse_data['total_reports']}")

    verdict = "CLEAN"

    if (vt_data and vt_data.get("malicious", 0) > 0) or \
       (abuse_data and abuse_data["abuse_score"] > 50):
        verdict = "MALICIOUS"

    if verdict == "MALICIOUS":
        print(Fore.RED + f"\n[!] Verdict: {verdict}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"\n[+] Verdict: {verdict}" + Style.RESET_ALL)
