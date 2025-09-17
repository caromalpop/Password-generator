#Creating a calandar for a specific month and year
import calendar
y = 2024
m = 12
print(calendar.month(y, m))

#Creating a study planner for a specific month and year
import calendar
y = 2024
m = 12
cal = calendar.monthcalendar(y, m)
study_days = [1, 3, 5]  # Study on Mondays, Wednesdays, and Fridays
print("Study Planner for December 2024:")
for week in cal:
    for day in week:
        if day != 0 and calendar.weekday(y, m, day) in study_days:
            print(f"Study on: {day}/{m}/{y}")

