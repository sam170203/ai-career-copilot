from fastapi import FastAPI

app=FastAPI(title="AI Career Copilot")

@app.get("/")
def home():
    return {"message":"AI career copilot chlra hai"}