#write functions here, don't add input('') statements here!
def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes < 0:
        return "Invalid arguments"
    else:
        miles = kilometers * 0.621371 + (minutes / 60) * 0.621371
        return round(miles, 2)