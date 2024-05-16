import requests
from bs4 import BeautifulSoup
import time

# URL de la page de catégorie "Culture" sur Wikipédia en français
start_url = "https://fr.wikipedia.org/wiki/Catégorie:Culture"
base_url = "https://fr.wikipedia.org"
visited_urls = set()
corpus = ''

def get_article_links(category_url):
    response = requests.get(category_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Trouver tous les liens vers les pages d'articles
        links = soup.select('.mw-category-group a, .mw-category-generated a')
        article_urls = [base_url + link.get('href') for link in links if link.get('href').startswith('/wiki/')]
        return article_urls
    return []

def get_article_content(article_url):
    response = requests.get(article_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ''
        for p in paragraphs:
            article_text += p.get_text()
        return article_text
    return ''

# Obtenir les liens d'articles à partir de la page de catégorie
article_urls = get_article_links(start_url)

# Extraire le contenu de chaque article
for url in article_urls:
    if url not in visited_urls:
        print(f"Récupération de : {url}")
        article_content = get_article_content(url)
        corpus += article_content + '\n'
        visited_urls.add(url)
        time.sleep(1)  # Pause d'une seconde pour éviter de surcharger le serveur

        # Limiter le nombre d'articles pour éviter une extraction infinie
        if len(visited_urls) >= 300:
            break

# Enregistrer le corpus dans un fichier local
with open('corpus_francais.txt', 'w', encoding='utf-8') as file:
    file.write(corpus)

print("Le corpus a été créé avec succès et enregistré dans 'corpus_francais.txt'")
