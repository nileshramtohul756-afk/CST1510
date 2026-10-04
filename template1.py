"""
RECORD CHECK  -  my version
===========================

Name  :Ramtohul Pouroushottam
Lane  :  AI     
Date  :29/09/2026


"""

used = 87
total = 120
free = total - used
percent_used = (used / total) * 100            


print()
print("=" * 34)
print("   RECORD CHECK  -  srv-01") 
print("=" * 34)
print(f"   Used        : {used:>+10.2f}")
print(f"   Total       : {total:>+10.2f}")
print(f"   Free        : {free:>+10.2f}")
print(f"   Percent     : {percent_used:>+10.2f}%")
print("=" * 34)