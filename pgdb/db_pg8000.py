import pg8000.native as pg

from pgdb import CONN

def main():
    """connect and run a simple query using pg8000"""
    con = pg.Connection(**CONN)
    query = con.prepare("SELECT * FROM customer WHERE store_id = :store_id LIMIT 5")
    for res in query.run(store_id=2):
        cols = [c["name"] for c in query.columns]
        row = dict(zip(cols, res))
        print(row["first_name"], row["last_name"])

if __name__ == "__main__":
    main()
