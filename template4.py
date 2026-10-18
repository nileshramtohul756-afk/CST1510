"""
RECORD CHECK  -  my version
===========================

Name  : Ramtohul Pouroushottam
Lane  :  AI 
Date  : 17/10/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value,limit):
    """Calculates and returns the ddifference, percentage and status"""
    difference = limit - value
    percent = (value/limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    

    return difference, percent, status          


def print_report(label, value, limit, difference, percent, status):
    """print the final output report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Rows Loaded   : {value:>10.2f}")
    print(f"  Rows Expected : {limit:>10.2f}")
    print(f"  Difference    : {difference:>10.2f}")
    print(f"  Percent       : {percent:>10.2f}")
    print(f"  Status        : {status:>10}")
    print("=" * 34)

def load_records(path):
    """Reads label,value,limit from file and returns a list of dicts"""
    record = []
    try:
        with open(path) as f:
            for content in f:
                label, value, limit = content.strip().split(",")
                value = float(value)
                limit = float(limit)
                record.append({
                    "label" : label,
                    "value" : value,
                    "limit" : limit
                })
    except FileNotFoundError:
        print(f"FILE HAS NOT BEEN CREATED : {path}")
    return record

records = load_records("my_data.txt")
for line in records:
    dataset_name = line["label"]
    rows_loaded = line["value"]
    rows_expected = line["limit"]

    difference, percent, status = check_record(rows_loaded, rows_expected)

    print_report(dataset_name, rows_loaded, rows_expected, difference, percent, status)










