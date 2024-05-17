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
                segments = article.strip().split('\n')
                title = ''
                url = ''
                content = []
                content_flag = False
                for segment in segments:
                    if segment.startswith('Titre: '):
                        title = segment.replace('Titre: ', '')
                    elif segment.startswith('Lien: '):
                        url = segment.replace('Lien: ', '')
                    elif segment.startswith('Contenu:'):
                        content_flag = True
                    elif content_flag:
                        content.append(segment)
                text = '\n'.join(content)
                data.append({
                    'id': len(data) + 1,  # Assign sequential IDs starting from 1
                    'url': url,
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
