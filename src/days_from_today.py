from datetime import datetime, date

# Convert a string to a date object
def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None

# Get the number of days between a date and today
def get_days_from_today(date_str:str)->int:
    today = date.today()
    date_value = string_to_date(date_str)
    if date_value is None:
        return "Invalid date format"
    return (date_value - today).days


date_value = input("Enter a date in the format YYYY-MM-DD: ")
if not date_value:
    print("No date provided")
else:
    print(get_days_from_today(date_value))
