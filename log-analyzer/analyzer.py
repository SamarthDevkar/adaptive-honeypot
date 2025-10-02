import json
from collections import defaultdict
import os

LOG_PATH = "../cowrie/var/log/cowrie/cowrie.json"

if not os.path.exists(LOG_PATH):
    print(f"❌ Cowrie log not found at {LOG_PATH}")
    exit(1)

sessions = defaultdict(lambda: {
    "ip": None,
    "credentials": [],
    "commands": [],
    "start": None
})

with open(LOG_PATH, "r") as f:
    for line in f:
        try:
            log = json.loads(line)
        except json.JSONDecodeError:
            continue

        sid = log.get("session")
        if not sid:
            continue

        event = log.get("eventid")
        if event == "cowrie.session.connect":
            sessions[sid]["ip"] = log.get("src_ip")
            sessions[sid]["start"] = log.get("timestamp")
        elif event == "cowrie.login.success":
            sessions[sid]["credentials"].append((log.get("username"), log.get("password")))
        elif event == "cowrie.command.input":
            sessions[sid]["commands"].append(log.get("input"))

with open("parsed_sessions.json", "w") as out:
    json.dump(sessions, out, indent=4)

print(f"✅ Parsed and saved {len(sessions)} attacker sessions to parsed_sessions.json")
