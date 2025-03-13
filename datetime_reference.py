import time
import datetime

# --- time.time() ---
print("--- time.time() ---")
start_time = time.time()
time.sleep(1)  # Simulate some work
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")

# --- datetime.datetime ---
print("\n--- datetime.datetime ---")
now = datetime.datetime.now()
print(f"Current datetime: {now}")

# Creating datetime objects
dt_from_values = datetime.datetime(2024, 12, 25, 10, 30, 0)
print(f"Datetime from values: {dt_from_values}")

dt_from_iso = datetime.datetime.fromisoformat("2024-11-15T15:45:00")
print(f"Datetime from ISO: {dt_from_iso}")

dt_from_timestamp = datetime.datetime.fromtimestamp(time.time())
print(f"Datetime from timestamp: {dt_from_timestamp}")

# Formatting datetime objects
formatted_dt = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime: {formatted_dt}")

# Datetime calculations
future_dt = now + datetime.timedelta(days=7, hours=12)
print(f"Future datetime: {future_dt}")

diff = future_dt - now
print(f"Time difference: {diff}")

# Accessing components
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}, Hour: {now.hour}")

# Replacing components
replaced_dt = now.replace(minute=0, second=0)
print(f"Replaced datetime: {replaced_dt}")

# --- datetime.date ---
print("\n--- datetime.date ---")
today = datetime.date.today()
print(f"Today's date: {today}")

date_from_iso = datetime.date.fromisoformat("2024-11-15")
print(f"Date from ISO: {date_from_iso}")

# Date calculations
future_date = today + datetime.timedelta(days=30)
print(f"Future date: {future_date}")

# --- datetime.time ---
print("\n--- datetime.time ---")
current_time = datetime.datetime.now().time()
print(f"Current time: {current_time}")


time_from_values = datetime.time(16, 15, 30)
print(f"Time from values: {time_from_values}")

# accessing time components
print(f"Hour: {current_time.hour}, Minute: {current_time.minute}, Second: {current_time.second}")

print(f"str : {str(datetime.datetime.now().time())}")





##########################################################################

# To get input in specific format

from datetime import datetime

def parse_datetime_ymd_hms(datetime_string):
    """Parses datetime in YYYY-MM-DD HH:MM:SS format."""
    try:
        return datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None

def parse_datetime_mdy_hms(datetime_string):
    """Parses datetime in MM-DD-YYYY HH:MM:SS format."""
    try:
        return datetime.strptime(datetime_string, "%m-%d-%Y %H:%M:%S")
    except ValueError:
        return None

def parse_datetime_iso(datetime_string):
    """Parses datetime in ISO 8601 format (YYYY-MM-DDTHH:MM:SS)."""
    try:
        return datetime.fromisoformat(datetime_string)
    except ValueError:
        return None

def parse_datetime_mdy_hm(datetime_string):
    """Parses datetime in MM/DD/YYYY HH:MM format."""
    try:
        return datetime.strptime(datetime_string, "%m/%d/%Y %H:%M")
    except ValueError:
        return None

# Example usage
datetime_str_ymd_hms = "2023-11-15 14:30:45"
dt_obj_ymd_hms = parse_datetime_ymd_hms(datetime_str_ymd_hms)
print(f"'{datetime_str_ymd_hms}': {dt_obj_ymd_hms}")

datetime_str_mdy_hms = "11-15-2023 14:30:45"
dt_obj_mdy_hms = parse_datetime_mdy_hms(datetime_str_mdy_hms)
print(f"'{datetime_str_mdy_hms}': {dt_obj_mdy_hms}")

datetime_str_iso = "2023-11-15T14:30:45"
dt_obj_iso = parse_datetime_iso(datetime_str_iso)
print(f"'{datetime_str_iso}': {dt_obj_iso}")

datetime_str_mdy_hm = "11/15/2023 14:30"
dt_obj_mdy_hm = parse_datetime_mdy_hm(datetime_str_mdy_hm)
print(f"'{datetime_str_mdy_hm}': {dt_obj_mdy_hm}")

# Example with invalid format
invalid_datetime_str = "15/11/2023 14:30:45"
invalid_dt_obj = parse_datetime_ymd_hms(invalid_datetime_str)
print(f"'{invalid_datetime_str}': {invalid_dt_obj}")
