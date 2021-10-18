pgdb
====

This project is to mess around with PostgreSQL.

Sample database downloaded from [PostgreSQL Tutorial][sample-db]. Using
[ElephantSQL][elephant] for database hosting.

[sample-db]: https://www.postgresqltutorial.com/postgresql-sample-database/
[elephant]: https://www.elephantsql.com/

Setup
-----

### Create a password file

* [The Password File](https://www.postgresql.org/docs/current/libpq-pgpass.html)

Create a `.pgpass` file in your home directory.

```
# located at
# ----------
# windows:   %appdata%/postgresql/pgpass.conf
# mac/linux: ~/.pgpass
#
# permission
# ----------
# Restrict access to only the owner with the following command:
# 
# chmod 0600 path-to-passfile

# see also
# --------
# https://www.postgresql.org/docs/current/libpq-pgpass.html
#
# syntax
# ------
# Lines beginning with # are comments.
# All other lines should have the following format
#   with * as wildcard.
#
# hostname:port:database:username:password
# 
# examples
# --------
# localhost:5432:demo:dbuser:demo@123
# *:*:*:postgres:admin12345
#

```

### Create a local .env file

Create a `.env` file:

```bash
#!/usr/bin/env bash

PGUSER=""
PGDATABASE=""
PGHOST=""

# PG_COLOR="always"       # always, never, auto

```

### Create user and database

```bash
createuser dvdrental -P
createdb dvdrental --owner=dvdrental
```
