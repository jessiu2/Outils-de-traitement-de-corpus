import pandas as pd

def process_file(file_path):
    try:
        # Ouvrir et lire le fichier
        with open(file_path, 'r', encoding='utf-8') as file:
            articles = file.read().split('---\n\n')  # Séparer les articles par '---\n\n'
        
        # Analyser le contenu des articles
        data = []
        for article in articles:
            if article.strip():  # Vérifier que l'article n'est pas vide
                segments = article.strip().split('\n')
                title = ''
                url = ''
                content = []
                in_content = False  # Indicateur pour la capture du contenu
                for segment in segments:
                    if segment.startswith('Titre: '):
                        title = segment.replace('Titre: ', '').strip()
                        in_content = False  # Réinitialiser le marqueur de contenu
                    elif segment.startswith('Lien: '):
                        url = segment.replace('Lien: ', '').strip()
                        in_content = False  # Réinitialiser le marqueur de contenu
                    elif segment.startswith('Contenu:'):
                        in_content = True  # Commencer à capturer le contenu
                    elif in_content:
                        content.append(segment.strip())
                text = '\n'.join(content)
                data.append({
                    'id': len(data) + 1,  # Assigner un ID séquentiel
                    'url': url,
                    'title': title,
                    'text': text
                })
        
        # Créer un DataFrame à partir des données collectées
        df = pd.DataFrame(data)
        
        # Définir le chemin du fichier de sortie
        output_file_path = file_path.replace('.txt', '.csv')
        
        # Sauvegarder le DataFrame dans un fichier CSV, sans index et avec des virgules comme séparateurs
        df.to_csv(output_file_path, index=False, sep=',', encoding='utf-8', quotechar='"', quoting=1)
        
        print(f"Les données traitées ont été enregistrées dans '{output_file_path}'")

    except Exception as e:
        print(f"Une erreur s'est produite lors du traitement du fichier : {e}")

def main():
    # Demander le chemin du fichier à l'utilisateur
    file_path = input("Veuillez entrer le chemin du fichier txt : ")
    
    # Traiter le fichier spécifié
    process_file(file_path)

if __name__ == "__main__":
    main()
