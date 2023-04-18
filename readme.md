# Face Recoginition and Verification

This project is Face Recoginition module based on FaceNet, FastAPI, fasis, and SQLite. Image Embedding using FaceNet is obtain and stored as fasis vector database. And the other data is stored as SQLlite database object. Whenever a new data comes in a row is added to fasis and SQLite. We can access it using

`localhost:8000/enroll` using post request.

When we run the match function  `localhost:8000/match `is a function interface from where we can upload an image and inreturn fasis will return the best matching image; also id of it on the basis of which data of SQLite is obtained.


## Ussage

To run server use command

uvicorn  app:app --host 127.0.0.1 --port 8000 

Use post request at

`localhost:8000/enroll` for enroll new face

`localhost:8000/match` for matching the face


## Installation


pip install -r requeirments.txt
