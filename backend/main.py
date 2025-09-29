import fastapi

app = fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World! and Workflow"}


@app.get("/test_workflow")
def test_workflow():
    return {"message": "Hello, Workflow!"}


@app.get("/test_workflow_2")
def test_workflow_2():
    return {"message": "Hello, Workflow 2!"}


@app.get("/test_workflow_3")
def test_workflow_3():
    return {"message": "Hello, Workflow 3!"}
