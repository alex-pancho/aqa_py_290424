from pony.orm import Database, Required, PrimaryKey, Set, db_session

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
    links = Set("Links")

class Seasons(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(str)
    name = Required(str)
    season = Required(str)
    title = Required(str)
    links = Set("Links")

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

# Прив'язка до бази даних (MySQL або SQLite)
db.bind(provider='sqlite', filename='uakino.db', create_db=True)
# db.bind(provider='mysql', host='localhost', user='root', passwd='root', db='uakino')

# Створення таблиць
db.generate_mapping(create_tables=True)

@db_session
def check_in_base(entity_class, **kwargs):
    """
    Перевіряє наявність запису в базі даних.
    """
    return entity_class.exists(**kwargs)

@db_session
def add_to_db(entity_class, **kwargs):
    """
    Додає новий запис у базу даних.
    """
    entity_class(**kwargs)

@db_session
def add_m3u(link_id, m3u_links):
    """
    Оновлює поле m3u_links для заданого запису Links.
    """
    link = Links[link_id]
    link.m3u_links = m3u_links

@db_session
def save():
    """
    Зберігає зміни в базі даних.
    """
    db.commit()