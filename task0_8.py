def time_convertor(num):
    number = int(num)

    HandlesPluralsForHours = "hour"
    HandlesPluralsForMinutes = "minute"

    count_hours = 0

    while number >= 60:
        number -= 60
        count_hours += 1

    minutes = number
    if count_hours > 1:
        Handles_Plurals_For_Hours = "hours"

    if minutes > 1:
        Handles_Plurals_For_Minutes = "minutes"

    time = f"{count_hours}{Handles_Plurals_For_Hours}, {minutes}{Handles_Plurals_For_Minutes}"
    return time


timed = time_convertor(133)
print(timed)
