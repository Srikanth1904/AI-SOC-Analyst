 # AI SOC Analyst

## Overview

AI SOC Analyst is a cybersecurity-focused web application developed to simulate some of the core activities performed by a Security Operations Center (SOC). The project analyzes uploaded log files, identifies suspicious activities, detects brute-force login attempts, extracts attacker IP addresses, and provides security recommendations through an interactive dashboard.

The main goal of this project was to gain practical experience in cybersecurity monitoring, log analysis, threat detection, machine learning, API development, and frontend-backend integration.

While learning cybersecurity concepts, I noticed that most beginner projects focus on simple scanners or basic scripts. I wanted to build something that combines cybersecurity concepts with software development and machine learning. This project helped me understand how security logs can be processed and transformed into meaningful security insights.

---

## Project Objective

Security teams receive thousands of log events every day. Manually reviewing these logs is time-consuming and inefficient. The purpose of this project is to automate part of that process by:

* Accepting security log files as input
* Parsing and analyzing log events
* Identifying failed login attempts
* Detecting suspicious IP addresses
* Detecting brute-force attack patterns
* Generating threat assessments
* Displaying findings in an easy-to-understand dashboard

The project demonstrates how cybersecurity concepts can be combined with modern web technologies and machine learning techniques.

---

## Features

### Log Upload and Analysis

Users can upload log files directly through the web dashboard. The uploaded logs are sent to the backend for processing and analysis.

### Failed Login Detection

The system scans log files and counts failed login attempts. Failed login events are one of the most common indicators of unauthorized access attempts.

### Successful Login Tracking

The application also tracks successful logins to provide additional context during analysis.

### IP Address Extraction

IP addresses are automatically extracted from uploaded logs using pattern matching techniques. This helps identify the systems generating suspicious activity.

### Top Attacker IP Detection

The application identifies the IP address responsible for the highest number of failed login attempts.

### Risk Classification

Based on observed activity, the system categorizes threats into:

* LOW
* MEDIUM
* HIGH

This allows analysts to prioritize investigations.

### Brute Force Attack Detection

The project detects potential brute-force attacks by monitoring repeated failed login attempts from the same source.

### Machine Learning Anomaly Detection

The application uses Isolation Forest from Scikit-Learn to identify unusual login patterns that may indicate suspicious activity.

### Security Recommendations

Based on the detected threat level, the system provides recommendations that can help analysts respond appropriately.

### SOC Alert Banner

When high-risk activity is detected, the dashboard displays a visible alert notification to highlight potential security incidents.

### Interactive Dashboard

The React-based frontend presents analysis results in a clear and user-friendly format.

---

## Technology Stack

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

### Backend

* Python
* FastAPI

### Machine Learning

* Scikit-Learn
* Isolation Forest

### Version Control

* Git
* GitHub

---

## Project Architecture

The application follows a frontend-backend architecture.

Frontend:

* React Dashboard
* File Upload Interface
* Threat Visualization

Backend:

* FastAPI REST APIs
* Log Processing Engine
* Threat Analysis Engine
* Machine Learning Module

Machine Learning Layer:

* Isolation Forest Anomaly Detection

---

## Workflow

1. User uploads a log file.
2. Frontend sends the file to the FastAPI backend.
3. Backend parses the uploaded log file.
4. Failed login attempts are counted.
5. IP addresses are extracted.
6. Top attacker IP is identified.
7. Risk level is calculated.
8. Machine learning model performs anomaly detection.
9. Security recommendations are generated.
10. Results are returned to the frontend dashboard.
11. Dashboard displays the analysis.

---

## Example Log Input

Failed login from 192.168.1.10

Failed login from 192.168.1.10

Failed login from 192.168.1.10

Failed login from 192.168.1.20

Successful login from 192.168.1.50

---

## Example Analysis Output

* Failed Logins: 4
* Successful Logins: 1
* Top Attacker IP: 192.168.1.10
* Risk Level: HIGH
* Anomaly Status: Detected
* Recommendation: Investigate suspicious login activity

---

## Challenges Faced During Development

While building this project, I encountered several practical challenges:

* Setting up FastAPI backend services
* Connecting React frontend with FastAPI APIs
* Handling CORS issues
* Processing uploaded files correctly
* Integrating machine learning predictions
* Debugging frontend and backend communication
* Designing a dashboard that presents information clearly

Solving these challenges helped improve my understanding of full-stack development and cybersecurity workflows.

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Cybersecurity log analysis
* Threat detection concepts
* Security monitoring workflows
* Python backend development
* FastAPI API development
* React frontend development
* Machine learning integration
* REST API communication
* Git and GitHub version control
* Debugging real-world application issues

---

## Future Improvements

Future enhancements planned for this project include:

* Threat severity scoring
* PDF incident report generation
* SQLite database integration
* Historical attack tracking
* User authentication and authorization
* Threat intelligence integration
* MITRE ATT&CK mapping
* Geo-location tracking of attacker IPs
* AI-generated incident summaries
* Real-time monitoring capabilities

---

## Author

Bandi Srikanth

Cybersecurity Enthusiast | Full Stack Developer

GitHub: https://github.com/Srikanth1904

