from os import environ as env

CONN = dict(
    database=env.get("PGDATABASE"),
    user=env.get("PGUSER"),
    password=env.get("PGPASS"),
)

