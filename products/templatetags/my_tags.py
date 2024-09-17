from django import template
from config.settings import LANGUAGE_CODE

register = template.Library()

@register.filter(name='e2f')
def english_numbers_convertor(number):

    triple = (len(str(number)) - 1) // 3
    f_number_list = list(str(number))
    jobran = 0
    if LANGUAGE_CODE ==('fa' or 'fa-ir'):
        # persian_num = {
        #     "0": "۰",
        #     "1": "۱",
        #     "2": "۲",
        #     "3": "۳",
        #     "4": "۴",
        #     "5": "۵",
        #     "6": "۶",
        #     "7": "۷",
        #     "8": "۸",
        #     "9": "۹",
        # }
        # for e, p in persian_num.items():
        #     # global f_number
        #     number = str(number).replace(e, p)
        #
        #
        # f_number_list = list(str(number))
        arabic = '۰۱۲۳۴۵۶۷۸۹'
        english = '0123456789'

        translation_table = str.maketrans(english, arabic)
        number = str(number).translate(translation_table)
    return number


    # for i in range(triple):
    #     f_number_list.insert(-((i+1)*3) + jobran, ',')
    #     jobran -= 1
    #
    # number_splited = ''
    # for j, index in enumerate(f_number_list):
    #     number_splited += f_number_list[j]
    #
    # return number_splited



@register.filter
def active_comment(comment):
    return comment.filter(active=True)

@register.filter(name='len')
def the_len(value):
    return value.len()