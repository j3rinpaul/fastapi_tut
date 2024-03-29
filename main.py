from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def index():
    return {"Heyy"}


@app.get("/blog")
def show(limit = 10,publish:bool = True,sort:Optional[str] = None):
    if publish:
        return {'blog':{f'{limit} blogs which are published'}}
    else:
        return {'blog': {f'{limit} from all blogs'}}

'''
query parameters are given for getting certain data from the db
default values can be given along with optional ones too
here the limit and publish is required and default vales are given 
the sort is of optional and the default value is none as it is optional

fastapi differentiates between the path params and query params like
if the params is declared in the path then it is treated as path params
if the params is only declared in function or as in the query the it is treated as query params
'''

@app.get("/blog/{id}")
def show_id(id:int):
    return {'blog_id':id}