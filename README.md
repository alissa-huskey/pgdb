pgdb
====

This project is to mess around with PostgreSQL using Python. It can be found
on [github][repo].

Sample database downloaded from [PostgreSQL Tutorial][sample-db].

[sample-db]: https://www.postgresqltutorial.com/postgresql-sample-database/
[elephant]: https://www.elephantsql.com/
[poetry]: https://python-poetry.org/
[repo]: https://github.com/alissa-huskey/pgdb.git

Table of Contents
-----------------

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Examples](#examples)


Prerequisites
-------------

* bash 4+
* python 3.8+
* [postgresql](https://www.postgresql.org/)
* [poetry][poetry]

Setup
-----

| [Config](#config) | [Scripts](#scripts) | [Development environment](#development-environment) |

`tl;dr` [^*]

```bash
git clone https://github.com/alissa-huskey/pgdb.git
cd pgdb
cp env .env
source .env
./tools/mkdb
poetry install
poetry shell
python pgdb/main.py
```

[^*]: https://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn%27t_read

### Config

Use the following example files and the instructions therein as a basis for
their counterparts on your local machine.

* [.env](env)
* [.pgpass](pgpass)

### Scripts

While you really just need to run `./tools/mkdb`, the following setup scripts
might be a useful reference.

* [setup](tools/setup) -- drops and recreates user and database
* [mksql](tools/mksql) -- generate SQL by replacing `__PATH__` with absolute path to `./data`
* [mkdb](tools/mkdb) -- [re]create user and database then load schema and sample data

### Development environment

Use [poetry][poetry] to install Python dependencies, create a virtual
envionment, then activate it in your shell.

```bash
poetry install
poetry shell
```

Python samples
--------------

This project includes simple scripts which connecting to the sample database
and run a query using each of the following drivers:

* [pg8000](pgdb/db_pg8000.py)
* [postgresql](pgdb/db_postgresql.py)
* [psycopg](pgdb/db_psycopg.py)

----
