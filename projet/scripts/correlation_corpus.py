import numpy as np
import pandas as pd
from scipy.stats import pearsonr

with open('~/Outils-de-traitement-de-corpus/projet/data/processed/corpus_wiki_fr_cleaned.txt', 'r', encoding='utf-8') as file:
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
print("Corrélation entre la longueur du texte et la fréquence de 'tourism' :", correlation)
