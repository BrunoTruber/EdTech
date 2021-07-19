
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')

def datas(com_string):
    try:
        datetime.strptime(com_string, '%d/%m/%Y')
    except ValueError:
        print('NULL')
        return None
        
    else:
        data_ = datetime.strptime(com_string, '%d/%m/%Y')
        return datetime.strftime(data_, '%d de %B de %Y')
dt = input('digite a data no formato DD/MM/AAAA: ')
dt_str = datas(dt)

if dt_str is not None:
    print(dt_str)
####################################
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')

def datas(com_string):
    try:
        datetime.strptime(com_string, '%d/%m/%Y')
    except ValueError:
        print('NULL')
        return None
        
    else:
        data_datetime = datetime.strptime(com_string, '%d/%m/%Y')
        return datetime.strftime(data_datetime, '%d de %B de %Y')
dt = input('digite a data no formato DD/MM/AAAA: ')
dt_str = datas(dt)

if dt_str is not None:

    print(dt_str)