from datetime import datetime, timedelta

# Get the current time
current_time = datetime.now()

# Subtract 30 minutes
time_minus_30_minutes = current_time - timedelta(minutes=30)

# Format the datetime objects
current_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
time_minus_30_minutes_str = time_minus_30_minutes.strftime("%Y-%m-%dT%H:%M:%SZ")

print("Current Time:", current_time_str)
print("Time Minus 30 Minutes:", time_minus_30_minutes_str)
