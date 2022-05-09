## Описание программы:
Программы выводит совпадения товаров из маркет плесов по предоставленым данным.
Сначала достает все бренды из базы данных, затем к каждому бренду берет те товары которые ему пренадлежат, разбивая по маркетплейсам.
Берет имена продуктов одного маркет плейса и сравнивает с другим маркет плейсом елси совпадение есть то печает его в консоль.
Способ довольно не быстрый но благодоря фильтрации по брендам и совпадению получается максимально точно совпадение которое может быть.


## Запуск программы

Клонируйте репозиторий: 
 
``` 
https://github.com/emuhich/marketplace.git
``` 

Перейдите в папку проекта в командной строке:

``` 
cd hw05_final
``` 

Создайте и активируйте виртуальное окружение:

``` 
python -m venv venv
``` 
``` 
venv/Scripts/activate
``` 

Установите зависимости из файла *requirements.txt*: 
 
``` 
pip install -r requirements.txt
``` 

Укажите данные для подключения к БД в файле config.py: 
 
``` 
host = "хост"
user = "имя пользователя"
password = "пароль"
db_name = "имя БД"
``` 

Для старта пропишите команду: 
 
``` 
python main.py
``` 

