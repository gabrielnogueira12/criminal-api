from flask import Flask, request
from src.api.criminals.register_criminal import register
from src.api.criminals.delete_criminal import delete
from src.api.criminals.update_criminal import update
from src.api.criminals.get_criminal import search
from src.api.criminals.list_criminals import list_criminals
from src.api.crimes.get_crime import search_crime
from src.api.crimes.register_crime import register_crime
from src.api.crimes.update_crime import update_crime
from src.api.crimes.delete_crime import delete_crime


app = Flask(__name__)

@app.route('/list-criminals', methods=['GET'])
def list_all_criminals():
    list_criminal = list_criminals()
    
    return list_criminal

@app.route('/search-criminal', methods=['GET'])
def get_criminal_by_id():
    args = request.args
    criminal = search(args)
    
    return criminal

@app.route('/register-criminal', methods=['POST'])
def register_criminal():
    headers = request.headers
    registered_criminal = register(headers)
    
    return registered_criminal

@app.route('/update-criminal', methods=['POST'])
def update_criminal():
    headers = request.headers
    updated_criminal = update(headers)
    
    return updated_criminal

@app.route('/delete-criminal', methods=['DELETE'])
def delete_criminal():
    args = request.args    
    deleted_criminal = delete(args)
    
    return deleted_criminal

@app.route('/search-crimes', methods=['GET'])
def get_crime_by_id():
    args = request.args
    crime = search_crime(args)
    
    return crime

@app.route('/register-crimes', methods=['POST'])
def register_crimes():
    headers = request.headers
    registered_crimes = register_crime(headers)
    
    return registered_crimes

@app.route('/update-crimes', methods=['POST'])
def update_crimes():
    headers = request.headers
    updated_crimes = update_crime(headers)
    
    return updated_crimes

@app.route('/delete-crimes', methods=['DELETE'])
def delete_crimes():
    args = request.args    
    deleted_crimes = delete_crime(args)
    
    return deleted_crimes


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)