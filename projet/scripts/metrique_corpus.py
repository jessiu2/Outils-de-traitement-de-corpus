import nltk
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from textstat.textstat import textstatistics
from sentence_transformers import SentenceTransformer, util
import argparse

nltk.download('punkt')

# Fonction pour analyser les arguments de la ligne de commande
def parse_args():
    parser = argparse.ArgumentParser(description="Évaluer le corpus avec diverses métriques")
    parser.add_argument("input_file", type=str, help="Chemin vers le fichier d'entrée")
    return parser.parse_args()

# Diversité lexicale - Rapport Type-Token
def type_token_ratio(tokens):
    return len(set(tokens)) / len(tokens)

# Yule's K
def yules_k(tokens):
    token_counts = Counter(tokens)
    M1 = sum(token_counts.values())
    M2 = sum(f * f for f in token_counts.values())
    return (M1 * M1) / (M2 - M1)

# Lisibilité - Indice de Flesch
def flesch_reading_ease(text):
    return textstatistics().flesch_reading_ease(text)

# Fonction principale
def main(input_file_path):
    # Charger les données
    with open(input_file_path, 'r', encoding='utf-8') as file:
        corpus = file.read()

    # Tokenisation
    tokens = word_tokenize(corpus)
    sentences = sent_tokenize(corpus)

    # Calculer la diversité lexicale
    ttr = type_token_ratio(tokens)
    yules_k_score = yules_k(tokens)

    # Calculer la cohérence locale - Utilisation des embeddings de phrases (BERT)
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    sentence_embeddings = model.encode(sentences)
    cosine_scores = util.pytorch_cos_sim(sentence_embeddings, sentence_embeddings)
    local_coherence = np.mean(cosine_scores.numpy())

    # Calculer la lisibilité
    flesch_score = flesch_reading_ease(corpus)

    # Afficher les résultats
    print(f"Rapport Type-Token: {ttr}")
    print(f"Yule's K: {yules_k_score}")
    print(f"Cohérence Locale (Similarité Cosinus Moyenne): {local_coherence}")
    print(f"Indice de Lisibilité de Flesch: {flesch_score}")

if __name__ == "__main__":
    args = parse_args()
    main(args.input_file)
