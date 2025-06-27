import json
import os
os.makedirs("crowdsourcing/ue_reports", exist_ok=True)
 
report = {
    "bts_id": "001-999",
    "imsi_requests": 4,
    "unencrypted_connections": 3,
    "fake_lac": True,
    "anomaly_score": 0.92
}

with open("crowdsourcing/ue_reports/ue3.json", "w") as f:
    json.dump(report, f, indent=2)
