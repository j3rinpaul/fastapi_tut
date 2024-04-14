'''
for query params
`from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results`



FastAPI will know that the value of q is not required because of the default value = None.

'''
# ============================================================================
'''
if we want additional validation like
    `q is optional but if provided should exceed 50 characters`
'''
"""
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

#http://127.0.0.1:8000/items/?q=dfkjghdikfjghkdsjfhg
#50 character length of q is validated using the query method
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    #Annotated is used for types and metadata
    # add Query to it, and set the parameter max_length to 50

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
    

"""
# ============================================================

'''
# q: not required
#Now inorder to add a default value we should do:

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

#http://127.0.0.1:8000/items/
#if no value is given for q then it will be set into "paul"
#if q is provided then it should be of min = 2 and max = 50
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=2,max_length=50)] = "paul"):
    #Annotated is used for types and metadata
    # add Query to it, and set the parameter max_length to 50

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''

# ========================================================================

#q : required

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#or

@app.get("/items3/")
async def read_items(q3: Annotated[str, Query(min_length=3)] = ...):
    result = {"items3": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q3:
        result.update({"q": q3})
    return result


#also it can be declared along with None too

@app.get("/items2/")
async def read_items(q2: Annotated[str | None, Query(min_length=3)] = ...):
    #here the none is given as it says it is not required but the ellipsis make it required
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q2:
        results.update({"q": q2})
    return results



#============================================================

# Query params as a list or multiple values given to q
#http://localhost:8000/items/?q=foo&q=bar

@app.get("/items_list/")
async def read_items(q_list: Annotated[list[str] | None, Query()] = None):
    # we can either give the datatypes inside the list[str] then fastapi checks whether the contents are str
    # or simply give the list so that the fastapi wont check for the datatypes
    query_items = {"q": q_list}
    return query_items

#Query parameter list / multiple values with defaults
# http://localhost:8000/items/
@app.get("/items_listdef/")
async def read_items(q_def: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q_def}
    return query_items

#more metadata can be added
#http://127.0.0.1:8000/items_meta/?item-query=fixedquery
@app.get("/items_meta/")
async def read_items(
    q: Annotated[str | None, Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^afghb$",
            deprecated=True,
        )] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#metadata list
'''
    ~ alias  =   to give another name to the query `http://127.0.0.1:8000/items/?item-query=foobaritems` instead of read_items we can use item-query
    ~ title  =     give title metadata 
    ~ description  = give description metadata
    ~ deprecated    = show that the value is deprecated
'''

#Validations specific for strings:
"""
~ min_length = declaring min length for the parameter
~ max_length = declaring maximum length for the parmeter
~ pattern - for regex

"""