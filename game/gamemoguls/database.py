import sqlite3
import datetime

class DB():

    def createdb(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        conn.commit()
        conn.close()

    def cdb(dbname):
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        
    def dcdb(dbname):
        conn=sqlite3.connect(dbname)
        conn.commit()
        conn.close()


    class Column:
        sql_types = {
            int: 'INT',
            str: 'VARCHAR(255)',
            float: 'DECIMAL(10,2)',
            bool: 'BOOLEAN',
            datetime.date: 'DATE',
            datetime.datetime: 'TIMESTAMP'
        }

        def __init__(self, name, datatype, primary_key=False, nullable=True, default=None):
            self.name = name
            self.datatype = datatype
            self.primary_key = primary_key
            self.nullable = nullable
            self.default = default


    class Table():
        def __init__(self, name, columns):
            self.name = name
            self.columns = columns

        def create(self):
            table = f"CREATE TABLE IF NOT EXISTS {self.name} ("
            for column in self.columns:
                column_sql = f"{column.name} {column.sql_types[column.datatype]}"

                if column.primary_key:
                    column_sql += " PRIMARY KEY"
                if not column.nullable:
                    column_sql += " NOT NULL"
                if column.default is not None:
                    column_sql += f" DEFAULT {column.default}"

                table += column_sql + ", "

            table = table.rstrip(", ") + ")"
            return table
        
        def insert(self, data):
            table = f"INSERT INTO {self.name} ("
            for column in self.columns:
                table += column.name + ", "
            table = table.rstrip(", ") + ") VALUES ("
            for column in self.columns:
                table += "?, "
            table = table.rstrip(", ") + ")"

            return table, data
        
        def select(self, data):
            table = f"SELECT * FROM {self.name} WHERE "
            for column in self.columns:
                table += column.name + " = ? AND "
            table = table.rstrip(" AND ")

            return table, data


        