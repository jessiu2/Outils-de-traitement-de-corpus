import requests
from bs4 import BeautifulSoup
import time

# URL de base et modèle de l'URL de recherche pour Wikipedia
base_url = "https://fr.wikipedia.org"
search_url_template = "https://fr.wikipedia.org/w/index.php?search={}&title=Spécial:Recherche&profile=advanced&fulltext=1&ns0=1&offset={}"

def fetch_article_links(search_term, max_articles=200):
    article_urls = []
    offset = 0
    # Continuer à chercher jusqu'à atteindre le nombre maximum d'articles
    while len(article_urls) < max_articles:
        search_url = search_url_template.format(search_term, offset)
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            search_results = soup.find_all('div', class_='mw-search-result-heading')
            for result in search_results:
                link = result.find('a')
                if link and link.get('href'):
                    article_urls.append(base_url + link.get('href'))
                    if len(article_urls) >= max_articles:
                        break
            # Préparer la pagination pour la page de résultats suivante
            offset += 20
        else:
            break  # Arrêter la boucle si la réponse du serveur n'est pas appropriée
        time.sleep(1)  # Délai respectueux pour éviter de surcharger le serveur
    return article_urls

def fetch_article_content(article_url):
    response = requests.get(article_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').get_text()
        paragraphs = soup.find_all('p')
        article_text = '\n'.join(p.get_text() for p in paragraphs)
        return f"Titre: {title}\nLien: {article_url}\nContenu:\n{article_text}\n\n"
    return ''

# Fonction principale de scraping
def scrape_wikipedia(search_term, max_articles=200, filename='tourisme_search_corpus_francais.txt'):
    article_urls = fetch_article_links(search_term, max_articles)
    corpus = ""
    for url in article_urls:
        print(f"Récupération: {url}")
        corpus += fetch_article_content(url)
        time.sleep(1)  # Délai respectueux pour éviter de surcharger le serveur

    # Sauvegarder le corpus dans un fichier local
    with open('corpus_wiki_fr.txt', 'w', encoding='utf-8') as file:
        file.write(corpus)
    print(f"Le corpus a été créé avec succès et enregistré dans 'corpus_wiki_fr.txt'")

# Exemple d'utilisation
scrape_wikipedia("tourisme", 200)
