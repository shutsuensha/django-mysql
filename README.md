- Начало: 07.06.2025
- Завершение: 07.06.2025

### ⚙️ Технологии
- Django
- Mysql
- Docker
- Nginx
- DataTables


### Настройка в Docker

### Подготовка переменных окружения
Скопируйте файл **.env.example** в **.env** и заполните его следующим образом(пример):
```ini
MYSQL_DB_HOST=mysql_container
MYSQL_DB_PORT=3306
MYSQL_DB_USER=user
MYSQL_DB_PASS=password
MYSQL_DB_NAME=dbname
MYSQL_ROOT_PASSWORD=rootpassword
```

### Создание docker-сети
```bash
docker network create record-network
```

### Запуск сервиса основной БД
```bash
docker compose -f docker-compose-services.yml up -d
```

### Сборка образа Django-приложения
```bash
docker build -t django-image-record-app -f Dockerfile .
```

### Применение миграций
```bash
docker run --rm --network record-network --env-file .env django-image-record-app python manage.py migrate
```

### Запуск оброзов Django + Nginx
```bash
docker compose -f docker-compose.yml up -d
```

### Приложение
http://localhost/
