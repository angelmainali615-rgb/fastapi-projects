from fastapi  import FastAPI,HTTPException
from schema import Book
from typing  import List
app=FastAPI()

books:List[Book]=[]
@app.post("/books")
def create_book(book:Book):
    for b in books:
        if b.id==book.id:
            raise HTTPException(status_code=400,detail="Given ID already exists")
    books.append(book)
    return book
    
@app.get("/books")
def get_book():
    return books

@app.get("/books/{books_id}")
def get_book_by_id(book_id:int):
    for book in books:
        if book.id==book_id:
            return books
        raise HTTPException(status_code=404, detail="Book not found")
    
@app.delete("/books/{books_id}")
def delete_books(book_id:int):
    for book in books:
        if book.id==book_id:
            return "Book deleted successfully"
        raise HTTPException(status_code=400,detail="Book not found ")
        
