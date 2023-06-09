
import dbhelper
from flask import Flask ,request
app = Flask(__name__)

@app.get('/api/item')
def get_items():
    results = dbhelper.run_procedure('call get_all_items()',[])
    if(type(results) == list):
        return results
    else:
        return 'something went wrong'

@app.post('/api/item')
def post_items():
    results = dbhelper.run_procedure('call new_item(?,?,?)',[request.json.get('name'),request.json.get('description'),request.json.get('price')])
    if(type(results) == list):
        return results
    else:
        return 'something went wrong'
    
@app.patch('/api/item')
def patch_items():
    results = dbhelper.run_procedure('call update_item(?,?)',[request.json.get('id'),request.json.get('price')])
    if(type(results) == list):
        return results
    else:
        return 'something went wrong'
    
@app.delete('/api/item')
def delete_items():
    dbhelper.run_procedure('call delete_item(?)',[request.json.get('id')])
    return 'successfull delete'
    

##############################
@app.get('/api/employee')
def get_employee():
    results = dbhelper.run_procedure('call get_employee(?)',[request.json.get('id')])
    if(type(results) == list):
        return results
    else:
        return 'something went wrong'

@app.post('/api/employee')
def post_employee():
    results = dbhelper.run_procedure('call new_employee(?,?,?)',[request.json.get('name'),request.json.get('position'),request.json.get('wage')])
    if(type(results) == list):
        return results
    else:
        return 'something went wrong'
    
@app.patch('/api/employee')
def patch_employee():
    results = dbhelper.run_procedure('call get_employee(?)',[request.json.get('id')])
    if(type(results) == list):
        return results
    else:
        return 'something went wrong'
    
@app.delete('/api/employee')
def delete_employee():
    dbhelper.run_procedure('call delete_employee(?)',[request.json.get('id')])
    return 'delete successful'
    


app.run(debug=True)
