

Название репозитория должно состоять из 4 букв латинского алфавита и от 1 до 5 цифр. Например: ydhr77. Не указывать в имени репозитория, именах коммитов тестовое задание, название тестового задания и прочие, чтобы другие кандидаты не могли найти в поисковике этот репозиторий. Тестовые задания, которые нарушают эти правила, приниматься не будут, кандидату с таким тестовым будет отказано.



файл .env:
MYSQL_DB_HOST=
MYSQL_DB_PORT=
MYSQL_DB_USER=
MYSQL_DB_PASS=
MYSQL_DB_NAME=
MYSQL_ROOT_PASSWORD=



docker network create record-network

docker compose -f docker-compose-services.yml up -d

docker build -t django-image-record-app -f Dockerfile .

docker run --rm --network record-network --env-file .env django-image-record-app python manage.py migrate

docker compose -f docker-compose.yml up -d

Приложение
http://localhost/