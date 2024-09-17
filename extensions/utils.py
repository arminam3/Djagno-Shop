from . import jalali

from django.utils import timezone

def english_numbers_convertor(number):
    persian_num = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e, p in persian_num.items():
        number = number.replace(e, p)
    return number

def jalali_convertor(time):
    time = timezone.localtime(time)

    j_month = [
        'فروردین',
        'اردیبهشت',
        'خرداد',
        ' تیر ',
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند'
    ]

    time_to_str = "{} {},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = "{}{}{} ,  ساعت{}:{}".format(
                                           time_to_tuple[2],
                                           j_month[time_to_tuple[1]-1],
                                           time_to_tuple[0],
                                           time.hour,
                                           time.minute if time.minute > 9 else f'0{time.minute}'
                                       )

    return english_numbers_convertor(output)