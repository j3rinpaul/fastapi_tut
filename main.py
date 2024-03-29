from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"Heyy"}


@app.get("/blog")
def show():
    return {'blog':{"all bloggs"}}

'''
in dynamic routingafter the path a variable within { } is declared and called 
based on that

Order of the code matters in dynamic routing:
    -if the path has same routes as of dynamic route which is declared below 
    the dynamic route will not be considered 
    -the dynamic route only be considered even if we call the other route

    eg: route :blog/{id} is above the blog/undefined in the code and 
        the blog/{id} only accepts the int as id so it return error when the undefined is given 
        so defining the non-dynamic route before the dynamic can rectify this error
'''

@app.get("/blog/{id}")
def show_id(id):
    return {'blog_id':id}