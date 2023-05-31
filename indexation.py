import string
import csv
import numpy
import math
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Ouvrir le fichier .REL
file = open("C:/Users/ewenc/Documents/INFO\GitHub/TALEOProject/CISI.ALLnettoye", 'r')

def vectorizeFile(file):
    articles = []
    current_article = ""

    # Lire le contenu ligne par ligne
    for line in file:
        line = line.strip()  # Enlever les caractères de fin de ligne

        # Vérifier si la ligne commence par ".I" suivi d'un numéro d'article
        if line.startswith(".I"):
            # Si un article courant existe déjà, ajouter l'article précédent à la liste
            if current_article != "":
                articles.append(current_article)
                current_article = ""
            # Commencer un nouvel article
        elif line.startswith("."):
            current_article += ""
        elif current_article is not None:
            # Si ce n'est pas une ligne commençant par ".I", ajouter la ligne à l'article courant
            current_article += " " + line  # Concaténer la ligne à l'article courant

    # Ajouter le dernier article à la liste après la fin de fichier
    if current_article is not None:
        articles.append(current_article)
        current_article = ""

#print(articles[0])
#articles contient un article par case

# Tokeniser les articles
    tokenized_articles = []
    for article in articles:
        tokenized_articles.append(word_tokenize(article))
    #tokenized article contient un article tokenisé par case, c'est à dire une liste de mots entre simples quotes séparé par des virgules
    print(tokenized_articles[0])
    # Charger les mots non pertinents
    stop_words = set(stopwords.words('english'))

    # Enlever les mots non pertinents des articles tokenisés
    filtered_articles = []
    liste_mots_sans_ponctuation = []
    liste_mots_sans_stopwords = []
    for liste_mots in tokenized_articles :
        # Supprimez les mots de ponctuation
        for mot in liste_mots :
            if mot not in string.punctuation :
                liste_mots_sans_ponctuation.append(mot)
        # Supprimez les mots très communs de la langue anglaise
        for mot in liste_mots_sans_ponctuation :
            mot = mot.lower()
            if mot not in stop_words :
                liste_mots_sans_stopwords.append(mot)
        # Mettez à jour la liste de mots dans le tableau
        filtered_articles.append(liste_mots_sans_stopwords)
        liste_mots_sans_ponctuation = []
        liste_mots_sans_stopwords = []

    print(filtered_articles[0])

    # Convertir les articles filtrés en chaînes de caractères
    preprocessed_articles = [' '.join(tokens) for tokens in filtered_articles]

    print(preprocessed_articles[0])

    return filtered_articles


def tf(vocabulaire,doc):
    tf=[]
    a=0
    i=0
    for mot in vocabulaire :
        i=0
        for term in doc :
            if mot == term :
                if i<4:
                    a=a+4
                a=a+1
                i=i+1
        tf.append(a/(len(doc)-1))
        a=0
    return tf

def normalizedTf(vocabulaire, doc):
    tfTemp = tf(vocabulaire,doc)
    maxTf = max(tfTemp)
    tf1 = []
    for term in tfTemp :
        tf1.append(term/maxTf)

    return tf1

def augmentedNormalizeTf(vocabulaire, doc):
    tfTemp = normalizedTf(vocabulaire,doc)
    tf2 = []
    for term in tfTemp :
        if term == 0 :
            tf2.append(0)
        else :
            tf2.append(0.5 + 0.5*term)
    return tf2

def logarithmTf(vocabulaire, doc) :
    # tfTemp = tf(vocabulaire, doc)
    # tf3 = []
    # for term in tfTemp :
    #     if term == 0 :
    #         tf3.append(0)
    #     else :
    #         tf3.append(math.log(term,10)+1)
    tf3 = []
    a = 0
    i = 0
    for mot in vocabulaire:
        i = 0
        for term in doc:
            if mot == term:
                if i < 4:
                    a = a + 4
                a = a + 1
                i = i + 1
        if a == 0:
            tf3.append(0)
        else:
            tf3.append(math.log(a / (len(doc) - 1),10)+1)
        a = 0
    return tf3

def squaredTf(vocabulaire,doc):
    # tfTemp = tf(vocabuaire, doc)
    # tf4 = []
    # for term in tfTemp :
    #     tf4.append(term*term)
    # return tf4
    tf4 = []
    a = 0
    i = 0
    for mot in vocabulaire:
        i = 0
        for term in doc:
            if mot == term:
                if i < 4:
                    a = a + 4
                a = a + 1
                i = i + 1
        tf4.append((a / (len(doc) - 1))*(a / (len(doc) - 1)))
        a = 0
    return tf4

def idf(vocabulaire,list_doc):
    idf = []
    for mot in vocabulaire :
        a = 1
        for doc in list_doc :
            if mot in doc :
                a = a+1
        idf.append(math.log(len(list_doc)/(a),10))
    return idf

def probabilisticIdf(vocabulaire, list_doc):
    idf1 = []
    for mot in vocabulaire:
        a = 1
        for doc in list_doc:
            if mot in doc:
                a = a + 1
        idf1.append(math.log((len(list_doc)-a) / (a), 10))
    return idf1

def squaredIdf(vocabulaire, list_doc):
    idf2 = []
    for mot in vocabulaire:
        a = 1
        for doc in list_doc:
            if mot in doc:
                a = a + 1
        idf2.append((math.log(len(list_doc) / (a), 10))*(math.log(len(list_doc) / (a), 10)))
    return idf2

def tf_idf(vocabulaire,list_doc) :
    tfidf = []
    inverse= squaredIdf(vocabulaire,list_doc)
    print(inverse[0:3])
    for doc in list_doc :
        term_f = tf(vocabulaire,doc)
        temp = []
        for i in range(0,len(vocabulaire)) :
            temp.append(term_f[i]*(inverse[i]+0.1))
        tfidf.append(temp)
    test = tf(vocabulaire,list_doc[0])
    print(test[0:3])
    print(tfidf[0][0:3])

    return tfidf