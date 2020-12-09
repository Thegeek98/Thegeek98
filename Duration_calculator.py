hours = int(input("Starting time(hours): "))
minutes = int(input("Starting time(minutes): "))
duration = int(input("Event duration(minutes): "))

# Find a total of all minutes
all_minutes = (hours * 60) + minutes + duration

# Find a number of hours hidden in minutes and update the hour
hour = all_minutes // 60

# Correct minutes to fall in the (0..59) range
mins = all_minutes % 60

# Correct hours to fall in the (0..23) range
hour %= 24

print(hour, ":", mins, sep="")
