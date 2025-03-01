"""
"2023-10-26 10:00:00|192.168.1.10|10.0.0.1|TCP|80|443|2023-10-26 10:05:00|192.168.1.20|10.0.0.2|UDP|53|2023-10-26 10:10:00|192.168.1.30|10.0.0.3|TCP|22|2023-10-26 10:15:00|192.168.1.40|10.0.0.4|TCP|8080"
"""

import re

input_str="2023-10-26 10:00:00|192.168.1.10|10.0.0.1|TCP|80|443|2023-10-26 10:05:00|192.168.1.20|10.0.0.2|UDP|53|2023-10-26 10:10:00|192.168.1.30|10.0.0.3|TCP|22|2023-10-26 10:15:00|192.168.1.40|10.0.0.4|TCP|8080"


date_regx=r"20[0-9]{2}-(0[1-9]|1[0-2])-[0-9]{2}"
entries=list(map(lambda x:x.strip(),input_str.split("|")))

i=0
ans=[]
while i<len(entries):
    entry=entries[i]
    if re.search(date_regx,entry) :
        protocol=entries[i+3]
        date=entries[i]
        source_ip=entries[i+1]
        destination_ip=entries[i+2]
        if protocol=="TCP":
            val=f"{source_ip}->{destination_ip} {date}"
            ans.append((date,val))
            i+=3
    i+=1
    
ans.sort()
for line in ans:
    print(line[1])
    
    

