def leap_year(year):
    divisible_by = lambda x: year % x == 0

    if not divisible_by(4):
        return False

    return not divisible_by(100) or divisible_by(400)
