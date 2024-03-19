from datetime import datetime, timedelta


def get_current_time_str():
    datetime_format_str = '%y-%m-%d %H:%M:%S.%f'
    now_kst = datetime.utcnow() + timedelta(hours=9)
    current_time = now_kst.strftime(datetime_format_str)
    return current_time


if __name__ == '__main__':
    print('Hello World!')
    print(f'current time(KST): {get_current_time_str()}')
