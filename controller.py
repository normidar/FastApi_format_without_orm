from fastapi import FastAPI

from sql_tool import SqlTool


class Controller:
    @staticmethod
    def run(app: FastAPI, tool: SqlTool):
        @app.get('/')
        def homepage():
            return 'homepage'
