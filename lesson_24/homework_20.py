from pony.orm import Database, Required, PrimaryKey, Optional, Set, db_session


# Параметры подключения к БД
mysql_params = {
    'provider': 'mysql',
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'uakino'
}

sqlite_params = {
    'provider': 'sqlite',
    'filename': 'uakino.db',
    'create_db': True
}

# Инициализируем БД
db = Database()


# Оглашаем модели
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
    source_id = Optional(str)
    series_id = Optional(str)
    quality = Optional(str)
    its_work = Optional(str)
    type_src = Optional(str)
    m3u_links = Optional(str)
    subs = Optional(str)
    item = Required(Items)
    season = Required(Seasons)


# Связи между моделями
Items.links = Set(Links)
Seasons.links = Set(Links)


# Подключение к БД
def setup_database(provider_params):
    db.bind(**provider_params)
    db.generate_mapping(create_tables=True)


@db_session
def check_in_base(title_ua):
    # Проверим, существует ли элемент с заданным заголовком в БД
    item = Items.get(title_ua=title_ua)
    return item is not None


@db_session
def add_to_db(item_data):
    # Добавим новый элемент к БД
    item = Items(**item_data)
    return item


@db_session
def add_m3u(source_id, m3u_link):
    # Приводим source_id к строке
    source_id = str(source_id)
    # Добавить M3U ссылку к существующему элементу
    link = Links.get(source_id=source_id)
    if link:
        link.m3u_links = m3u_link
        return link
    return None


@db_session
def save():
    # Сохранить изменения в БД
    db.commit()


# Выбор БД для подключения
setup_database(sqlite_params)

if __name__ == '__main__':
    # Добавляем новый элемент
    new_item = {
        "title_ua": "Новий Фільм",
        "title_or": "New Movie",
        "type_src": "фільм",
        "year": "2024",
        "director": "Джон Доу",
        "description": "Опис нового фільму.",
        "poster": "link_to_poster",
        "json": "{}",
        "imdb": "tt1234567"
    }
    item = add_to_db(new_item)
    print(f"Добавлен новый элемент с ID: {item.id}")

    # Проверка наличия элемента в БД
    exists = check_in_base("Новий Фільм")
    print(f"Элемент существует: {exists}")

    # Добавление M3U ссылки к существующему элементу
    if exists:
        link = add_m3u(item.id, "link_to_m3u")
        if link:
            print(f"M3U ссылка добавлена к источнику с ID: {link.source_id}")
        else:
            print(f"Элемент для добавления M3U не найден")

    # Сохранение изменений
    save()
    print("Изменения сохранены")
