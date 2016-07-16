from datetime import date
Student{# - dict
    'name' : [Elijah Dennis Wekesa]
    'date_of_birth': datetime.datetime(2009, 10, 5, 18, 00)
    'phone_number': '0723918374' 
    }
def age():
	Student['date_of_birth']
    today = date.today()
    y = today.year - birthday.year
    if today.month < birthday.month or today.month == birthday.month and today.day < birthday.day:
        y -= 1
    return y


    # try: 
    #     birthday = born.replace(year=today.year)
    # except ValueError: # raised when birth date is February 29 and the current year is not a leap year
    #     birthday = born.replace(year=today.year, month=born.month+1, day=1)
    # if birthday > today:
    #     return today.year - born.year - 1
    # else:
    #     return today.year - born.year