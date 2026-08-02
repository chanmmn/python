import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI App")


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float


# in-memory store for demo purposes
items: dict[int, Item] = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple FastAPI App"}


@app.get("/items", response_model=list[Item])
def list_items():
    return list(items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items[item.id] = item
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
