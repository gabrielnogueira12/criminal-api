def transform_crimes_query_result_into_json(result):
    
    crimes = dict()
    
    crimes['id'] = result[0]
    crimes['nome'] = result[1]
    crimes['descricao'] = result[2]
    
    return crimes