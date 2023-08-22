# REST API на Flask
___
API для поиска фильмов.
## data.py
Файл содержит словарь данных.
## app/models.py
Здесь находятся модели SQLAlchemy, схемы для сериализации.
## app/config.py
Файл содержит необходимые конфиги
## app/database.py
Здесь находится экземпляр класса SQLAlchemy.
## app/views
В папке находятся представления, описанные ниже
## main.py
Файл для запуска приложения.

### Эндпойнты такие:
#### Movie
GET /movies/ - все фильмы \
POST /movies/ - добавление нового фильма 

GET /movies/<int: nid> - фильм с идентификатором nid \
PUT /movies/<int: nid> - обновление фильма с идентификатором nid \
DELETE /movies/<int: nid> - удаление фильма с идентификатором nid
#### Genre
GET /genres/ - все жанры \
POST /genres/ - добавление нового жанра 

GET /genres/<int: nid> - жанр с идентификатором nid \
PUT /genres/<int: nid> - обновление жанра с идентификатором nid \
DELETE /genres/<int: nid> - удаление жанра с идентификатором nid
#### Director
GET /directors/ - все режиссеры \
POST /directors/ - добавление нового режиссера 

GET /directors/<int: nid> - режиссер с идентификатором nid \
PUT /directors/<int: nid> - обновление режиссера с идентификатором nid \
DELETE /directors/<int: nid> - удаление режиссера с идентификатором nid

## Зависимости
Зависимости лежат в requirements.txt. Для установки используйте в терминале команду:
pip install -r requirements.txt