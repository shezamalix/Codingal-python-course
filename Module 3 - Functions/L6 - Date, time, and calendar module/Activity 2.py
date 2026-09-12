import time
import random

def getRandomDate(startDate, endDate) :
    r = random.random()
    dateFormat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + r * (endTime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate
    

print("Random Date = ", getRandomDate("1/1/2026", "9/12/2026"))






