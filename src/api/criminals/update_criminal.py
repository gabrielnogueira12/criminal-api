from src.db.db_connection import ConnectionDB
from datetime import datetime
from src.helpers.transform_crimes_id_into_list import transform_crimes_into_list
from src.helpers.get_crimes_id import get_crimes_id
from src.helpers.get_crimes_modified_to_update_in_db import get_crimes_modified_to_update_in_db
    
def update(headers) -> None:
    
    connection = ConnectionDB()
    with connection.cursor() as cursor:
        
        id = headers.get('id')
        nome = headers.get('nome')
        dt_nascimento = datetime.strptime(headers.get('data-nascimento'), '%d/%m/%Y')
        nacionalidade = headers.get('nacionalidade')
        crimes = transform_crimes_into_list(headers.get('crimes'))
        genero = headers.get('genero')
        peso = headers.get('peso')
        altura = headers.get('altura')
        org = headers.get('organizacao')
        
        try:
            cursor.execute(
                """UPDATE TB_CRIMINOSOS 
                SET
                    nm_criminoso = :nome, 
                    dt_nascimento = :dtnascimento,
                    nacionalidade = :nacionalidade,
                    genero = :genero,
                    peso = :peso,
                    altura = :altura,
                    organizacao = :org
                WHERE id = :id
                """,
                [nome, dt_nascimento, nacionalidade, genero, peso, altura, org, id]
            )
            
            crimes_antigos = get_crimes_id(id)
            
            ids_to_modify = get_crimes_modified_to_update_in_db(crimes_antigos, crimes)
            print(ids_to_modify)
            
            
            for i in ids_to_modify['out']:
                print(f"out: {i}")
                cursor.execute("DELETE FROM TB_CRIMES_COMETIDOS WHERE TB_CRIMINOSOS_ID=:idcriminoso AND TB_CRIMES_ID=:idcrime", [id, i])
            
            for i in ids_to_modify['in']:
                print(f"in: {i}")
                cursor.execute("INSERT INTO TB_CRIMES_COMETIDOS VALUES (:idcriminoso, :idcrime)", [id, i])
            
            connection.connection.commit()
            
        except Exception as exc:
            connection.connection.rollback()
            print(f"Error on update")
            raise Exception(exc)
    
    return "Updated successfully!"