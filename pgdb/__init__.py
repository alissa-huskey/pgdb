from os import environ

def env(var):
    """Return the value of the PG{VAR} env var"""
    if isinstance(var, tuple):
        _, var = var
    return environ.get(f"PG{var}".upper())

def nameof(name):
    """Return either var, or the first element of var if a tuple"""
    if isinstance(name, tuple):
        name, _ = name
    return name

fields = ("database", "user", "host", "port", ("password", "pass"))
CONN = {nameof(x): env(x) for x in fields if env(x)}
