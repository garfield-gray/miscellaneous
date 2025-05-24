#! /usr/bin/env python3


# run in using "./log1.py /var/log/syslog"


import sys

logfile = sys.argv[1]


import re
from collections import defaultdict

# Load syslog lines
with open(logfile, "r") as file:
    lines = file.readlines()

# Pattern for lines like: CRON[pid]: (username) CMD (...)
cron_pattern = re.compile(r"\[\d+\]:\s+\((?P<user>\w+)\)\s+CMD")
# Dictionary to count usernames
user_counts = defaultdict(int)

# Parse and count
for line in lines:
    match = cron_pattern.search(line)
    if match:
        user = match.group("user")
        user_counts[user] += 1

# Print results
print("Username occurrences in CRON logs:")
for user, count in user_counts.items():
    print(f"{user}: {count}")

