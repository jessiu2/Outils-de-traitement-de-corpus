import pandas as pd
from sklearn.model_selection import train_test_split
import sys

def split_data(input_file_path, train_file_path, test_file_path, test_size=0.2, random_state=42):
    # Charger les données
    df = pd.read_csv(input_file_path, delimiter='\t')

    # Diviser les données en ensembles d'entraînement et de test
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)

    # Sauvegarder les ensembles d'entraînement et de test
    train_df.to_csv(train_file_path, sep='\t', index=False)
    test_df.to_csv(test_file_path, sep='\t', index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file_path> <train_file_path> <test_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    train_file_path = sys.argv[2]
    test_file_path = sys.argv[3]

    split_data(input_file_path, train_file_path, test_file_path)
