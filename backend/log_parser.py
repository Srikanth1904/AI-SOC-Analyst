import re
from collections import Counter

def parse_logs(log_content):

    lines = log_content.splitlines()

    failed_logins = 0
    successful_logins = 0

    failed_ips = []
    all_ips = []

    for line in lines:

        ips = re.findall(
            r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
            line
        )

        all_ips.extend(ips)

        if "Failed login" in line:
            failed_logins += 1
            failed_ips.extend(ips)

        if "Successful login" in line:
            successful_logins += 1

    attacker_ip = "N/A"

    if failed_ips:
        attacker_ip = Counter(failed_ips).most_common(1)[0][0]

    return {
        "total_lines": len(lines),
        "failed_logins": failed_logins,
        "successful_logins": successful_logins,
        "ip_addresses": list(set(all_ips)),
        "top_attacker_ip": attacker_ip
    }