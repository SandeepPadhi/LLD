"""
You are given a string expression which consists of several comma separated tokens 
enclosed within opening ('{') and closing ('}') curly braces.
The string expression might or might not have a prefix before opening curly brace('{') and
a suffix after closing curly brace ('}').
You have to return a list of strings as output for each comma separated item as shown below in the examples. 

Example 1: 
Input = "/2022/{jan,feb,march}/report"
Output = "/2022/jan/report"
		 "/2022/feb/report"
		 "/2022/march/report"
		 
Example 2: 
Input = "over{crowd,eager,bold,fond}ness"
Output = "overcrowdness"
		 "overeagerness"
		 "overboldness"
		 "overfondness"
		 
Example 3: 
Input = "read.txt{,.bak}"
Output = "read.txt"
		 "read.txt.bak"

"""

input_arr=["over{crowd,eager,bold,fond}ness","read.txt{,.bak}", "/2022/{jan,feb,march}/report"]


def parse(input_str):
    print(f"\n\ninput_str:{input_str}")
    i=0
    j=len(input_str)-1
    suffix=""
    while input_str[i]!="{":
        i+=1
    prefix=input_str[:i]
    
    while input_str[j]!="}":
        j-=1
    suffix=input_str[j+1:]
    
    for element in input_str[i+1:j].split(","):
        print(f"{prefix}{element}{suffix}")
    
    
for input_str in input_arr:
    parse(input_str)


