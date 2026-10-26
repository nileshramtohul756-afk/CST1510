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

"""Calculates free rows, percentage of rows loaded, assigns a bordered report for each dataset and keeps track of how 
   many datasets were "OVER LIMIT".
"""
over_limit_count = 0



while True:     #starts an infinite loop to process many datasets in one session
 dataset_name = input("Enter dataset name (type 'quit' to stop): ")    # asks user for dataset name
 if dataset_name == "quit":
    break   # loop is broken if quit is entered

 rows_loaded = float(input("Enter rows loaded: "))
 rows_expected = float(input("Enter rows expected: "))
 free = rows_expected - rows_loaded      # calculates available rows
 percent = (rows_loaded/rows_expected) * 100    # calculates percentage of rows loaded

 # dertermines status based on the threshold of the percentage
 if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1    # increases the counter for over limit record  by 1
 elif percent >= 90:
    status = "WARNING"
 else:
    status = "OK"    


 # prints a bordered report based on the given dataset
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

print(f"Total record OVER LIMIT: {over_limit_count}") # prints the number of OVER LIMIT counted
