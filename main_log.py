
# Доработать декоратор logger в коде ниже. 
# Должен получиться декортор, который записывает в файл 'main.log':
# -дату и время вызова функции,
# -имя функции, 
# -аргументы, с которыми вызвалась 
# - возвращаемое значение. 
# Функция test_1 в коде ниже также должна отработать без ошибок.
import os
from datetime import datetime
import functools 

def logger(old_function):
    @functools.wraps(old_function)
    def new_function(*args, **kwargs):
        date_time = datetime.now()
        results = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'\nДата и время: {date_time}\n'
                       f'\nВызываем {old_function.__name__} c аргументами {args} и {kwargs}\n'
                       f'\nВозвращаемое значение:{results}\n')
        return results

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    
    @logger
    def div(a, b):
        return a / b
    
    @logger
    def isinstance(a, int):
        return a
     

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'
   
    
    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, 'a', encoding='utf-8') as log_file:
        log_file.write(summator.__name__)
        
  
    for item in (4.3, 2.2, 6.5):
        item=str(item)
        with open(path, 'a', encoding='utf-8') as log_file:
            log_file.write(f'\n{item}\n')
      
if __name__ == '__main__':
    test_1()