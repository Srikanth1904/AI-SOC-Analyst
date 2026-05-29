def parse_logs(log_content):
    lines = log_content.splitlines()

    failed_logins = 0
    successful_logins = 0

    for line in lines:
        if "Failed login" in line:
            failed_logins += 1

        if "Successful login" in line:
            successful_logins += 1

    return {
        "total_lines": len(lines),
        "failed_logins": failed_logins,
        "successful_logins": successful_logins
    }