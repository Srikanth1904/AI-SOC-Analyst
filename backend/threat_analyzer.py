def analyze_threats(log_data):

    failed_logins = log_data["failed_logins"]

    severity_score = min(failed_logins * 20, 100)

    if failed_logins >= 5:
        risk_level = "HIGH"
        recommendation = (
            "Possible brute force attack detected. "
            "Block suspicious IP addresses immediately."
        )

    elif failed_logins >= 3:
        risk_level = "MEDIUM"
        recommendation = (
            "Multiple failed login attempts detected. "
            "Monitor user activity."
        )

    else:
        risk_level = "LOW"
        recommendation = (
            "No significant threat detected."
        )

    return risk_level, recommendation, severity_score