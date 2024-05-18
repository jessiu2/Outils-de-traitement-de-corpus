import sys
import numpy as np
import pandas as pd
from scipy.stats import pearsonr

def compute_correlation(file_path):
    # Lire les données textuelles depuis le fichier
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = file.readlines()

    # Créer un DataFrame pour stocker la longueur de chaque texte et la fréquence du mot 'tourism'
    data = {'text_length': [], 'tourism_count': []}

    for text in text_data:
        length = len(text)  # Longueur du texte
        count = text.lower().count('tourism')  # Compter les occurrences du mot 'tourism'
        data['text_length'].append(length)
        data['tourism_count'].append(count)

    df = pd.DataFrame(data)

    # Calculer la corrélation
    correlation, _ = pearsonr(df['text_length'], df['tourism_count'])
    return correlation

if __name__ == '__main__':
    # Vérifier si le script a reçu suffisamment d'arguments
    if len(sys.argv) < 2:
        print("Utilisation : python correlation.py chemin-vers-fichier")
        sys.exit(1)  # Quitter le script indiquant que l'entrée n'était pas correcte

    file_path = sys.argv[1]
    correlation = compute_correlation(file_path)
    print("Corrélation entre la longueur du texte et la fréquence de 'tourism' :", correlation)

