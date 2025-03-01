input_str="""

[database]
host=localhost
port=5432
# this is a comment
user=admin

[web]
port=8080
debug=true

timeout=10

"""
import re
from collections import defaultdict
import json

inputlines=[]
for docline in input_str.split("\n"):
    line=docline.strip()
    if line!="":
        inputlines.append(line)
        
setting_reg=r"^\[\w+\]$"
keyvalue_reg=r"\w+=\w+"

print(inputlines)

jsondict=defaultdict(None)
current_setting=None
for line in inputlines:
    if re.search(setting_reg,line):
        current_setting=line
        jsondict[current_setting]=defaultdict(str)
    elif re.search(keyvalue_reg,line):
        spanlist=re.findall("\w+",line)
        key=spanlist[0]
        value=spanlist[1]
        jsondict[current_setting][key]=value
    else:
        print(f"unknow entity:{line}")
        
ans=json.dumps(jsondict, indent=4)
print(ans)

print(re.findall("\w+",s))
            
        
        
    