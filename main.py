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
    #création du vocabulaire
    vocabulaire =recherche.vocabulaire(listeDocument, listeRequete)
    print(vocabulaire[0:3])

    #tfidf des doc et des requetes
    requete_vectors = indexation.tf_idf(vocabulaire, listeRequete)
    document_vectors = indexation.tf_idf(vocabulaire, listeDocument)
    print(len(requete_vectors[1]))
    print(len(document_vectors[1]))
    print(len(vocabulaire))


    # for i in range(0,4):
    #     document_vectors[i]+=1
    #
    # print(len(requete_vectors[0]))

    listeResultat = recherche.similarity_evaluation(requete_vectors,document_vectors, 0.12)
    #print(listeResultat[0])
    recherche.liste_to_fichier(listeResultat)