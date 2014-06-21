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
    engine = create_engine('mysql+mysqldb://root:root@localhost/clinic')
    metadata = MetaData(engine)
