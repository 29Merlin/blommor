from src.database.connection import db_cursor
from psycopg2.extensions import cursor

@db_cursor
def add_flower_type(cur: cursor, name:str) -> None:
    cur.execute(
        "INSERT INTO flower_types (name) VALUES (%s)",
        (name,)
    )


@db_cursor
def add_flower(cur: cursor, name:str, type:str, primary_color:str, price:float) -> None:
    cur.execute(
        "INSERT INTO flowers (name, type, primary_color, price) VALUES (%s, %s, %s, %s)",
        (name, type, primary_color, price)
    )

@db_cursor
def get_all_flowers(cur: cursor) -> list[dict]:
    cur.execute("SELECT name, type, primary_color, price, stock FROM available_flowers")
    rows = cur.fetchall()
    return [
        {
            "name": row[0],
            "type": row[1],
            "primary_color": row[2],
            "price": row[3],
            "stock": row[4]
        }
        for row in rows
    ]

@db_cursor
def remove_flower(cur: cursor, name:str) -> None:
    cur.execute(
        "DELETE FROM flowers WHERE name = %s",
        (name,)
    )

@db_cursor
def update_flower_stock(cur: cursor, name:str, stock:int) -> None:
    cur.execute(
        "UPDATE flowers SET stock = %s WHERE name = %s",
        (stock, name)
    )
