import { useEffect, useState } from "react";

function App() {
  const uploadFile = async () => {
  if (!selectedFile) {
    alert("Please select a file");
    return;
  }

  const formData = new FormData();
  formData.append("file", selectedFile);

  const response = await fetch(
    "http://127.0.0.1:8000/upload-log",
    {
      method: "POST",
      body: formData,
    }
  );

  const data = await response.json();
  setResult(data);
};
  const [health, setHealth] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((res) => res.json())
      .then((data) => setHealth(data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div
      style={{
        backgroundColor: "#0f172a",
        minHeight: "100vh",
        color: "white",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1>🛡️ AI SOC Analyst Dashboard</h1>
      <input
  type="file"
  onChange={(e) => setSelectedFile(e.target.files[0])}
  style={{
    marginTop: "20px",
    marginBottom: "20px",
    color: "white"
  }}
/>
<button
  onClick={uploadFile}
  style={{
    marginLeft: "10px",
    padding: "10px",
    cursor: "pointer"
  }}
>
  Upload Log
</button>

      <div
        style={{
          background: "#1e293b",
          padding: "20px",
          borderRadius: "10px",
          marginTop: "20px",
          width: "400px",
        }}
      >
        <h3>Backend Status</h3>

        {health ? (
          <>
            <p>Server: {health.server}</p>
            <p>Module: {health.module}</p>
            <p>Version: {health.version}</p>
          </>
        ) : (
          <p>Loading...</p>
        )}
      </div>
      {result && (
  <div
    style={{
      background: "#1e293b",
      padding: "20px",
      borderRadius: "10px",
      marginTop: "20px",
      width: "500px",
    }}
  >
    <h2>Security Analysis</h2>

    <p><b>Failed Logins:</b> {result.analysis.failed_logins}</p>

    <p><b>Successful Logins:</b> {result.analysis.successful_logins}</p>

    <p><b>Risk Level:</b> {result.risk_level}</p>

    <p><b>Anomaly Status:</b> {result.anomaly_status}</p>

    <p><b>Recommendation:</b> {result.recommendation}</p>
  </div>
)}
    </div>
  );
}

export default App;