from src.db.db_connection import ConnectionDB

def update_crime(headers) -> str:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        id = headers.get('id')
        nome = headers.get('nome')
        descricao = headers.get('descricao')
        
        try:

            cursor.execute(
                "UPDATE TB_CRIMES SET nm_crimes = :nm, ds_crimes = :descricao" \
                "WHERE id = :id",
                [nome, descricao, id]
            )
            
            connection.connection.commit()
            
        except Exception as exc:
            connection.connection.rollback()
            print(f"Error on update")
            raise Exception(exc)
        
    return "Updated successfully!"