"""
Practical Question: Log File Analysis with Threading and Locking

Scenario:

You have a large log file (application.log) containing various log entries. Each line follows a consistent format:

[TIMESTAMP] [LEVEL] [MODULE] - MESSAGE
For example:

[2023-10-27 10:00:00] [INFO] [NETWORK] - Connection established
[2023-10-27 10:01:00] [ERROR] [DATABASE] - Connection failed
[2023-10-27 10:02:00] [WARNING] [SYSTEM] - Low disk space
[2023-10-27 10:03:00] [ERROR] [APPLICATION] - Invalid input
Your task is to:

Read the log file concurrently using multiple threading.
Use regular expressions to extract specific information from each log entry:
The LEVEL (e.g., "ERROR", "WARNING", "INFO").
The MESSAGE.
Count the occurrences of "ERROR" and "WARNING" messages.
Use a lock to ensure thread safety when updating the counts.
Requirements:

Create a function analyze_logs(log_file_path, num_threading) that takes the log file path and the number of threading as input.
Divide the log file into chunks that each thread will process.
Each thread should use regular expressions to extract the LEVEL and MESSAGE.
Use a threading.Lock to protect the shared counters for "ERROR" and "WARNING" messages.
Print the final counts of "ERROR" and "WARNING" messages.
Python Code Skeleton:

"""
import unittest
import re
import threading


FILE_NAME="log_file.txt"
error_count=0
warning_count=0
timestamp_pattern=r"\d{4}-{\d}{2}-\d{2}\s*\d{2}:\d{2}:\d{2}"
info_level_pattern=r"INFO"
error_level_pattern=r"ERROR"
warning_level_pattern=r"WARNING"
message_pattern=r"[A-Z][\w\s]+\n"


def insert():
    with open(FILE_NAME,'w') as f:
        f.write("[2023-10-27 10:00:00] [INFO] [NETWORK] - Connection established\n")
        f.write("[2023-10-27 10:01:00] [ERROR] [DATABASE] - Connection failed\n")
        f.write("[2023-10-27 10:02:00] [WARNING] [SYSTEM] - Low disk space\n")
        f.write("[2023-10-27 10:03:00] [ERROR] [APPLICATION] - Invalid input\n")


def analyzer(file,lock,threadno):
    global error_count,warning_count
    with lock:
        message=re.search(message_pattern,file)
        # print(f"threadno:{threadno} file:{file}")
        # print(f"threadno:{threadno} message:{message}")
        error_message=re.search(error_level_pattern,file)
        if error_message :
            print(f"thread no :{threadno} message:{message.group()} , level:{error_message.group()}")
            error_count+=1
            return
        warning_message=re.search(warning_level_pattern,file)
        if warning_message:
            print(f"thread no :{threadno} message:{ message.group()} , level:{warning_message.group()}")            
            warning_count+=1
            return
        info_message=re.search(info_level_pattern,file)
        if info_message:
            print(f"thread no :{threadno} message:{message.group()} , level:{info_message.group()}")   
            return         
        print()


def parse():
    try:
        lock=threading.Lock()
        with open(FILE_NAME,"r") as f:
            threadno=0
            tarr=[]
            for line in f:
                t=threading.Thread(target=analyzer ,args=(line,lock,threadno,))
                tarr.append(t)
                threadno+=1
            
            for t in tarr:
                t.start()
            
            for t in tarr:
                t.join()

    except FileNotFoundError as e:
        print(f"File not found:{e}")
            

def app():
    insert()
    parse()




# if __name__ == '__main__':
#     app()


import os

class TestLogThreads(unittest.TestCase):
    def testinsert(self):
        insert()
        self.assertTrue(os.path.exists(FILE_NAME))
        with open(FILE_NAME,"r") as f: 
            content=list(f.read().split("\n"))
            self.assertEqual(content[0],"[2023-10-27 10:00:00] [INFO] [NETWORK] - Connection established")
    def testapp(self):
        app()
        self.assertEqual(error_count,2)
        self.assertEqual(warning_count,1)


if __name__ == '__main__':
   unittest.main()