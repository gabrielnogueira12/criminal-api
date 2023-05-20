def get_crimes_modified_to_update_in_db(old, new):
    
    put_in = list()
    out = list()
    
    for i in old:
        if i not in new:
            out.append(i)
        
    for i in new:
        if i not in old:
            put_in.append(i)
    
    
    return {
        "out": out,
        "in": put_in
        }
    
