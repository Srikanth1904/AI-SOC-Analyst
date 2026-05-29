from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(failed_logins):

    data = pd.DataFrame({
        "failed_logins": [1, 2, 3, 4, 5, failed_logins]
    })

    model = IsolationForest(
        contamination=0.2,
        random_state=42
    )

    predictions = model.fit_predict(data)

    if predictions[-1] == -1:
        return "Anomaly Detected"

    return "Normal Activity"