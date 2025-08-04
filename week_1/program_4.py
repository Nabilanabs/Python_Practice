import time

# Get the current time
current_time = time.localtime()

# Format the time
formatted_time = time.strftime("%a %b %d %H:%M:%S %Z %Y", current_time)

# Print the formatted time
print("Current Date and Time:", formatted_time)