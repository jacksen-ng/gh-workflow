import fastapi

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World! and Workflow"}


@app.get("/test_workflow")
def test_workflow():
    return {"message": "Hello, Workflow!"}