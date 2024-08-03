from pony.orm import *
from pony.orm.core import sql_logger

db = Database()

sqlite = dict(
    provider='sqlite',
    filename='uakino.db',
    create_db=True
)

mysql = dict(
    provider='mysql',
    host='localhost',
    user='root',
    passwd='root',
    db='uakino'
)

class Items(db.Entity):
    id = PrimaryKey(int, auto=True)
    title_ua = Optional(str)
    title_or = Optional(str)
    type_src = Optional(str)
    year = Optional(str)
    director = Optional(str)
    description = Optional(str)
    poster = Optional(str)
    json = Optional(str)
    imdb = Optional(str)
    links = Set('Links')

class Seasons(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(int)
    name = Optional(str)
    season = Optional(str)
    title = Optional(str)
    links = Set('Links')

class Links(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(int)
    series_id = Optional(int)
    quality = Optional(str)
    its_work = Optional(str)
    type_src = Optional(str)
    m3u_links = Optional(str)
    subs = Optional(str)
    item = Optional(Items)
    season = Optional(Seasons)

db.bind(**sqlite)
# db.bind(**mysql)  
db.generate_mapping(create_tables=True)
set_sql_debug(True)

@db_session
def check_in_base(table, condition):
    if table == 'Items':
        return select(item for item in Items if eval(condition))[:]
    elif table == 'Seasons':
        return select(season for season in Seasons if eval(condition))[:]
    elif table == 'Links':
        return select(link for link in Links if eval(condition))[:]
    else:
        raise ValueError("Unknown table")

@db_session
def add_to_db(table, data):
    if table == 'Items':
        Items(**data)
    elif table == 'Seasons':
        Seasons(**data)
    elif table == 'Links':
        Links(**data)
    else:
        raise ValueError("Unknown table")

@db_session
def add_m3u(link_id, m3u_link):
    link = Links.get(id=link_id)
    if link:
        link.m3u_links = m3u_link
    else:
        raise ValueError("Link not found")

@db_session
def save():
    pass