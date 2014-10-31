from peewee import Model, IntegerField, CharField, SqliteDatabase

db = SqliteDatabase(None)


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