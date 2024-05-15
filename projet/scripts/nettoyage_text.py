import re

def clean_text(text):
    # Supprimer les balises HTML
    text = re.sub('<[^<]+?>', '', text)
    # Remplacer les caractères spéciaux et les espaces superflus
    text = re.sub('\s+', ' ', text).strip()
    return text

cleaned_text = clean_text(text)
print(cleaned_text[:500])  # Imprimer les 500 premiers caractères du texte nettoyé
