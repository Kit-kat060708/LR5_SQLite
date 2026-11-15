import sqlite3
from pathlib import Path
folder = Path(__file__).resolve().parent
con = sqlite3.connect(folder/"app.db")

con.execute("""
CREATE TABLE IF NOT EXISTS equipment (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    value INTEGER
)
""")

data = [
    ("Футбольный мяч", "Футбол", 10),
    ("Вратарские перчатки", "Футбол", 4),
    ("Футбольные ворота", "Футбол", 2),
    ("Щитки", "Футбол", 8),
    ("Баскетбольный мяч", "Баскетбол", 6),
    ("Баскетбольная сетка", "Баскетбол", 3),
    ("Волейбольный мяч", "Волейбол", 7),
    ("Волейбольная сетка", "Волейбол", 2)
]

count = con.execute(
    "SELECT COUNT(*) FROM equipment"
).fetchone()[0]

if count==0: 
    con.executemany(
        "INSERT INTO equipment (name, category, value)"
        "VALUES (?,?,?)",
        data
    )
    con.commit()

print("Все записи:")
rows = con.execute(
    "SELECT * FROM equipment ORDER BY id"
).fetchall()
for row in rows:
    print(row)

print("\nИнвентарь для футбола:")
rows = con.execute(
    "SELECT * FROM equipment WHERE category = ?",
    ("Футбол",)
).fetchall()
for row in rows:
    print(row)

print("\nКоличество больше 5:")
rows = con.execute(
    "SELECT * FROM equipment WHERE value > 5"
).fetchall()
for row in rows:
    print(row)

print("\nСортировка по убыванию количества:")
rows = con.execute(
    "SELECT * FROM equipment ORDER BY value DESC, id ASC"
).fetchall()
for row in rows:
    print(row)

#Изменение количества инвентаря
record_id = 2
new_value = 5

con.execute(
    "UPDATE equipment SET value = ? WHERE id = ?",
    (new_value, record_id)
)
con.commit()

print("\nПосле изменений записи:")
print(con.execute(
    "SELECT * FROM equipment WHERE id = ?",
    (record_id,)
).fetchone())

#Удаление записи
record_id = 8

con.execute(
    "DELETE FROM equipment WHERE id = ?",
    (record_id,)
)
con.commit()

print("\nПосле удаления записи:")
for row in con.execute("SELECT * FROM equipment ORDER BY id"):
    print(row)

print("\nРабота программы завершена!")
con.close()