def leap_year_check():
    a = input('Insert a year to check: ')
    assert a.isnumeric(), 'Input must be numeric'
    a = int(a)
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print(f"{a} is a leap year")
    else:
        print(f"{a} is not a leap year")

leap_year_check()