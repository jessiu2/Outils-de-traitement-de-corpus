import pandas as pd

def process_file(file_path):
    try:
        # Lire le fichier
        with open(file_path, 'r', encoding='utf-8') as file:
            articles = file.read().split('---\n\n')  
        
        # Analyser le contenu des articles
        data = []
        for article in articles:
            if article.strip():  # Vérifier si l'article n'est pas vide
                lines = article.strip().split('\n')
                title = lines[0].replace('Title: ', '')  # Extraire le titre
                text = '\n'.join(lines[1:])  # Extraire le texte
                data.append({
                    'id': '',  # Champ id vide pour l'instant
                    'url': '',  # Champ url vide pour l'instant
                    'title': title,
                    'text': text
                })
        
        # Créer un DataFrame
        df = pd.DataFrame(data)
        
        # Générer le chemin de fichier de sortie
        output_file_path = file_path.replace('.txt', '.csv')
        
        # Sauvegarder le DataFrame dans un fichier CSV, sans index
        df.to_csv(output_file_path, index=False)
        
        print(f"Les données traitées ont été enregistrées dans '{output_file_path}'")

    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")

def main():
    # Demander à l'utilisateur de saisir le chemin du fichier
    file_path = input("Veuillez saisir le chemin du fichier txt : ")
    
    # Appeler la fonction de traitement du fichier
    process_file(file_path)

if __name__ == "__main__":
    main()
