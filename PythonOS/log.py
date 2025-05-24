#! /usr/bin/env python3


# run in using "./log.py /var/log/syslog"


import sys
import re

logfile = sys.argv[1]


with open(logfile, "r") as file:
    lines = file.readlines()

# Regex for ISO-style CRON lines
cron_pattern = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}T[\d:.+-]+)\s+"
    r"\S+\s+CRON\[\d+\]:\s+\((?P<user>\w+)\)\s+CMD\s+\((?P<command>.+)\)$"
)

# Extract and print matches
for line in lines:
    line = line.strip()
    match = cron_pattern.match(line)
    if match:
        ts = match.group("timestamp")
        user = match.group("user")
        cmd = match.group("command")
        print(f"[{ts}] {user} ran: {cmd}")

