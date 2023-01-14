# Доработать парметризованный декоратор logger в коде ниже. 
# Должен получиться декортор, который записывает в файл 'main.log':
# -дату и время вызова функции,
# -имя функции, 
# -аргументы, с которыми вызвалась 
# - возвращаемое значение. 
# Путь к файлу должен передаваться в аргументах декоратора. 
# Функция test_2 в коде ниже также должна отработать без ошибок.
import os
from datetime import datetime
import functools 

def logger(path):
    def __logger(old_function):
        @functools.wraps(old_function)
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            results = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(f'\nДата и время: {date_time}\n'
                        f'\nВызываем {old_function.__name__} c аргументами {args} и {kwargs}\n'
                        f'\nВозвращаемое значение:{results}\n')
                return results
        return new_function
    return __logger


def test_2():

    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b
        
        @logger(path)
        def div(a, b):
            return a / b
        
        @logger(path)
        def isinstance(a, int):
            return a
        

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)
      

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path, 'a', encoding='utf-8') as log_file:
            log_file.write(summator.__name__)

        assert 'summator', 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            item=str(item)
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f'\n{item}\n')


if __name__ == '__main__':
    test_2()
   
      
