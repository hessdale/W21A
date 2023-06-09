
import dbhelper
import json
from flask import Flask ,request
app = Flask(__name__)

############### Item Api Endpoints ############### 

@app.get('/api/item')
def get_items():
    #try to use dbhelpers run procedure to get all items with no arguments
    try:
        results = dbhelper.run_procedure('call get_all_items()',[])
        # if the results are a list returned then it converts with json
        if(type(results) == list):
            return json.dumps(results,default=str)
        #else error message
        else:
            return 'something went wrong'
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')

@app.post('/api/item')
def post_items():
    #try to use dbhelpers run procedure to make new item with arguements for name description and price
    try:
        results = dbhelper.run_procedure('call new_item(?,?,?)',[request.json.get('name'),request.json.get('description'),request.json.get('price')])
        # if the results are a list returned then it converts with json
        if(type(results) == list):
            return json.dumps(results,default=str)
        #else error message
        else:
            return 'something went wrong'
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')
    
@app.patch('/api/item')
def patch_items():
    #try to use dbhelpers run procedure to update item with arguements for id and price
    try:
        results = dbhelper.run_procedure('call update_item(?,?)',[request.json.get('id'),request.json.get('price')])
        # if the results are a list returned then it converts with json
        if(type(results) == list):
            return json.dumps(results,default=str)
        #else error message
        else:
            return 'something went wrong'
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')
    
    
@app.delete('/api/item')
def delete_items():
    #try to use dbhelpers run procedure to delete a item with arguement for id
    try:
        results = dbhelper.run_procedure('call delete_item(?)',[request.json.get('id')])
        return results
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')
    
############### Employee Api Endpoints ###############

@app.get('/api/employee')
def get_employee():
    #try to use dbhelpers run procedure to get employee with arguement for id
    try:
        results = dbhelper.run_procedure('call get_employee(?)',[request.json.get('id')])
        # if the results are a list returned then it converts with json
        if(type(results) == list):
            return json.dumps(results,default=str)
        #else error message
        else:
            return 'something went wrong'
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')

@app.post('/api/employee')
def post_employee():
    #try to use dbhelpers run procedure to get employee with arguements for name, position and wage
    try:
        results = dbhelper.run_procedure('call new_employee(?,?,?)',[request.json.get('name'),request.json.get('position'),request.json.get('wage')])
        # if the results are a list returned then it converts with json
        if(type(results) == list):
            return json.dumps(results,default=str)
        #else error message
        else:
            return 'something went wrong'
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')
    
@app.patch('/api/employee')
def patch_employee():
    #try to use dbhelpers run procedure to update employee with arguements for id and wage
    try:
        results = dbhelper.run_procedure('call update_employee(?,?)',[request.json.get('id'),request.json.get('wage')])
        # if the results are a list returned then it converts with json
        if(type(results) == list):
            return json.dumps(results,default=str)
        #else error message
        else:
            return 'something went wrong'
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')
    
@app.delete('/api/employee')
def delete_employee():
    #try to use dbhelpers run procedure to delete employee with arguement for id
    try:
        results = dbhelper.run_procedure('call delete_employee(?)',[request.json.get('id')])
        return results
    #except errors: Type, UnboundLocal and Value with respective error messages
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')
    
#runs app with debugger
app.run(debug=True)
