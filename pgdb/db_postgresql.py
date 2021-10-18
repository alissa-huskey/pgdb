import postgresql

from pgdb import CONN

def main():
    """connect and run a simple query using postgresql"""
    db = postgresql.open(**CONN)
    query = db.prepare("SELECT * FROM customer WHERE store_id = $1 LIMIT 5")
    for row in query(2):
        print(row["first_name"], row["last_name"])

if __name__ == "__main__":
    main()
