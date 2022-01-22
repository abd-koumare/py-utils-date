import datetime


def get_number_of_months(start_date, end_date):
    return (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)


def get_number_of_days(start_date, end_date):
    return (end_date - start_date).days


def get_weekdays_dates(start_date, end_date):
    weekdays_dates = []
    for date in daterange(start_date, end_date):
        if date.isoweekday() >= 6:
            weekdays_dates.append(date)
    return weekdays_dates


# daterange is exclusive like regular range end_date + timedelta(days=1) to make it inclusive
def daterange(start_date, end_date):
    for x in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(x)


def merge_date_list(l1, l2):
    return set(l1 + l2)
