import json
import glob

THRESHOLD = 0.8
report_dir = "crowdsourcing/ue_reports/"
reports = glob.glob(f"{report_dir}/*.json")

summary = {}
flagged_bts = set()

for report_file in reports:
    with open(report_file) as f:
        data = json.load(f)
        bts = data["bts_id"]
        if bts not in summary:
            summary[bts] = {"total_reports": 0, "total_score": 0.0}
        summary[bts]["total_reports"] += 1
        summary[bts]["total_score"] += data["anomaly_score"]

# Evaluate
for bts_id, stats in summary.items():
    avg_score = stats["total_score"] / stats["total_reports"]
    print(f"\nBTS: {bts_id} | Reports: {stats['total_reports']} | Avg Score: {avg_score:.2f}")
    if avg_score > THRESHOLD:
        print("Flagged as Rogue BTS!")
        flagged_bts.add(bts_id)

with open("data/rogue_bts_list.json", "w") as f:
    json.dump(list(flagged_bts), f, indent=2)
