from yoyo import step
import sqlite3


class Repo:
    conn = sqlite3.connect('/C:/Users/bernh/git/pycharm/mea4_02_repository/data/db/db.db')

    @staticmethod
    def create_table_fizzbuzz():
        cursor = Repo.conn.cursor()
        cursor.execute('''
        CREATE TABLE fizzbuzz
        (id INTEGER PRIMARY KEY ASC, request int, response varchar(50))
        ''')
        Repo.conn.commit()
        Repo.conn.close()

    @staticmethod
    def fizzpuzz_post(id1: int, request1: int, response1: str) -> str:
        cursor = Repo.conn.cursor()
        cursor.execute(('''
        INSERT INTO fizzbuzz (id, request, response) VALUES (?,?,?)
        '''), (id1, request1, response1))
        Repo.conn.commit()
        Repo.conn.close()
        return "ok"

    @staticmethod
    def delete_table_fizzbuzz():
        cursor = Repo.conn.cursor()
        cursor.execute('''
        DROP TABLE fizzbuzz
        ''')
        Repo.conn.commit()
        Repo.conn.close()


    # steps = [
    #     step(create_table_fizzbuzz, delete_table_fizzbuzz, fizzpuzz_post)
    # ]
