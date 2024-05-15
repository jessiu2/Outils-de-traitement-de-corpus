import wikipedia
import re

def get_wikipedia_data(language="fr", page_titles=[], num_pages=10):
    wikipedia.set_lang(language)
    data = []

    for title in page_titles:
        try:
            page = wikipedia.page(title)
            data.append({
                "id": page.pageid,
                "url": page.url,
                "title": page.title,
                "text": page.content
            })
        except wikipedia.exceptions.PageError:
            print(f"Page '{title}' does not exist on {language} Wikipedia.")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Ambiguous title '{title}' on {language} Wikipedia: {e.options}")

        if len(data) >= num_pages:
            break
    
    return data

def clean_text(text):
    cleaned_text = re.sub(r'<.*?>', '', text)
    cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

page_titles = ["inalco", "NLP", "Vin"]
corpus_data = get_wikipedia_data(language="fr", page_titles=page_titles, num_pages=10)

output_file = "corpus_wikifr.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for article in corpus_data:
        cleaned_text = clean_text(article["text"])
        f.write(f"ID: {article['id']}\n")
        f.write(f"Title: {article['title']}\n")
        f.write(f"URL: {article['url']}\n")
        f.write(cleaned_text + "\n")
        f.write("="*50 + "\n")

with open("corpus_wikifr.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
