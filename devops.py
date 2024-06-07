from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/Home")
def read_root():
    return {"Hello": "World"}

@app.get("/About")
def about():
    return{"msg":"About us"}

@app.get("Contact-Us")
def contact_us():
    return {"email":"abc@gmail.com","mob_no":"1234567890"}

@app.get("/login")
def login(username :str,password:str):
    if username =="aman" and password =="abc12345":
        return {"Data":"login successfull"}
    else:
        return {"Data":"login unsuccessfull"}
    
@app.post("/login")
def login_post(request:Request):
    print(request.headers)
    print(request.body)
    

