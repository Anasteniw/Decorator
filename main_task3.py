import os
from datetime import datetime
import functools 

def logger(old_function):
    @functools.wraps(old_function)
    def new_function(*args, **kwargs):
        date_time = datetime.now()
        results = old_function(*args, **kwargs)
        with open('task_3.log', 'a', encoding='utf-8') as file:
            file.write(f'\nДата и время: {date_time}\n'
                       f'\nВызываем {old_function.__name__} c аргументами {args} и {kwargs}\n'
                       f'\nВозвращаемое значение:{results}\n')
        return results

    return new_function


def task_3():

    path = 'task_3.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    
    def some_HW(document):
        return document
    some_HW ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})

if __name__ == '__main__':
    task_3()