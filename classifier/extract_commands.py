import json

with open('../cowrie/var/log/cowrie/cowrie.json') as f, open('commands.txt', 'w') as out:
    for line in f:
        try:
            log = json.loads(line)
            if log.get("eventid") == "cowrie.command.input":
                out.write(log["input"] + "\n")
        except:
            continue
