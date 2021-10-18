from contextlib import contextmanager
import psycopg2

from pgdb import CONN

@contextmanager
def psycopg():
    """context manager for psycopg2 database connection"""
    conn = psycopg2.connect(**CONN)

    try:
        with conn:
            with conn.cursor() as cur:
                yield cur
    finally:
        conn.close()

def main():
    """connect and run a simple query using psycopg"""
    with psycopg() as cur:
        cur.execute(
            "SELECT * FROM customer WHERE store_id = %(store_id)s LIMIT 5;",
            {"store_id": 2},
        )
        cols = [c.name for c in cur.description]
        for res in cur.fetchall():
            row = dict(zip(cols, res))
            print(row["first_name"], row["last_name"])

if __name__ == "__main__":
    main()
