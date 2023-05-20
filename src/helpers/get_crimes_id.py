from src.db.db_connection import ConnectionDB

def get_crimes_id(id_criminal):
    connection = ConnectionDB()
    crimes_ids = list()
    
    with connection.cursor() as cursor:
        query = cursor.execute("SELECT TB_CRIMES_ID FROM TB_CRIMES_COMETIDOS WHERE  TB_CRIMINOSOS_ID=:idcriminoso", [id_criminal])

        for row in query:
            crimes_ids.append(row[0])
        
        
        return crimes_ids