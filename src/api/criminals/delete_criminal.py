from src.db.db_connection import ConnectionDB
from datetime import datetime
    
def delete(headers) -> str:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        try:
            id = headers.get('id')
            
            cursor.execute(
                "DELETE FROM TB_CRIMES_COMETIDOS WHERE TB_CRIMINOSOS_ID = :id", [id]        
            )
            
            cursor.execute(
                "DELETE FROM TB_CRIMINOSOS WHERE id = :id", [id]        
            )
            
            connection.connection.commit()
        
        except Exception as exc:
            connection.connection.rollback()
            print(f"Error on delete")
            raise Exception(exc)
        
    return "Deleted successfully!"