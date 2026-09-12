import datetime
import calendar

now = datetime.datetime.now()
print(now)

print(calendar.month(2026, 9))

today = datetime.date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)

#format the full date time string
print(now.strftime("%H:%M:%S"))

print(now.strftime("%I:%M:%S %p"))