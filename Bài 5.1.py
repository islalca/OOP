import time

# seconds since epoch
current_time = time.time()

# number of days since epoch
days = current_time // (24 * 60 * 60)

# seconds remaining today
seconds_today = current_time % (24 * 60 * 60)

# convert to hours, minutes, seconds
hours = seconds_today // 3600
seconds_today = seconds_today % 3600

minutes = seconds_today // 60
seconds = seconds_today % 60

print("Days since epoch:", int(days))
print("Current time:", int(hours), ":", int(minutes), ":", int(seconds))