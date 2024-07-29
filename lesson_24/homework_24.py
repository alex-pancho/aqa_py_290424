"""Завдання на створення моделі з допомогою Pony ORM:

1. Створіть базу даних, яка має три таблиці:

    - Таблиця `Items`:
        - Поле `id` - первинний ключ (Primary Key), автоінкрементне ціле число.
        - Поля `title_ua`, `title_or`, `type_src`, `year`, `director`, `description`, `poster`, `json`, `imdb` - строкові поля.

    - Таблиця `Seasons`:
        - Поле `id` - первинний ключ (Primary Key), автоінкрементне ціле число.
        - Поля `source_id`, `name`, `season`, `title` - строкові поля.

    - Таблиця `Links`:
        - Поле `id` - первинний ключ (Primary Key), автоінкрементне ціле число.
        - Поля `source_id`, `series_id`, `quality`, `its_work`, `type_src`, `m3u_links`, `subs` - строковий тип полів.

2. Зв'яжіть моделі між собою:

    - В `Items` існує зв'язок один-до-багатьох з `Links` через поле `id`.
    - В `Seasons` існує зв'язок один-до-багатьох з `Links` через поле `source_id`.

3. Задайте параметри бази данихякі можна передавати до функції `db.bind()`:

    - Для MySQL:
        - Постачальник: 'mysql'
        - Хост: 'localhost'
        - Користувач: 'root'
        - Пароль: 'root'
        - Назва бази даних: 'uakino'

    - Для SQLite:
        - Постачальник: 'sqlite'
        - Назва файлу: 'uakino.db'
        - Створити базу даних, якщо її не існує.
4. Використовуйте декоратори `@db_session` для функцій `check_in_base`, `add_to_db`, `add_m3u`, та `save`, щоб забезпечити їхню роботу в межах транзакцій.
"""

from pony.orm import Database, Required, PrimaryKey, Set, select, db_session
db = Database()
class Items(db.Entity):
    id = PrimaryKey(int, auto=True)
    title_ua = Required(str)
    title_or = Required(str)
    type_src = Required(str)
    year = Required(str)
    director = Required(str)
    description = Required(str)
    poster = Required(str)
    json = Required(str)
    imdb = Required(str)
    links = Set('Links')

class Seasons(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(str)
    name = Required(str)
    season = Required(str)
    title = Required(str)
    links = Set('Links')

class Links(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(str)
    series_id = Required(str)
    quality = Required(str)
    its_work = Required(str)
    type_src = Required(str)
    m3u_links = Required(str)
    subs = Required(str)
    item = Required(Items)
    season = Required(Seasons)

def bind_database(provider='sqlite', **kwargs):
    if provider == 'mysql':
        db.bind(provider=provider, host='localhost', user='root', passwd='root', db='uakino')
    elif provider == 'sqlite':
        db.bind(provider=provider, filename='uakino.db', create_db=True)
    else:
        raise ValueError("Unsupported provider")

bind_database(provider='sqlite')
db.generate_mapping(create_tables=True)


@db_session
def check_in_base(entity, **kwargs):
    result = select(e for e in entity if all(getattr(e, k) == v for k, v in kwargs.items()))[:]
    return result

@db_session
def add_to_db(entity, **kwargs):
    return entity(**kwargs)

@db_session
def add_m3u(link_id, m3u_link):
    link = Links[link_id]
    link.m3u_links = m3u_link

@db_session
def save(entity):
    entity.flush()


