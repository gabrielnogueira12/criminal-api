from src.db.db_connection import ConnectionDB
from src.helpers.transform_criminal_query_result_into_json import transform_criminal_query_result_into_json
    
def search(args) -> str:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        id = args.get('id', type=int)
        
        try:
            cursor.execute("SELECT * FROM TB_CRIMINOSOS WHERE id = :id", [id])
            criminal = transform_criminal_query_result_into_json(cursor.fetchone())
            
            
        except Exception as exc:
            print(f"Error on search")
            raise Exception(exc)
    
    response = {
        "body": criminal,
        "status": 200
    }
    
    return response