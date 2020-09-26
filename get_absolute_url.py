# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:01:37 2020

@author: lukin
"""

'''
Задача: написать функцию get_absolute_url принимающую:

1 обязательный аргумент url;
произвольное количество позиционных аргументов;
произвольное количество именованных аргументов.


Функция должна формировать полный url адрес из переданного домена и параметров:

Позиционные аргументы должны добавляться к переданному url через слэш '/';
После добавления всех позиционных аргументов добавляется знак вопроса ?;
После знака вопроса добавляются именованные аргументы по шаблону 'ключ=значение&'.

Вот пример работы функции:

print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))


Должен получиться результат:

www.yandex.ru/posts/news?id=24&author=admin
www.google.com/images?id=24&category=auto&color=red&size=small
'''
def get_absolute_url(abs_url, *args, **kwargs):
    string_url = abs_url
    for arguments in args:
        string_url += '/' + arguments
    for k, v in kwargs.items():
        string_url += '?' + k + '=' + v + '&'
    #в строке последний знак получился "&" обрезаем его
    string_url = string_url[:-1]
    #в строке получились пары '&?', а должно быть '&' делаем замену шаблона для этих пар
    string_url = string_url.replace('&?', '&')
    return string_url

#ЭТО ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ.
#ЛИБО НАПИСАТЬ ВЫВОД ФУНКЦИЙ СО СВОИМИ ПАРАМЕТРАМИ
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))
print(get_absolute_url('www.yandex.ru', 'posts', 'news', 'images', id='24', author='admin',  category='auto', color='red', size='small'))

