import os
### I wish I knew all of these when I was working back in rahap,

###to rename all the craps automatically:)


# os.remove("something")
# od.rename()
print(os.path.exists("sample.txt"))

print("size of sample.txt")

print(os.path.getsize("sample.txt"))

print("last update sample.txt")

import datetime
print(datetime.datetime.fromtimestamp(os.path.getatime("sample.txt")))


print("abs path sample.txt")

print(os.path.abspath("sample.txt"))
