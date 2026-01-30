import uvicorn
from fastapi import FastAPI
from schema import Item
from fastapi import HTTPException
from schema import UserProfile
from fastapi import Depends
from typing import Optional

# 1. Create the App instance
app = FastAPI()

# 2. Define a Path Operation (Route)
@app.get("/")
def root():
    return {"message": "Hello World, welcome to FastAPI!"}

@app.get("/test")
def test():
    return {"message":"hello world,test!"}
@app.get("/add")
def add(a: str, b: str):
    return {"result": a + b}

@app.post("/home")
def home(number:int):
    return {"number":number}

@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "data": ["user1", "user2", "user3"][skip : skip + limit]
    }

print("Route /users/ added.")

@app.post("/items")
def create_item(item: Item):
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price+item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
    
@app.post("/create-user/")
async def create_user(user: UserProfile):
    # At this point, FastAPI has already validated the data!
   
    # We can access data like a standard Python object
    user_message = f"User {user.username} created with email {user.email}"
   
    if user.age < 18:
        return {"status": "error", "message": "User is too young"}
   
    # We can also convert the model back to a dictionary
    return {
        "status": "success",
        "message": user_message,
            "received_data": user.dict()}
        

@app.get("/items-check/{item_id}", status_code=200)
async def read_item_check(item_id: int):
    if item_id == 0:
        # Return a 404 Error
        raise HTTPException(status_code=404, detail="Item not found (ID cannot be 0)")
    return {"item_id": item_id}

print("Route /items-check/{item_id} added.")

# A simple dependency function
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


# Using the dependency in a route
@app.get("/products/")
async def read_products(commons: dict = Depends(common_parameters)):
    return {"message": "Products retrieved", "params": commons}



@app.get("/orders/")
async def read_orders(commons: dict = Depends(common_parameters)):
    return {"message": "Orders retrieved", "params": commons}

print("Routes using Dependency Injection added.")


# 3. Run the server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8001/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8001)
