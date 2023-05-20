from src.db.db_connection import ConnectionDB
from src.helpers.transform_crimes_query_into_json import transform_crimes_query_result_into_json
    

def search_crime(args) -> str:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        id = args.get('id', type=int)
        
        try:
            cursor.execute("SELECT * FROM TB_CRIMES WHERE id = :id", [id])
            crimes = transform_crimes_query_result_into_json(cursor.fetchone())
            
            
        except Exception as exc:
            print(f"Error on search")
            raise Exception(exc)
    
    response = {
        "body": crimes,
        "status": 200
    }
    
    return response