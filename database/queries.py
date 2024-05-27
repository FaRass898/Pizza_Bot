class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_or_instagram  TEXT,
            date_of_visit TEXT,
            food_rating INTEGER,
            cleaning_rating INTEGER,
            rating INTEGER
        )
    """
    DROP_CATEGORIES_TABLE = """DROP TABLE IF EXISTS categories"""
    CREATE_CATEGORIES_TABLE ="""
    CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT
    )
    """
    DROP_MENU_TABLE = """DROP TABLE IF EXISTS menu"""
    CREATE_MENU_TABLE ="""
    CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price FLOAT,
            picture TEXT,
            categorie_id INTEGER,
            FOREIGN KEY(categorie_id) REFERENCES categories(id)
    )"""

    POPULATE_CATEGORIES = """
        INSERT INTO categories (name) VALUES 
        ('pizza'),
        ('nuggets'),
        ('milkshakes')
    """

    POPULATE_MENU = """
        INSERT INTO menu (name, price, picture, categorie_id) VALUES
            ("Маргарита", 450, "pizza1.jpg", 1),
            ("Пепперони", 400, "pizza1.jpg", 1),
            ("Гавайская", 470, "pizza1.jpg", 1),
            ("Мясная", 460, "pizza1.jpg", 1),
            ("Четыре сыра", 500, "pizza1.jpg", 1),
            ("Острые", 350, "nuggets.jpg", 2),
            ("Барбекю", 380, "nuggets.jpg", 2),
            ("Терияки", 400, "nuggets.jpg", 2),
            ("Чесночные", 370, "nuggets.jpg", 2),
            ("Фруктовый смузи", 250, "milkshake.jpg", 3),
            ("Вишневый фреш", 200, "milkshake.jpg", 3),
            ("Клубничный лимонад", 180, "milkshake.jpg", 3),
            ("Ванильный", 280, "milkshake.jpg", 3),
            ("Шоколадный", 300, "milkshake.jpg", 3),
            ("Клубничный", 320, "milkshake.jpg", 3)
    """