# test-app
Приложение на тестовое задание

1. Структура разработана с учётом того, что контент в будущем может расширяться. 
   Общие поля и методы контента вынесены в родительский класс.  

2. Сделано API на 2 эндпойнта:
   
    * api/pages/ - список всех страниц с пагинацией. Пагинация установлена на 2 страницы в settings.py.
    В ответе содержится список страниц со всеми полями и ссылкой на API с детальной информацией по страцице.
      
    * api/pages/<pk> - детальная информация о странице. Помимо всех полей страницы содержит поля всех привязанных 
    объектов.

3. При обращении к API страницы счётчик просмотров каждого вида контента увеличивается на единицу. 
   У каждого объекта - свой счётчик. Реализовано через атомарную транзакцию. 
   Выполнение транзакции выполняется с помощью библиотеки очередей django-rq с использованием Redis.
   
4. В админке поиск страниц происходит по полю title собственному и всех завимимых объектов. 
   Например - можно найти все страницы в которых контент называется "Видео 1". 
   Привязка контента к страницам реализована через filter_horizontal с поиском контента по title.



## Установка

0. Необходимые требования:
   * [Redis](https://redis.io/) >= 3.0.0.   
   Для фоновых задач используется библиотека очередей [django-rq](https://github.com/rq/django-rq) -> 
   она использует лёгкую библиотеку [RQ](https://python-rq.org/) которая использует [Redis](https://redis.io/). 
   Сервер Redis должен быть запущен.

1. [Клонируйте репозиторий](https://help.github.com/en/articles/cloning-a-repository) на свой компьютер
```git clone https://github.com/NineMan/test_app.git```
```cd test_app```

2. Создайте и активируйте [виртуальное окружение](https://virtualenv.pypa.io) в каталоге репозитория
```
python3 -m venv env
source env/bin/activate
```

3. [Установите зависимости](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
```pip install -r requirements.txt```

4. [Примените миграции](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-migrate)
```python manage.py migrate```

5. [Загрузите тестовые данные](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-loaddata)
```python manage.py loaddata pages```

6. Запустите проект и откройте в браузере адрес http://localhost:8000/api/pages/
```python manage.py runserver```
