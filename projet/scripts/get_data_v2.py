import requests
from bs4 import BeautifulSoup

def get_recent_changes(date):
    base_url = "https://fr.wikipedia.org/w/api.php"
    params = {
        "action": "query",  # Type d'action pour l'API
        "format": "json",  # Format de la réponse
        "list": "recentchanges",  # Demander la liste des modifications récentes
        "rcstart": f"{date}T00:00:00Z",  # Heure de début pour les changements récents
        "rcend": f"{date}T23:59:59Z",  # Heure de fin pour les changements récents
        "rcprop": "title|ids",  # Propriétés à retourner : ici, les titres et les IDs des pages
        "rclimit": "max",  # Limite du nombre de résultats retournés (max pour le maximum possible)
        "rcnamespace": "0",  # Seulement l'espace de noms principal (articles)
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    print(response.json()) 
    titles = [change['title'] for change in data['query']['recentchanges']]
    return titles

def fetch_wikipedia_article(title):
    url = f"https://fr.wikipedia.org/wiki/{title.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find('div', {'id': 'mw-content-text'}).text
    return text

# Récupérer les titres des articles modifiés à une date spécifiée
titles = get_recent_changes("2024-05-15")
with open("articles_wiki.txt", 'w', encoding='utf-8') as file:
    for title in titles:
        try:
            article_text = fetch_wikipedia_article(title)
            file.write(f"Title: {title}\n{article_text}\n\n---\n\n")
        except Exception as e:
            print(f"Échec de la récupération de {title}: {str(e)}")
