import re
import json

logs = [
    "[1678886400] INFO [network] - Connection established",
    "[1678886500] WARNING [database] - Query slow",
    "[1678886600] ERROR [application] - Exception occurred",
    "[1678886900]    DEBUG   [system]   -   System is running",
]

def parse_log(log):
    match = re.match(r"\[(\d+)\]\s+(\w+)\s+\[(\w+)\]\s+-\s+(.*)", log)
    if match:
        timestamp, level, module, message = match.groups()
        return {
            "timestamp": int(timestamp),
            "level": level,
            "module": module,
            "message": message
        }
    else:
        return None

def parse_logs(logs_array):
    result_logs_array = [parse_log(log) for log in logs_array if parse_log(log)]
    return result_logs_array

def output(outlogs):
    return json.dumps(outlogs, indent=1, check_circular=True, sort_keys=True)

def filter_logs(parsed_logs, filters):
    def log_matches_filter(log):
        for key, value in filters.items():
            if key == "level" and log["level"] != value:
                return False
            if key == "module" and log["module"] != value:
                return False
            if key == "min_timestamp" and log["timestamp"] < value:
                return False
            if key == "max_timestamp" and log["timestamp"] > value:
                return False
            if key == "message" and value not in log["message"]:
                return False
        return True

    return [log for log in parsed_logs if log_matches_filter(log)]

def main():
    filters = {
        "level": "WARNING",
        "min_timestamp": 1678886500,
        "message": "Query"
    }
    parsed_logs = parse_logs(logs)
    print(output(filter_logs(parsed_logs, filters)))

main()