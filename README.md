pgdb
====

This project is to mess around with PostgreSQL using Python. It can be found
on [github][repo].

Sample database downloaded from [PostgreSQL Tutorial][sample-db].

[sample-db]: https://www.postgresqltutorial.com/postgresql-sample-database/
[elephant]: https://www.elephantsql.com/
[poetry]: https://python-poetry.org/
[repo]: https://github.com/alissa-huskey/pgdb

Prerequisites
-------------

* bash 4+
* python 3.8+
* [postgresql](https://www.postgresql.org/)
* [poetry][poetry]

Setup
-----

`tl;dr` [^*]

1. `git clone https://github.com/alissa-huskey/pgdb.git`
1. `cp env .env`
1. `source .env`
1. `./tools/mkdb`
1. `poetry install`
1. `poetry shell`
1. `python pgdb/main.py`

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
