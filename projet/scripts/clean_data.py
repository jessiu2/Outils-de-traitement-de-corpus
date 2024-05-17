import re

def clean_txt_file(file_path):
    try:
        # Lire le contenu du fichier
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Utiliser une expression régulière pour supprimer les références de type "[1]" de chaque ligne
        cleaned_lines = [re.sub(r'\[\d+\]', '', line).strip() for line in lines]
        
        # Enregistrer les données nettoyées dans un nouveau fichier
        cleaned_file_path = file_path.replace('.txt', '_cleaned.txt')
        with open(cleaned_file_path, 'w', encoding='utf-8') as file:
            for line in cleaned_lines:
                file.write(line + '\n')  # Write each line and maintain original line breaks
        
        print(f"\nLes données nettoyées ont été enregistrées dans '{cleaned_file_path}'")

    except Exception as e:
        print(f"Erreur lors du traitement du fichier : {e}")

def main():
    # Demander à l'utilisateur de saisir le chemin du fichier
    file_path = input("Veuillez saisir le chemin du fichier : ")
    
    # Appeler la fonction de nettoyage des données
    clean_txt_file(file_path)

if __name__ == "__main__":
    main()
