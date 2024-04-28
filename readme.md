# Facial Search Engine: Face Recognition and Verification

This project serves as a facial recognition system leveraging FaceNet, FastAPI, fasis, and SQLite. Face images are transformed into embeddings using FaceNet and stored in a fasis vector database. Additional data is stored in an SQLite database. Upon receiving new data, both databases are updated with relevant information.

Use it

`localhost:8000/enroll` using post request.

When we run the match function  `localhost:8000/match `is a function interface from where we can upload an image and inreturn fasis will return the best matching image; also id of it on the basis of which data of SQLite is obtained.


## Ussage

To run server use commanda

uvicorn  app:app --host 127.0.0.1 --port 8000 

Use post request at

`localhost:8000/enroll` for enroll new face

`localhost:8000/match` for matching the face


## Installation


pip install -r requeirments.txt
