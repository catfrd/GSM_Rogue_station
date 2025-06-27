import json
import os
os.makedirs("crowdsourcing/ue_reports", exist_ok=True)

report = {
    "bts_id": "001-001",
    "imsi_requests": 1,
    "unencrypted_connections": 0,
    "fake_lac": False,
    "anomaly_score": 0.15
}

with open("crowdsourcing/ue_reports/ue4.json", "w") as f:
    json.dump(report, f, indent=2)
