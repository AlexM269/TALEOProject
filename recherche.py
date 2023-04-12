import numpy as np

def indexation_query():
    print("ouais")
def preprocess_query():
    print("preprocess_query")
def similarity_evaluation(req,doc,seuil):
    liste = []
    for i in range(0,len(req)):
        for j in range(0,len(doc)):
            prod_vectors = (np.dot(doc[j], req[i])) / (np.linalg.norm(doc[j]) * np.linalg.norm(req[i]))
            if prod_vectors > seuil:
                liste.append((i,j,prod_vectors))
    return liste

def liste_to_fichier(data):
    line=""
    with open("reponse_requete.txt","w") as f:
        for i in range(0,len(data)):
            line = line + data[i][0]+"  "+data[i][1]+"  "+data[i][2]+"\n"
            f.write(line)
    
        
