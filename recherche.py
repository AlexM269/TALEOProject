import numpy as np

from nltk.corpus import wordnet

def expand_query(vocab_query):
    expanded_query = []
    for term in vocab_query:
        expanded_query.append(term)  # Ajouter le terme d'origine
        synonyms = set()
        for syn in wordnet.synsets(term):
                synonyms.add(syn)
        expanded_query.extend(list(synonyms))  # Ajouter les synonymes
    return expanded_query

# on veut enrichir la requête : tout les mot (nom,verb,adj, pas adrv), trouvé les synonym et leur donner un poid (le même ?)
#https://www.nltk.org/howto/wordnet.html
#https://www.geeksforgeeks.org/nlp-synsets-for-a-word-in-wordnet/


#Création d'une liste de vecteur de similarité entre deux vecteurs requète et document à partir d'un seuil de similarité
def similarity_evaluation(req,doc,seuil):
    liste = []
    for i in range(0,len(req)):
        for j in range(0,len(doc)):
            #produit des vecteurs de poids de doc et req sur le produit de leur norme
            prod_vectors = (np.dot(doc[j], req[i])) / (np.linalg.norm(doc[j]) * np.linalg.norm(req[i]))
            if prod_vectors > seuil:
                liste.append((i, j, prod_vectors))
    return liste

#A partir de la liste de similarité, crée un fichier de type CISI_dev.REL pour afficher les documents correspondants à la requète
def liste_to_fichier(data):

    with open("reponse_requete.txt","w") as f:
        for i in range(0,len(data)):
            line = ""
            line = line + str(data[i][0]+1)+"  "+str(data[i][1])+"  "+str(data[i][2])+"\n"
            f.write(line)


def vocabulaire(listeDocument, listeRequete):
    vocabulary = []
    for doc in listeDocument :
        for mot in doc :
            if mot not in vocabulary :
                vocabulary.append(mot)
    for query in listeRequete:
        for mot in query:
            if mot not in vocabulary :
                vocabulary.append(mot)
    return vocabulary
        
