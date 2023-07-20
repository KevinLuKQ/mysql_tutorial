import pymysql

class DBUtil:
    config = {
        'host':'localhost',
        'port':3306,
        'user':'root', 
        'passwd':'12345Jk@', 
        'db':'student_management', 
        'charset':'utf8'
    }


    def __init__(self) -> None:
        """
        The `__init__` function initializes a connection to a database and creates a cursor object for
        executing SQL queries.
        """
        '''
        Get Connection and cursor
        '''

        self.con = pymysql.connect(**DBUtil.config)
        self.cursor = self.con.cursor()
    
    def close(self) -> None:
        '''
        Close connection and cursor
        '''

        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()
        
    def execute_dml(self,sql, *args):
        try:
            self.cursor.execute(sql, args)
            self.con.commit()
        except Exception as e:
            print(e)
            if self.con:
                self.con.rollback()
        finally:
            self.close()

    def query_one(self, sql, *args):
        try:
            self.cursor.execute(sql, args)
            rs = self.cursor.fetchone()
            return rs
        except Exception as e:
            print(e)
        finally:
            self.close()

    def query_all(self, sql, *args):
        '''The `query_all` function executes a SQL query with optional arguments, fetches all the results, and
        returns them.
        
        Parameters
        ----------
        sql
            The `sql` parameter is a string that represents the SQL query you want to execute. It can be any
        valid SQL statement, such as a SELECT, INSERT, UPDATE, or DELETE statement.
        
        Returns
        -------
            The method `query_all` is returning the result of executing the SQL query using the cursor's
        `fetchall()` method.
        
        '''
        try:
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close()

    
if __name__ == "__main__":
    db = DBUtil()
    sql = "SELECT * FROM students"
    print(db.query_one(sql))
    print(DBUtil.close.__doc__)