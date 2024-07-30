

from pony.orm import Database, Required, Set, db_session, PrimaryKey


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

# Параметри для MySQL
#def bind_mysql():
    #db.bind(provider='mysql', host='localhost', user='root', passwd='root', db='uakino')

# Параметри для SQLite
def bind_sqlite():
    db.bind(provider='sqlite', filename='uakino.db', create_db=True)

# необхідний провайдер
#bind_mysql()
bind_sqlite()

# Створення таблиць
db.generate_mapping(create_tables=True)

@db_session
def check_in_base(id):
    return Items.get(id=id) is not None

@db_session
def add_to_db(item_data):
    item = Items(**item_data)
    return item

@db_session
def add_m3u(link_data):
    link = Links(**link_data)
    return link

@db_session
def save():
    db.commit()
