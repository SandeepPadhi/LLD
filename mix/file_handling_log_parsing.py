"""
# Example log file creation for regex testing.
with open("logfile.txt", "w") as f:
    f.write("2023-11-20 10:00:00 - INFO - System started\n")
    f.write("2023-11-20 10:01:00 - ERROR - Database connection failed\n")
    f.write("2023-11-20 10:02:00 - WARNING - Low disk space\n")
    f.write("2023-11-20 10:03:00 - ERROR - Invalid user input\n")



"""

import re

logs=["2023-11-20 10:00:00 - INFO - System started\n","2023-11-20 10:01:00 - ERROR - Database connection failed\n",
"2023-11-20 10:02:00 - WARNING - Low disk space\n","2023-11-20 10:03:00 - ERROR - Invalid user input\n"]



def analyze(filename):
    try: 
        ans=[]
        with open(filename,"rt") as file:
            for line in file:
                entries=[entry.strip() for entry in  line.split(" - ")]
                print(f"entries: {entries}")  # Correct f-string
                match=re.search(r"ERROR",entries[1])
                if match :
                    print(f"match:{match}")
                    ans.append(entries[-1])
                
                
            return ans

    except FileNotFoundError:
        print("file not found")
    
    except Exception as e:
        print(f"exception occured as {e}")

filename="log_file.txt"
with open(filename,"w") as file:
    for log in logs:
        file.write(log)



print(analyze(filename))




s = "My phone number is 123-san-456-7890"
pattern = r"(\d{3})-san-(\d{3})-(\d{4})"  # Three captured groups

match = re.search(pattern, s)

if match:
    print("Entire match:", match.group(0))
    print("First group:", match.group(1))
    print("Second group:", match.group(2))
    print("Third group:", match.group(3))
else:
    print("No match found.")

match = re.match(pattern, s)
print(match)
