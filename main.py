from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/course/{course_id}") # http://127.0.0.1:8000/course/200
def my_course(course_id: int):
    return {"course_id": course_id} 


# A get function
dummy_data = [i for i in range(10)]
@app.get("/my/page/items/")
async def read_item(page: int = 0, limit: int = 0, skip: int = 1):
    # http://127.0.0.1:8000/my/page/items/?page=3&limit=2&skip=2
    return dummy_data[page: page*2 + limit: skip] 
# like dummy_data = [i for i in range(10)]
# dummy_data[3:8:2] output dummy_data [3, 5, 7]


# A post example
from pydantic import BaseModel

class MyItem(BaseModel):
    name: str
    info: str = None
    price: float
    qty: int

@app.post("/purchase/item/")
async def create_item(item: MyItem):
    return {"amount": item.qty*100, "success": True}
# curl -X POST "http://127.0.0.1:8000/purchase/item/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"sample item\",\"info\":\"This is info for the item\",\"price\":40,\"qty\":2}"
# for windows, use requests.post


# create a FORM
from fastapi import Form #pip install python-multipart
@app.post("/accounts/login/")
async def login_view(username: str = Form(...), password: str = Form(...)):
    return {"success": True}
