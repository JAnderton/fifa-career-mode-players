from peewee import Model, IntegerField, CharField, SqliteDatabase

db = SqliteDatabase('resources/database/players.db')


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


if __name__ == "__main__":
    db.create_table(Download, True)