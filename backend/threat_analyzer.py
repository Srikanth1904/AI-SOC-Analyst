def analyze_threat(failed_logins):
    
    if failed_logins >= 10:
        return "HIGH"

    elif failed_logins >= 5:
        return "MEDIUM"

    else:
        return "LOW"