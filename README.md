
<h2 align="center">Приложение трекер полезных привычек.</h2>

<!-- USAGE EXAMPLES -->
## Usage

Перед запуском web-приложения создайте базу данных, создайте и примените миграции, установите необходимые пакеты из файла requirements.txt и заполните файл .env по образцу .env.example. Используйте команду "python manage.py csu" для создания суперпользователя. Для запуска используйте команду "python manage.py runserver" либо через конфигурационные настройки PyCharm.


### Docker 
Создать образы и контейнеры DOCKER с помощью команд: "docker-compose build" и "docker-compose up".


## Структура проекта

config/

    settings.py - настройки приложений
    urls.py - файл маршрутизации
    celery.py - настройки Celery

tracker/

    migrations/
        папка с миграциями
    admin.py - настройки админки
    pagination.py - пагинация
    permissions.py - права доступа
    models.py - модели приложения
    serializers.py - сериализаторы
    tasks.py - отложенные и периодические задачи
    tests.py - тесты
    urls.py - файл маршрутизации приложения
    validatots.py - валидация
    views.py - контроллеры

users/

    management/commands
        csu - кастомная команда создания суперпользователя
        create_user - создать юзера через терминал
        telebot - отправка  сообщения в Telegram
    admin.py - настройки админки
    serializers.py - сериализаторы
    models.py - модели приложения
    tests.py - тесты
    urls.py - файл маршрутизации приложения
    views.py - контроллеры

.gitignore - Git файл.

Dockerfile
docker-compose.yaml - Docker файлы.

env.example - пример заполнения переменных окружения.

manage.py - точка входа веб-приложения

requirements.txt - список зависимостей для проекта.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

kettariec@gmail.com

https://github.com/Kettariec/course_work_drf/