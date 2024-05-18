import pandas as pd
import numpy as np
import sys
from scipy import stats

def clean_data(input_file_path, output_file_path):
    # Charger les données
    df = pd.read_csv(input_file_path, delimiter='\t')

    # Calculer les z-scores
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))

    # Définir un seuil (par exemple, 3)
    threshold = 3
    outliers = (z_scores > threshold)

    # Supprimer les lignes avec des outliers
    df_cleaned = df[(outliers == False).all(axis=1)]

    # Sauvegarder les données nettoyées
    df_cleaned.to_csv(output_file_path, sep='\t', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    clean_data(input_file_path, output_file_path)
