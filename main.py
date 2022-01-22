from utils import *


def test_get_number_of_days():
    d1 = datetime.date(2022, 1, 3)
    d2 = datetime.date(2022, 3, 24)
    print(f'from {d1} to {d2}: {get_number_of_days(d1, d2)} days(s)')


def test_get_number_of_months():
    d1 = datetime.date(2021, 1, 3)
    d2 = datetime.date(2022, 2, 12)
    print(f'from {d1} to {d2}: {get_number_of_months(d1, d2)} month(s)')


def test_daterange():
    d1 = datetime.date(2021, 1, 3)
    d2 = datetime.date(2022, 2, 12)
    print(f'from {d1} to {d2}: {list(daterange(d1, d2))}')


def test_get_weekdays_dates():
    d1 = datetime.date(2022, 2, 1)
    d2 = datetime.date(2022, 2, 28)
    print(f'from {d1} to {d2}: {len(get_weekdays_dates(d1, d2))} weekday(s)')


def test_merge_date_list():
    d1 = datetime.date(2022, 2, 1)
    d2 = datetime.date(2022, 2, 10)

    d3 = datetime.date(2022, 2, 1)
    d4 = datetime.date(2022, 2, 15)
    l1 = list(daterange(d1, d2 + datetime.timedelta(days=1)))
    l2 = list(daterange(d3, d4 + datetime.timedelta(days=1)))
    print(f'merge result: {len(merge_date_list(l1, l2))} day(s) expected: 15 days')


if __name__ == '__main__':
    test_merge_date_list()
