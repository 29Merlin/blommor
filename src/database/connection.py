import os
import psycopg2
import psycopg2.extensions.connection as Connection
from functools import wraps
from psycopg2.extensions import cursor
from typing import Callable, TypeVar, ParamSpec, Concatenate

def connect_db() -> Connection:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

T = TypeVar("T")
P = ParamSpec("P")


def db_cursor(f: Callable[Concatenate[cursor, P], T]) -> Callable[P, T]:
    @wraps(f)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        with connect_db() as conn:
            with conn.cursor() as cur:
                return f(cur, *args, **kwargs)

    return wrapper
