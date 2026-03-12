
minutes = 42
seconds = 42

total_seconds = minutes * 60 + seconds
print("1. Total seconds:", total_seconds)

kilometers = 10
miles = kilometers / 1.61

print("2. Miles in 10 km:", miles)

total_seconds = 42 * 60 + 42
total_hours = total_seconds / 3600

miles = 10 / 1.61

pace_seconds_per_mile = total_seconds / miles
pace_minutes = int(pace_seconds_per_mile // 60)
pace_seconds = int(pace_seconds_per_mile % 60)

speed_mph = miles / total_hours

print("3. Average pace:", pace_minutes, "minutes", pace_seconds, "seconds per mile")
print("   Average speed:", speed_mph, "miles per hour")