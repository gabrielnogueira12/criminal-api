def transform_criminal_query_result_into_json(result):
    
    criminal = dict()
    
    criminal['id'] = result[0]
    criminal['nome'] = result[1]
    criminal['data_nascimento'] = result[2].strftime('%d/%m/%Y')
    criminal['genero'] = result[3]
    criminal['altura'] = result[4]
    criminal['peso'] = result[5]
    criminal['organizacao'] = result[6]
    criminal['nacionalidade'] = result[7]
    
    return criminal