#write functions here, don't add input('') statements here!
def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return "Invalid arguments"
    elif sales <= 499:
        return round((sales * 5) / 100, 2)
    elif sales <= 999:
        return round((sales * 6) / 100, 2)
    elif sales <= 1499:
        return round((sales * 7) / 100, 2)
    elif sales <= 1999:
        return round((sales * 8) / 100, 2)