def get_gender(gender='unknown'):
    if gender is 'm':
        gender='Male'
    elif gender is 'f':
        gender='Female'
    print(gender)

get_gender('m')
get_gender('f')
get_gender()