from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    #Query for query params and Path for path params
   
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    # the query doesnot need to be declared like  along with annotated
    #but the path requires to do it all the time
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

'''if you want to change the order and donot need to pass any query then pass a * first
    if we use annotated then it is of no problem
'''

@app.get("/items3/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

'''different params can be passed for int values in path
    ie for item_id the number range can be given on to that
    ~ gt - greater than
    ~ lt - lesser thatn
    ~ ge - greater than or equal
    ~ le  - lesser than or equal
    http://127.0.0.1:8000/items4/45?q=dfgsdfghsdfh

    can also add different datatypes in annotated
    like float
'''
@app.get("/items4/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get",gt=2,lt=50),
                      q: str,
                      size: Annotated[float, Query(gt=0, lt=10.5)]):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        results.update({"size":size})
    return results