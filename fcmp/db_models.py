from peewee import Model, IntegerField, CharField, SqliteDatabase
import os

__db_path__ = 'resources/database/players.db'
if not os.path.exists(os.path.dirname(__db_path__)):
    os.makedirs(os.path.dirname(__db_path__))
db = SqliteDatabase(__db_path__)


class Download(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    url = CharField(unique=True)
    status = CharField()

    class Meta:
        database = db


class Status(object):
    NEW = "new"
    DOWNLOADING = "downloading"
    COMPLETE = "complete"