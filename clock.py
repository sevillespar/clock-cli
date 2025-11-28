from datetime import datetime

now = datetime.now()

print("24h:", now.strftime("%H:%M:%S"))
print("12h:", now.strftime("%I:%M:%S %p"))
print("ISO:", now.isoformat())
