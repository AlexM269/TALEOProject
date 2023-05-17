import recherche
import indexation
import csv

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    fileDocument = open("C:/Users/ewenc/Documents/INFO\GitHub/TALEOProject/CISI.ALLnettoye", 'r')
    fileRequete = open("C:/Users/ewenc/Documents/INFO\GitHub/TALEOProject/CISI_dev.QRY", 'r')
    listeRequete = indexation.vectorizeFile(fileRequete)
    listeDocument = indexation.vectorizeFile(fileDocument)



    # Créer un objet TfidfVectorizer pour les documents
    vectorizer_doc = TfidfVectorizer()
    vectorizer_doc.fit_transform(listeDocument)
    # Obtenir le vocabulaire des documents
    vocabulary_doc = vectorizer_doc.get_feature_names()

    # Créer un objet TfidfVectorizer pour les requêtes
    vectorizer_req = TfidfVectorizer()
    # Calculer les poids TF-IDF pour chaque mot dans les requêtes
    vectorizer_req.fit_transform(listeRequete)
    # Obtenir le vocabulaire des requêtes
    vocabulary_req = vectorizer_req.get_feature_names()
    voc = recherche.expand_query(vocabulary_req)
    # Concaténer les deux vocabulaires sans doublons
    vocabulary = list(set(vocabulary_doc + voc))

    # Créer un nouvel objet TfidfVectorizer avec le vocabulaire combiné
    vectorizer_combined = TfidfVectorizer(vocabulary=vocabulary)

    # Calculer les poids TF-IDF pour chaque mot dans les documents
    tfidf_matrixDoc = vectorizer_combined.fit_transform(listeDocument)
    # Transformer la matrice TF-IDF des documents en une liste de vecteurs
    document_vectors = tfidf_matrixDoc.toarray()

    # Calculer les poids TF-IDF pour chaque mot dans les requêtes
    tfidf_matrixReq = vectorizer_combined.fit_transform(listeRequete)

    # Transformer la matrice TF-IDF des requêtes en une liste de vecteurs
    requete_vectors = tfidf_matrixReq.toarray()

    print(len(requete_vectors[0]))

    listeResultat = recherche.similarity_evaluation(requete_vectors,document_vectors, 0.12)
    print(listeResultat[0])
    recherche.liste_to_fichier(listeResultat)