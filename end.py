from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

with open("end_time.txt", "w") as f:
    f.write(f"{current_time}")
