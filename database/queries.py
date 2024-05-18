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