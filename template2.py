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


over_limit_count = 0

while True:
 dataset_name = input("Enter dataset name (type 'quit' to stop): ")
 if dataset_name == "quit":
    break

 rows_loaded = float(input("Enter rows loaded: "))
 rows_expected = float(input("Enter rows expected: "))
 free = rows_expected - rows_loaded    
 percent = (rows_loaded/rows_expected) * 100  
 if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1
 elif percent >= 90:
    status = "WARNING"
 else:
    status = "OK"    


 print()
 print("=" *34 )
 print(f"   RECORD CHECK  -  {dataset_name}")
 print("=" *34 )
 print(f"{" " * 2}Used{" " * 9}:{rows_loaded:>11.2f}")  
 print(f"{" " * 2}Total{" " * 8}:{rows_expected:>11.2f}")  
 print(f"{" " * 2}Free{" " * 9}:{free:>11.2f}")  
 print(f"{" " * 2}Percent{" " * 6}:{percent:>11.2f} %") 
 print(f"{" " * 2}Status{" " * 7}:{status:>11}")
 print("=" *34 )

print(f"Total record OVER LIMIT: {over_limit_count}")
