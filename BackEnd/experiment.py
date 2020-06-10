from database import CursorFromConnectionFromPool


class Experiment:

    @classmethod
    def execute(cls, query):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            return data

    @classmethod
    def insert_data(cls, data):
        with CursorFromConnectionFromPool() as cursor:
            for d in data:
                cursor.execute("INSERT into experiment1(id, x, y) VALUES (%s, %s, %s)", d)

    @classmethod
    def delete_data(cls):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute("DELETE FROM experiment1")
