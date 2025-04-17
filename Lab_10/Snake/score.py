import psycopg2
from datetime import datetime

# Настройки БД для результатов
DB_RESULTS  = "snake_scores"
DB_USER     = "postgres"
DB_PASSWORD = "Zhk369369"
DB_HOST     = "localhost"
DB_PORT     = "5432"

# Подключаемся к БД результатов
conn = psycopg2.connect(
    dbname=DB_RESULTS,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Запрашиваем все результаты, сортируя по очкам (убывание) и времени (возрастание)
cur.execute(
    "SELECT username, score, level, saved_at "
    "FROM results "
    "ORDER BY score DESC, saved_at ASC"
)
rows = cur.fetchall()

# Выводим результаты без использования сторонних библиотек
if rows:
    # Печать заголовка
    header = f"{'Username':<20}{'Score':<8}{'Level':<8}{'Saved At'}"
    print(header)
    print('-' * len(header))
    # Печать каждой записи
    for username, score, level, saved_at in rows:
        print(f"{username:<20}{score:<8}{level:<8}{saved_at}")
else:
    print("No results found in the database.")

# Закрываем соединение
cur.close()
conn.close()
