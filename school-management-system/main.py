import uvicorn 
from database import engine
from database import Base 
from fastapi import FastAPI
from  teacher.router import router as teacher_router
from student.router import router as student_router
from school.router import router as school_router
app=FastAPI(title="School Management API")

Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(school_router)

@app.get("/")
async def root():
    return {"message": "Welcome to School Management API !"}

#3. Run The server
if __name__ == "__main__":
    print("Server started! Go to http://127.0.0.1:8000/docs to see the Swagger UI.")
    uvicorn.run(app, host="127.0.0.1", port=8000)
