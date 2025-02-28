with open("start_time.txt", "r") as f:
    start = f.read()

with open("end_time.txt", "r") as f:
    end = f.read()

start = start.strip()
end = end.strip()

start_hours = int(start[:2])
end_hours = int(end[:2])

start_minutes = int(start[3:5])
end_minutes = int(end[3:5])

start_seconds = int(start[6:8])
end_seconds = int(end[6:8])

total_start = (start_hours * 3600) + (start_minutes * 60) + start_seconds
total_end = (end_hours * 3600) + (end_minutes * 60) + end_seconds

total_ellapsed = total_end - total_start 

hours_ellapsed = total_ellapsed // 3600
minutes_ellapsed = (total_ellapsed % 3600) // 60
seconds_ellapsed = total_ellapsed % 60


print(f"Time ellapsed: {hours_ellapsed}:{minutes_ellapsed}:{seconds_ellapsed}")
