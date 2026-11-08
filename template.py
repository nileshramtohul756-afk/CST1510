"""
RECORD CHECK  -  my version
===========================

Name  : Ramtohul Pouroushottam
Lane  :  IT
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Cleans and parses one messy line into a dictionary"""
    line = raw_line.strip().lower() # removes spaces and makes everything lowercase
    hostname_part, rest = line.split(",", 1) # splits only at the first comma to separate hostname from the rest
    hostname = hostname_part.strip()

    # loops through remaining key-value pairs and stores them as floats
    records = {}
    for content in rest.split(","):
        key, value = content.split("=")
        records[key.strip()] = float(value.strip())

    return {"hostname" : hostname, "used": records["used"], "total": records["total"]} # returns a dictionary

def status_of(used, total, warning_at = 90):
    """Returns OVER LIMIT, WARNING or OK"""
    percent = (used/total) * 100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

raw_records = []

with open("messy_lines.txt") as f: # opens the file
 raw_records = f.readlines()       # and loads all the lines into the raw_records list

total_records = 0
flagged_count = 0

for raw_record in raw_records: # loops through each messy line and checks the status
     record = parse_line(raw_record)
     status = status_of(record["used"], record["total"])

     print(f"{record} , {status}") # prints the dictionary with its status
    
     total_records += 1
     if status == "OVER LIMIT" or status == "WARNING":
         flagged_count += 1

print(f"{total_records} records and {flagged_count} flagged. ")         


