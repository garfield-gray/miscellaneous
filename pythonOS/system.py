#! /usr/bin/env python3


import shutil

du = shutil.disk_usage("/")

print(du)


print(du.used/du.total)
