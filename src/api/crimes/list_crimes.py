from src.db.db_connection import ConnectionDB
from src.helpers.transform_crimes_query_into_json import transform_crimes_query_result_into_json


def list_crimes():
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        criminals = list()
        
        try:
            query = cursor.execute("SELECT * FROM TB_CRIMES")
            
            for row in query:
                criminal = transform_crimes_query_result_into_json(row)
                criminals.append(criminal)
            
            response = {
                "body": criminals,
                "status": 200
            }
            
            return response
            
        except Exception as exc:
            print(f"Error on list")
            raise Exception(exc)
    
    