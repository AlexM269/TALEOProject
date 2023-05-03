import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Ouvrir le fichier .REL
with open("C:/Users/ewenc/Documents/INFO\GitHub/TALEOProject/CISI_dev.QRY", 'r') as file:
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

print(articles[0])
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
        if mot.lower() not in stop_words :
            liste_mots_sans_stopwords.append(mot)
    # Mettez à jour la liste de mots dans le tableau
    filtered_articles.append(liste_mots_sans_stopwords)
    liste_mots_sans_ponctuation = []
    liste_mots_sans_stopwords = []

print(filtered_articles[0])

# Convertir les articles filtrés en chaînes de caractères
preprocessed_articles = [' '.join(tokens) for tokens in filtered_articles]

print(preprocessed_articles[0])

# Initialiser le vecteuriseur TF-IDF
vectorizer = TfidfVectorizer()

# Calculer les poids TF-IDF pour chaque mot dans les articles
tfidf_matrix = vectorizer.fit_transform(preprocessed_articles)

# Obtenir les mots du vocabulaire (i.e., les mots présents dans les articles)
vocabulary = vectorizer.get_feature_names()

# Transformer la matrice TF-IDF en une liste de vecteurs
article_vectors = tfidf_matrix.toarray()

print(tfidf_matrix[0])