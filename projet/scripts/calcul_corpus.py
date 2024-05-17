import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import sys

nltk.download('punkt')

def diversite_lexicale(texte):
    tokens = word_tokenize(texte)
    return len(set(tokens)) / len(tokens)

def lire_corpus(file_path):
    # Ouvrir et lire le fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        texte_corpus = file.read()
    return texte_corpus

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_corpus_file>")
    else:
        file_path = sys.argv[1]
        texte_corpus = lire_corpus(file_path)
        score_diversite = diversite_lexicale(texte_corpus)
        print("Diversité lexicale :", score_diversite)
