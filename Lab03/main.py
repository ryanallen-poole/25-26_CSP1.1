seconds = 10000
hours = int(seconds / 3600)
secondsLeft = seconds % 3600
seconds = 2800
minutes = int(seconds / 60)
remainder = seconds % 60
seconds = 10000123
milliseconds = seconds % 1000

print("Lab03, 80 Point Version")
print("Starting seconds: ", seconds)
print("hours: ", hours)
print("minutes: ", minutes)
print("seconds: ", remainder)
print("milliseconds: ", milliseconds)
