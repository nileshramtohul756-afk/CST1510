"""
RECORD CHECK  -  my version
===========================

Name  :Ramtohul Pouroushottam
Lane  :  AI     
Date  :29/09/2026


"""

rows_loaded = float(input("Enter rows loaded: ")) # asks for rows loaded and converts to float
rows_expected = float(input("Enter rows expected: ")) # asks for rows expected and converts to float
free = rows_expected - rows_loaded # calculates the free rows 
percent_used = (rows_loaded / rows_expected) * 100  # calculates the percentage of rows used     
dataset_name = input("Enter dataset name: ") # asks for dataset name

print()
print("=" * 34) # prints 34 equal signs
print(f"   RECORD CHECK  -  {dataset_name}") 
print("=" * 34)
print(f"   Rows Loaded    : {rows_loaded:>+10.2f}")
print(f"   Rows Expected  : {rows_expected:>+10.2f}")
print(f"   Free           : {free:>+10.2f}")
print(f"   Percent        : {percent_used:>+10.2f} %")
print("=" * 34)