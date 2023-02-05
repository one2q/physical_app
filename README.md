## Тестовое задание для Backend-разработчика от Physical Transformation

## Задача
#### 1) Создать 2 модели с полями:
- Модель Post:
     заголовок,
     текст поста,
     количество просмотров,
     дата создания.

- Модель Comment связанная с моделью Post:
     текст комментария,
     дата создания.

#### 2) Реализовать создание постов и комментариев через админку

#### 3) Написать API для получения списка постов и просмотра отдельного поста.

##### API списка постов: 

внутри элемента поста вывести последний комментарий поста с параметрами pk, text.

##### API получения отдельного поста:

реализовать увеличение счётчика просмотров поста (при получении данных о посте увеличивать кол-во просмотров);
добавлять данные о всех комментариях, относящихся к посту.

### Зависимости

- Django - 4.1.6
- djangorestframework - 3.14.0
- djangorestframework - 3.14.0
- psycopg2 - 2.9.5
- pytest-django - 4.5.2
- python-dotenv - 0.21.1
- requests - 2.28.2
- drf-yasg - 1.21.4
### Запуск приложения
1) git clone https://github.com/one2q/physical_app
2) переименуйте .env.ci файл на .env
3) запустите docker-compose up -d --build
4) http://127.0.0.1:8000

### Документация 
- swagger  url http://127.0.0.1:8000/swagger/


### Createsuperuser
Для создания пользователя используйте команды:
1) docker-compose exec web bash
2) python manage.py createsuperuser

### Запуск тестов
1) docker-compose exec web bash
2) pytest

