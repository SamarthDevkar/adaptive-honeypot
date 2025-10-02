# classify_live.py
import json
import joblib

model = joblib.load("command_classifier.joblib")

with open('../cowrie/var/log/cowrie/cowrie.json') as f:
    for line in f:
        try:
            log = json.loads(line)
            if log.get("eventid") == "cowrie.command.input":
                cmd = log["input"]
                label = model.predict([cmd])[0]
                print(f"{cmd} --> {label}")
        except:
            continue
