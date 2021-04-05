# test-app
Приложение по тестовому заданию

## Описание

1. Структура разработана с учётом того, что контент в будущем может расширяться. 
   Общие поля и методы контента вынесены в родительский класс.  

2. Сделано API на 2 эндпойнта:
   
    * api/pages/ - список всех страниц с пагинацией. Пагинация установлена в settings.py.
    В ответе содержится список страниц со всеми полями и ссылкой на API с детальной информацией по страцице.
      
    * api/pages/<pk> - детальная информация о странице. Помимо всех полей страницы содержит поля всех привязанных 
    объектов.

3. При обращении к API страницы счётчик просмотров каждого вида контента увеличивается на единицу. 
   У каждого объекта - свой счётчик. Реализовано через атомарную транзакцию. 
   Выполнение транзакции выполняется с помощью библиотеки очередей django-rq с использованием Redis.
   
4. Зайти в админку - admin:admin

5. В фикстурах загружено 8 страциц, с пагинацией по 2 страницы. 
   Также загружено по три экземпляра каждого вида контента: "Аудио", "Текст" и "Видео".
   Страница 4 -> привязан весь контент.
   Страница 6 -> контент не привязан.

5. В админке поиск страниц происходит по полю title собственному и всех завимимых объектов. 
   Например - можно найти все страницы в которых контент называется "Видео 1". 
   Привязка контента к страницам реализована через filter_horizontal с поиском контента по title.

## Установка

0. Необходимые требования:
   * [Redis](https://redis.io/) >= 3.0.0. Т.к. для фоновых задач используется 
     библиотека очередей [django-rq](https://github.com/rq/django-rq) -> она 
     использует лёгкую библиотеку [RQ](https://python-rq.org/) -> использует 
     [Redis](https://redis.io/). Сервер Redis должен быть запущен.

1. [Клонируйте репозиторий](https://help.github.com/en/articles/cloning-a-repository) на свой компьютер
```
git clone https://github.com/NineMan/test_app.git
cd test_app
```

2. Создайте и активируйте [виртуальное окружение](https://virtualenv.pypa.io) в каталоге репозитория
```
python3 -m venv env
source env/bin/activate
```

3. [Установите зависимости](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
```pip install -r requirements.txt```
   
4. Создайте ```.env``` файл (или переименуйте и измените ```.env.example```) в корне проекта и задайте переменные окружения для проекта:
```
touch .env
echo SECRET_KEY=$(openssl rand -hex 32) >> .env
echo ALLOWED_HOSTS='"127.0.0.1", "localhost"' >> .env
echo RQ_HOST=localhost >> .env
echo RQ_PORT=6379 >> .env
echo RQ_DB=0 >> .env
echo RQ_USER=admin >> .env
echo RQ_PASSWORD=some-password >> .env
echo RQ_TIMEOUT=360 >> .env
```

5. [Примените миграции](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-migrate)
```python manage.py migrate```

6. [Загрузите тестовые данные](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-loaddata)
```python manage.py loaddata data```

7. Запустите проект ```python manage.py runserver``` 
   
8. Откройте в браузере адрес http://localhost:8000/api/pages/
