"""
RECORD CHECK  -  my version
===========================

Name  : Ramtohul Pouroushottam
Lane  :  AI     (delete two)
Date  : 9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""




rows_loaded = float(input("Enter rows loaded: ")) # asks user to input rows loaded and converts it to a float
rows_expected = float(input("Enter rows expected: ")) # asks user to input rows expected and converts it to a float
dataset_name = input("Enter dataset_name: ") # asks user to input dataset name
percent = (rows_loaded/rows_expected) * 100 # calculates the percentage of rows loaded as a percentage of rows expected
free = rows_expected - rows_loaded # calculates the number of free rows


def check(value,limit): 
    difference = limit - value
    percent = (value/limit) * 100
    return difference, percent # returns the difference and percent as a tuple

def status_of(percent):
    if percent >= 90:
        return "OVER LIMIT"
    else:
        return "OK"


status = status_of(percent) # calls the status_of function with the percent value and assigns the result to the variable status


def print_report(label, value, limit, difference, percent, status): 
    """Prints a report of the record check results"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Rows Loaded   : {value:>10.2f}") # prints the number of rows loaded, formatted to 2 decimal places and right-aligned
    print(f"  Rows Expected : {limit:>10.2f}") # prints the number of rows expected, formatted to 2 decimal places and right-aligned
    print(f"  Difference    : {difference:>10.2f}") # prints the difference, formatted to 2 decimal places and right-aligned
    print(f"  Percent       : {percent:>10.2f}") # prints the percentage formated to 2 decimal places and right-aligned
    print(f"  Status        : {status:>10}") # prints the status, right-aligned
    print("=" * 34)
print_report(dataset_name, rows_loaded, rows_expected, free, percent, status) #

