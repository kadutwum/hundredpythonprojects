import time
time_allowed = 5
while time_allowed:
    print(time_allowed, end="\r")
    time.sleep(1)
    time_allowed -= 1


