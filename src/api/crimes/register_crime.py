from src.db.db_connection import ConnectionDB

def register_crime(headers) -> str:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        nome = headers.get('nome')
        descricao = headers.get('descricao')
        
        try:

            cursor.execute(
                "INSERT INTO TB_CRIMES (nm_crimes, ds_crimes) " \
                "VALUES(:nm, :descricao)",
                [nome, descricao]
            )
            
            connection.connection.commit()
            
        except Exception as exc:
            connection.connection.rollback()
            print(f"Error on register")
            raise Exception(exc)
        
    return "Registered successfully!"