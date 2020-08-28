""""""
from math import floor
import datetime
import time
import warnings


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


def convert_datetime_to_timestamp(dt: str, tz_offset: int = 0) -> int:
    """"""
    warnings.warn('This function assumes that the input datetime is in UTC until the offset is IMPLEMENTED which it isnt')
    if not isinstance(tz_offset, int):
        raise TypeError(f'`tz_offset` expected to be integer but instead found type: {type(tz_offset)}')
    prefix = '-' if tz_offset < 0 else '+'

    time_struct_obj = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    unix_time = int(time.mktime(time_struct_obj))

    return unix_time


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

