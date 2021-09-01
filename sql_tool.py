from pymysql import Connection


class SqlTool:
    def __init__(self, db: Connection):
        self.db = db

    def create_db(self, sql: str):
        self.db.open()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
        finally:
            ...
        self.db.close()

    def run_sql(self, sql: str):
        self.db.open()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def search(self, sql: str):
        self.db.open()
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            rt = cursor.fetchall()
            self.db.close()
            return rt
        except:
            self.db.rollback()
        self.db.close()
