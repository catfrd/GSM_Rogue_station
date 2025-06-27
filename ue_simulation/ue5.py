import json
import os
os.makedirs("crowdsourcing/ue_reports", exist_ok=True)

report = {
    "bts_id": "001-999",
    "imsi_requests": 2,
    "unencrypted_connections": 1,
    "fake_lac": True,
    "anomaly_score": 0.81
}

with open("crowdsourcing/ue_reports/ue5.json", "w") as f:
    json.dump(report, f, indent=2)
