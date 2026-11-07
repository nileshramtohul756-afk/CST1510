"""
RECORD CHECK  -  my version
===========================

Name  : Ramtohul Pouroushottam
Lane  :  AI 
Date  : 22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
class Record:
    over_limit_count = 0

    def __init__(self, dataset_name, rows_loaded, rows_expected):
        self.label = dataset_name
        self.value = rows_loaded
        self.limit = rows_expected

    def status(self):
             """Returns OVER LIMIT, WARNING or OK depending on value of percent"""
             p = (self.value)/(self.limit) * 100
             if p >= 100:
                  return "OVER LIMIT"
             elif p >= 90:
                  return "WARNING"
             else:
                  return "OK"

    def check(self):
         """When rows_loaded > rows_expected, over limit count increases by 1"""
         if self.value > self.limit:
           Record.over_limit_count += 1


records = []   

def load_records(path):
     records = []
     with open(path) as f:
          for line in f:        # Reads label,value and limit from file
               label,value,limit = line.strip().split(",")
               records.append(Record(label, float(value), float(limit)))
     return records       


records = load_records("my_data.txt")          #loads the records from the file


total_over_limit = 0


for record in records:
    status = record.status()
    if status == "OVER LIMIT":
             total_over_limit += 1
    
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"Rows Loaded  : {record.value:>10.2f}")
    print(f"Rows Expected: {record.limit:>10.2f}")
    print(f"status       : {record.status():>10}")
    
    print("=" * 34)

print(f"Total records OVER LIMIT: {total_over_limit}")
