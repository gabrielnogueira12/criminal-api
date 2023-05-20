from src.db.db_connection import ConnectionDB
from datetime import datetime
from src.helpers.transform_crimes_id_into_list import transform_crimes_into_list
    
def register(headers) -> str:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        nome = headers.get('nome')
        data_nascimento = datetime.strptime(headers.get('data-nascimento'), '%d/%m/%Y')
        nacionalidade = headers.get('nacionalidade')
        crimes = transform_crimes_into_list(headers.get('crimes'))
        genero = headers.get('genero')
        peso = headers.get('peso')
        altura = headers.get('altura')
        org = headers.get('organizacao')
        
        try:
            
            cursor.execute("SELECT TB_CRIMINOSOS_id_SEQ.nextval FROM dual")
            id_criminoso = cursor.fetchone()[0]
            print(id_criminoso)
            print(type(id_criminoso))
            
            cursor.execute(
                "INSERT INTO TB_CRIMINOSOS (id, nm_criminoso, dt_nascimento, genero, altura, peso, organizacao, nacionalidade) " \
                "VALUES(:id, :nome, :dtnasc, :genero, :altura, :peso, :org, :nac)",
                [id_criminoso, nome, data_nascimento, genero, altura, peso, org, nacionalidade]
            )
                        
            for crime in crimes:
                cursor.execute(
                    f"INSERT INTO TB_CRIMES_COMETIDOS VALUES ({id_criminoso}, {crime})"
                )
            
            connection.connection.commit()
            
        except Exception as exc:
            connection.connection.rollback()
            print(f"Error on register")
            raise Exception(exc)
        
    return "Registered successfully!"