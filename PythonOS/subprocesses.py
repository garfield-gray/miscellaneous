#! /usr/bin/env python3

import subprocess


subprocess.run(["date"])


subprocess.run(["sleep", "2"])


result = subprocess.run(["ls", "fake_file"])
print(result.returncode)






result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)






result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)



result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())



