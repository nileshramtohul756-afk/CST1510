"""
RECORD CHECK  -  my version
===========================

Name  :Ramtohul Pouroushottam
Lane  :  AI     
Date  :29/09/2026


"""

rows_loaded = input("Enter rows loaded")
rows_expected = input("Enter rows expected")
free = rows_expected - rows_loaded
percent_free = (free / rows_expected) * 100  # extra calculation: Useful for capacity planning to quickly know remaining space rather than mental math
percent_used = (rows_loaded / rows_expected) * 100               
dataset_name = input("Enter dataset name: ")

print()
print("=" * 34)
print(f"   RECORD CHECK  -  {dataset_name}") 
print("=" * 34)
print(f"   Rows Loaded    : {rows_loaded:>+10.2f}")
print(f"   Rows Expected  : {rows_expected:>+10.2f}")
print(f"   Free           : {free:>+10.2f}")
print(f"   Percent        : {percent_used:>+10.2f} %")
print(f"   % Free         : {percent_free:>+10.2f} %")
print("=" * 34)

