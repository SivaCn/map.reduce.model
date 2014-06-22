#!/usr/bin/python


## ----------- sqlalchemy DataTypes ------------ ##
from sqlalchemy import create_engine, MetaData

## ----------- sqlalchemy Table Properties ------------ ##
from sqlalchemy import Table, Column, Integer, String, DATETIME

## ----------- sqlalchemy Constraints ------------ ##
from sqlalchemy import ForeignKey

## ----------- sqlalchemy CRUD imports ------------ ##
from sqlalchemy import select


class PreSet(object):
    """
    """
    engine = create_engine('mysql+mysqldb://root:root@localhost/creative')
    metadata = MetaData(engine)


class DBAPI(object):

    large_table = Table('large_table', PreSet.metadata,
            Column('identity_idn', Integer, primary_key=True),
            Column('user_idn', Integer),
            Column('tag', String(20)),
            Column('pool', Integer)
            )

    @classmethod
    def create(cls, table_name=''):
        try:
            cls.__getattribute__(cls, table_name).create()
        except Exception as error:
            print "ERROR:", str(error)

    @classmethod
    def insert(cls, table_name='', _many='', **_single):
        pass

    @classmethod
    def select(cls):
        pass
