"""
RECORD CHECK  -  my version
===========================

Name  : Ramtohul Pouroushottam
Lane  :  AI   
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("records_report.csv")  
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100

def status(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x >= 100 
                                   else ("WARNING" if x >= 90
                                           else "OK"))
                                 

non_ok_df = (df[df["status"] != "OK"])
print(non_ok_df)

status_counts = df.groupby("status").size()
print(status_counts)

df.to_csv("new_records_report.csv", index = False)

status_counts.plot(kind = "bar")
plt.title("Counts per Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.show()
plt.savefig("status_counts.png")

