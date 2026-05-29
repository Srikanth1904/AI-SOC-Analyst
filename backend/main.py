from fastapi.middleware.cors import CORSMiddleware
from anomaly_detector import detect_anomalies
from report_generator import generate_recommendation
from threat_analyzer import analyze_threat
from log_parser import parse_logs
from fastapi import FastAPI, UploadFile, File

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "project": "AI SOC Analyst",
        "status": "Running"
    }

@app.get("/health")
def health_check():
    return {
        "server": "online",
        "module": "SOC Backend",
        "version": "1.0"
    }

@app.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    content = await file.read()

    decoded_content = content.decode("utf-8")

    analysis = parse_logs(decoded_content)

    risk_level = analyze_threat(
        analysis["failed_logins"]
    )

    recommendation = generate_recommendation(
        risk_level
    )
    anomaly_status = detect_anomalies(
    analysis["failed_logins"]
    )

    return {
        "filename": file.filename,
        "analysis": analysis,
        "risk_level": risk_level,
        "anomaly_status": anomaly_status,
        "recommendation": recommendation
    }