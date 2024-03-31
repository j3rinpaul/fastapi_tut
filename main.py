from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    age:int
    gender:str|None = None


app = FastAPI()

'''
Request body

data from client towards the api

a class having all the details of the data that should constitute the body is declared
that class is being passed into the function as params


inside the async function we can use the class to obtain the values 
the class can be converted to dict for json purposes

the path and query params can also be transferred along with this

'''

@app.post('/details')
async def post_details(item:Item):
    item_dict = item.dict()
    if item.age > 18:
        item_dict.update({"class":"18plus"})
    return item_dict

#path params
#http://127.0.0.1:8000/detailed?items_id=34

@app.post('/detailed')
async def details(item:Item,items_id:int):
    return {"item_id":items_id,**item.dict()}

#query params + path params
#http://127.0.0.1:8000/query/54?q=20
@app.post('/query/{items_id}')
async def querty(item:Item,items_id:int,q:str | None = None):
    result = {"item_id": items_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result