from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from db_interface import DBInterace
import os
import base64

app = FastAPI()
db_int = DBInterace(db_name='test1',k=3)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/enroll")
async def create_user(name: str, address: str, city:str,state:str,zip:str, picture: UploadFile = File(...)):
    # Save the uploaded file to the server
    with open(f"faces/{picture.filename}", "wb") as buffer:
        buffer.write(await picture.read())
    file_name = f'faces/{picture.filename}'
    try:
        a=db_int.enroll(name=name,address=address,city=city,state=state,zip=zip,filename=file_name)
        status=True
    except:
        a=-1
        status=False
    #Create the user object

    content = {}
    content['id']=a
    content['status']=status
    # Return a JSON response with the user data
    return JSONResponse(content=content)

@app.post("/match")
async def upload_image(picture: UploadFile = File(...)):
    
    # Generate a unique filename
    filename = f"faces/{picture.filename}"
    # Save file to disk
    with open(f"faces/{picture.filename}", "wb") as buffer:
        buffer.write(await picture.read())
    
    data_json = db_int.reterive(filename=filename)
    # print(data_json)
    # Return file path and base64-encoded contents
    return JSONResponse(content=data_json)

@app.get("/image/{filename}")
async def get_image(filename: str):
    # Construct the path to the image file
    file_path = f"faces/{filename}"
    # Check if the file exists
    if not os.path.exists(file_path):
        print('no')
        return JSONResponse(content={"error": "File not found"})
    # Load file contents
    with open(file_path, "rb") as f:
        contents = f.read()
    # Encode file contents as base64
    print(file_path)
    base64_image = base64.b64encode(contents).decode('utf-8')
    # Return base64-encoded contents
    return JSONResponse(content={"base64_image": base64_image})