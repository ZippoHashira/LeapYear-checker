# Request integer input from the user to get start year 'year' and year count 'number_year'.
year = int(input("What year do you want to start with? "))
number_year = int(input("How many years do you want to check? "))

# Add year and number_year and store it in 'year_loop' which will be our end index.
year_loop = year + number_year

# For loop begins with 'year' value as start index and 'year_loop' value as end index.
for i in range(year, year_loop):

    # If 'i' is divisible by 400 and is a century year (i.e. i % 100 == 0),print 'It's a leap year'.
    if i % 400 == 0 and i % 100 == 0:
        print(f"{i} is a leap year.")

    # Else if 'i' is divisible by 4 but is not a century year (i.e. i % 100 != 0), print 'It's a leap year'.
    elif i % 4 == 0 and i % 100 != 0:
        print(f"{i} is a leap year.")

    # Otherwise, print 'It's not a leap year'.
    else:
        print(f"{i} is not a leap year.")
