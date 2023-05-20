def transform_crimes_into_list(crimes):
    crimes_list = list()
    
    for i in crimes.split(','):
        crimes_list.append(int(i))
    
    return crimes_list
