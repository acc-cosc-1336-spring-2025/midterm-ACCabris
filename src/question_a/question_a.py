def get_day_of_week(day):
    if day < 1 or day > 7:
        return "Invalid input. Please enter a number between 1 and 7."
    elif day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    else:
        return "Sunday"

day = int(input("Enter a number between 1 and 7: "))
print(get_day_of_week(day))