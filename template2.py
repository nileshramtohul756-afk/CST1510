"""
RECORD CHECK  -  my version
===========================

Name  : Ramtohul Pouroushottam
Lane  :  AI      (delete two)
Date  : 3/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


used = int(input("Enter used: "))
total = int(input("Enter total: "))
difference = total - used     # calculates how much is free
percent = (used/total) * 100  # calculates percentage used


print()
print("=" *34 )
print("   RECORD CHECK  -  srv-01")
print("=" *34 )
print(f"{" " * 2}Used{" " * 9}:{used:>11.2f}")  # number used is right aligned by 11 with 2 decimal places
print(f"{" " * 2}Total{" " * 8}:{total:>11.2f}")  # total is right aligned by 11 with 2 decimal places
print(f"{" " * 2}Free{" " * 9}:{difference:>11.2f}")  # the difference is right aligned by 11 with 2 decimal places
print(f"{" " * 2}Percent{" " * 6}:{percent:>11.2f} %")   # the percentage used is right aligned by 11 with 2 decimal places

if used >= total and percent >= 100:                    # 2 conditions to be satisfied to display the status
    print(f"{" " * 2}Status{" " * 7}:{" " * 9}OVER LIMIT")
elif used < total and percent >= 90:
    print(f"{" " * 2}Status{" " * 7}:{" " * 9}WARNING")  
else:
    print(f"{" " * 2}Status{" " * 7}:{" " * 9}OK")

print("=" *34 )

