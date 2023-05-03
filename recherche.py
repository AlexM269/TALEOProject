import numpy as np

def indexation_query():
    print("ouais")
def preprocess_query():
    print("preprocess_query")

#Création d'une liste de vecteur de similarité entre deux vecteurs requète et document à partir d'un seuil de similarité
def similarity_evaluation(req,doc,seuil):
    liste = []
    for i in range(0,len(req)):
        for j in range(0,len(doc)):
            #produit des vecteurs de poids de doc et req sur le produit de leur norme
            prod_vectors = (np.dot(doc[j], req[i])) / (np.linalg.norm(doc[j]) * np.linalg.norm(req[i]))
            print(i, j, prod_vectors)
            if prod_vectors > seuil:
                liste.append((i, j, prod_vectors))
    return liste

#A partir de la liste de similarité, crée un fichier de type CISI_dev.REL pour afficher les documents correspondants à la requète
def liste_to_fichier(data):
    line = ""
    with open("reponse_requete.txt","w") as f:
        for i in range(0,len(data)):
            line = line + data[i][0]+"  "+data[i][1]+"  "+data[i][2]+"\n"
            f.write(line)
    
        
