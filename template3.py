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




rows_loaded = float(input("Enter rows loaded: "))
rows_expected = float(input("Enter rows expected: "))
dataset_name = input("Enter dataset_name: ")
free = rows_expected - rows_loaded
percent = (rows_loaded/rows_expected) * 100



def check(value,limit):
    difference = limit - value
    percent = (value/limit) * 100
    return difference, percent

def status_of(percent):
    if percent >= 90:
        return "OVER LIMIT"
    else:
        return "OK"


status = status_of(percent)


print("=" * 34)
print(f"  DATASET CHECK - {dataset_name}")
print("=" * 34)
print(f"  Rows loaded         :  {rows_loaded:>10.2f}")
print(f"  Rows expected       :  {rows_expected:>10.2f}")
print(f"  Free                :  {free:>10.2f}")
print(f"  Percent             :  {percent:>10.2f} %")
print(f"  Status              :  {status:>10}")
print("=" * 34)


