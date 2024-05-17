import pandas as pd
import sys

def process_file(file_path):
    # Initialiser les listes vides pour stocker les données
    ids = []
    urls = []
    titres = []
    contenus = []

    # Lire le fichier et traiter chaque bloc
    with open(file_path, 'r', encoding='utf-8') as file:
        current_id = 1
        url = ''
        titre = ''
        contenu = []
        for line in file:
            if line.startswith('Lien:'):
                url = line.strip().split('Lien: ')[1]
            elif line.startswith('Titre:'):
                titre = line.strip().split('Titre: ')[1]
            elif line.strip() == '' and titre:  # Fin d'un bloc
                # Stocker les données collectées
                ids.append(current_id)
                urls.append(url)
                titres.append(titre)
                contenus.append(' '.join(contenu))
                # Préparer pour le prochain bloc
                current_id += 1
                url = ''
                titre = ''
                contenu = []
            else:
                contenu.append(line.strip())

    # Créer un DataFrame
    df = pd.DataFrame({
        'id': ids,
        'url': urls,
        'titre': titres,
        'contenu': contenus
    })

    # Déterminer le chemin du fichier CSV de sortie basé sur le chemin d'entrée
    csv_file_path = file_path.replace('.txt', '.csv')
    df.to_csv(csv_file_path, index=False)

    print(f'Les données ont été enregistrées avec succès dans {csv_file_path}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python script.py <chemin_vers_le_fichier>")
    else:
        process_file(sys.argv[1])
