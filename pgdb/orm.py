from urllib.parse import quote_plus
from contextlib import contextmanager

import sqlalchemy as db
from sqlalchemy.orm import relationship
from sqlalchemy.engine import URL
from sqlalchemy.orm import registry


from pgdb import CONN

@contextmanager
def database():
    ...

def url():
    """Return a URL object compiled from CONN dict"""

    remap = { "user": "username", "pass": "password" }
    config = {remap.get(k, k): v for k, v in CONN.items()}

    return URL.create(drivername="postgresql", **config)

def main():
    engine = db.create_engine(url())
    with engine.connect() as session:
        reg = registry()
        reg.metadata.reflect(bind=engine)
        tables = reg.metadata.tables
        Base = reg.generate_base()

        class Address(Base):
            __table__ = tables["address"]
            customer = relationship("Customer", uselist=False, back_populates="address")

        class Customer(Base):
            __table__ = tables["customer"]
            address = relationship("Address", uselist=False, back_populates="customer")

        query = db.select([Customer, Address]).where(Customer.store_id == 2)

        for row in session.execute(query).fetchmany(5):
            print(row.first_name, row.last_name, row.address)

if __name__ == "__main__":
    main()
