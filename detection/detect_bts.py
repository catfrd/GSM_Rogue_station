import time

def tail_f(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

log_file = "logs/openbts_simulated.log"

for line in tail_f(log_file):
    if "unencrypted" in line or "MNC: 999" in line:
        print("ALERT: Rogue BTS activity detected!")
        print(f"DETAIL: {line.strip()}")
