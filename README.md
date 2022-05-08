Для разворачивания сервера
1. git clone https://github.com/zik59/Docker-and-fastapi
2. docker-compose up

После нужно проверить контейнеры и подключиться к сервису с беком
1.docker ps
2.docker exec -it {CONTAINER ID} sh
Добавить миграции в бд(обязательно)
alembic upgrade head

Пример POST запроса есть в файле test.py, также с его помощью можно проверить работу программы

Для подключения к бд
docker-compose exec db psql -h localhost -U postgres --dbname=postgres

Для чтения данных из таблицы
SELECT * FROM questions;

Проверено и запущено на Ubuntu 20.04 и  Windows 10