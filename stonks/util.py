""""""
from math import floor
import datetime
import time


def convert_unix_timestamp_to_local_datetime(unix_timestamp: int) -> str:
    """"""
    unix_timestamp = int(unix_timestamp)
    unix_datetime = str(datetime.datetime.fromtimestamp(unix_timestamp))
    return unix_datetime


def convert_unix_timestamp_to_UTC_datetime(unix_timestamp: int) -> str:
    """Expected input: timestamp in seconds from UNIX epoch"""
    unix_timestamp = int(unix_timestamp)
    utc_datetime = str(datetime.datetime.utcfromtimestamp(unix_timestamp))
    return utc_datetime


def convert_datetime_to_timestamp(dt: str) -> int:
    """"""
    x = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    y = int(time.mktime(x))
    # datetime.datetime(dt)

    return y


def get_UNIX_timestamp_now() -> int:
    """Returns the floor of the current unix timestamp"""
    return floor(time.time())


if __name__ == '__main__':
    time_now = get_UNIX_timestamp_now()
    print(f'time now: {time_now}')
    print(f'Local datetime now: {convert_unix_timestamp_to_local_datetime(time_now)}')
    print(f'UTC datetime now: {convert_unix_timestamp_to_UTC_datetime(time_now)}')
    dt_example = '2020-08-28 17:01:41'
    print(f'Current datetime to stamp: current datetime = {dt_example} / '
          f'resulting stamp: {convert_datetime_to_timestamp(dt_example)}')

