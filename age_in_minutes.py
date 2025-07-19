from datetime import date
from datetime import datetime
from datetime import timedelta
import inflect
import sys


# converts dates into minute
class Count_date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def conv_date(self):
        date_time = datetime(self.year, self.month, self.day)
        return date_time

# take input and pass  into process and then into count_min
def main():

    d = input("Date of Birth: ")

    date1 = process(d)
    today = process_date(date.today())
    diff = today - date1
    secs = round(diff.total_seconds())
    mins = round(secs / 60)
    print(f"{inflect.engine().number_to_words(mins, andword="").capitalize()} minutes")

# return date in y,m,d format to main
def process_date(d):
    dates = d.strftime("%m/%d/%Y")
    month, day, year = dates.split("/")
    d1 = Count_date(int(year), int(month), int(day))
    return d1.conv_date()


def process(d):
    try:
        year, month, day = d.split("-")
    except ValueError:
        sys.exit("Invalid format")
    secs = Count_date(int(year), int(month), int(day))
    return secs.conv_date()


if __name__ == "__main__":
    main()
