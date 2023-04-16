from deepface import DeepFace
import numpy as np
import os,glob
import faiss
from sql_db_interface import SQLDBInterface

class FaceDBInterface(object):
    def __init__(self,face_directory:str = '',db_name:str = '',k=3) -> None:
        self.face_directory = face_directory
        self.db_name = db_name
        self.dimensions = 128 
        self.metric = 'euclidean'
        self.k_neib = k
        self.configure_things()

        
    def configure_things(self):
        if self.metric == 'euclidean':
            self.index = faiss.IndexFlatL2(self.dimensions)
        elif self.metric == 'cosine':
            self.index = faiss.IndexFlatIP(self.dimensions)
        
        if not os.path.isfile(self.db_name+'.index'):
            faiss.write_index(self.index,self.db_name+'.index')
            self.index = faiss.read_index(self.db_name+'.index')
        else:
            self.index = faiss.read_index(self.db_name+'.index')
            

    def vectorize_image(self,file_name):
        target_representation = DeepFace.represent(img_path = file_name, model_name = "Facenet")[0]["embedding"]
        target_representation = np.array(target_representation, dtype='f')
        target_representation = np.expand_dims(target_representation, axis=0)
        return target_representation
    
    def enroll_face(self,file_name):
        target_representation = self.vectorize_image(file_name=file_name)
        self.index.add(target_representation)
        faiss.write_index(self.index,self.db_name+'.index')
        return self.reterive_face(file_name=file_name)[1][0][0]


    def reterive_face(self,file_name):
        target_representation = self.vectorize_image(file_name=file_name)
        distances, neighbors = self.index.search(target_representation, self.k_neib)
        total_distances = (1/distances).sum()
        distance_metrics = [(1/d)/total_distances for d in distances]
        return distance_metrics,neighbors