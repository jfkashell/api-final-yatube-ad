# API для Yatube

Yatube API - учебный REST API для социальной сети публикаций. Через API
можно читать и создавать посты, оставлять комментарии, просматривать
сообщества и подписываться на авторов.

Проект построен на Django REST Framework. Для аутентификации используются
JWT-токены: неавторизованные пользователи могут читать публикации,
комментарии и сообщества, а создание, изменение и удаление контента доступно
только авторизованным пользователям. Изменять и удалять можно только свои
посты и комментарии.

## Технологии

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite

## Установка

Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone <адрес_репозитория>
cd api-final-yatube-ad-main
```

Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate
```

Для Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Выполните миграции:

```bash
python yatube_api/manage.py migrate
```

Запустите сервер разработки:

```bash
python yatube_api/manage.py runserver
```

Документация API будет доступна по адресу:

```text
http://127.0.0.1:8000/redoc/
```

## Примеры запросов

Получить список публикаций:

```http
GET /api/v1/posts/
```

Создать JWT-токен:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "user",
  "password": "password"
}
```

Создать публикацию:

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Новая публикация",
  "group": 1
}
```

Добавить комментарий к публикации:

```http
POST /api/v1/posts/1/comments/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Комментарий к публикации"
}
```

Подписаться на автора:

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "following": "author_username"
}
```
