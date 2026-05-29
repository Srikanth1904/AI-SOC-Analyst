def generate_recommendation(risk_level):

    if risk_level == "HIGH":
        return "Possible brute force attack detected. Investigate source IPs immediately."

    elif risk_level == "MEDIUM":
        return "Multiple failed login attempts detected. Monitor user activity."

    else:
        return "No significant threat detected."