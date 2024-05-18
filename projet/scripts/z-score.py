import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv('corpus_wiki_fr_cleaned.txt', delimiter='\t')

# Calculer les z-scores
from scipy import stats
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))

# Définir un seuil (par exemple, 3)
threshold = 3
outliers = (z_scores > threshold)

# Supprimer les lignes avec des outliers
df_cleaned = df[(outliers == False).all(axis=1)]

# Sauvegarder les données nettoyées
df_cleaned.to_csv('corpus_wiki_fr_cleaned_cleaned.txt', sep='\t', index=False)
