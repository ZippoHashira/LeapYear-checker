# Leap Year Checker

The `leap_year.py` program is designed to determine and display leap years based on user input.

## How to use:

1. Clone the repository to your local machine or create a new Python file called `leap_year.py` in your preferred directory.
2. Open the `leap_year.py` file in a Python editor or IDE of your choice.
3. In the program, you will be prompted to input a starting year and the number of years to check for leap years.
4. The program will use a `for` loop to iterate over the specified number of years and determine if each year is a leap year.
5. Leap years will be displayed as output.

## Leap Year Calculation

A leap year is determined based on the following criteria:

- If a year is divisible by 4, it is a leap year, except for:
  - Years divisible by 100, which are not leap years, unless:
    - They are also divisible by 400, in which case they are leap years.
