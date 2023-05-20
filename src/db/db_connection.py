import oracledb

class ConnectionDB:
    def __init__(self) -> None:
        self.pw = '110400'
        self.connection = oracledb.connect(
            user="RM94215",
            password=self.pw,
            host="oracle.fiap.com.br",
            port=1521,
            sid="ORCL"
        )

    def cursor(self):
        cursor = self.connection.cursor()
    
        return cursor
    
    def connection(self):
        return self.connection