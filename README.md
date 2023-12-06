# Fruktorum

Это Django-приложение для хранения закладок на веб-сайты пользователей.

## Запуск приложения

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/amriddinov-m/fruktorum.git
    ```

3. Перейдите в каталог с проектом:

    ```bash
    cd fruktorum
    ```

4. Запустите приложение с помощью Docker Compose:

    ```bash
    docker-compose up --build
    ```

5. После успешного запуска, приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

## Swagger API

После запуска приложения, вы можете ознакомиться с документацией к API, посетив [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## Завершение работы

Чтобы завершить работу приложения, выполните:

```bash
docker-compose down
