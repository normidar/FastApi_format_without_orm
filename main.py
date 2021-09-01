import pymysql
import uvicorn
from fastapi import FastAPI

from controller import Controller
from sql_tool import SqlTool

app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)

# engine = sqlalchemy.create_engine(
#     'mysql+pymysql://root:Makt0112pc-49466@localhost:3306')

# try:
#     engine.execute(
#         "CREATE TABLE Post(username CHAR(10) NOT NULL, content VARCHAR(1000) )"
#     )
# finally:
#     ...

db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")
#
db.close()
tool = SqlTool(db)
tool.create_db("CREATE TABLE Post(username CHAR(10) NOT NULL, content VARCHAR(1000) )")

Controller.run(app, tool)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
