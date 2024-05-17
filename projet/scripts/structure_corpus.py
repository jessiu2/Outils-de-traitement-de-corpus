import sys
import spacy

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_sentence_structure(text):
    nlp = spacy.load("fr_core_news_sm")
    doc = nlp(text)
    sentences = list(doc.sents)
    if len(sentences) == 0:
        return 0
    return sum(len(sent) for sent in sentences) / len(sentences)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_text_file>")
    else:
        file_path = sys.argv[1]
        text_corpus = load_text(file_path)
        average_sentence_length = analyze_sentence_structure(text_corpus)
        print("Longueur moyenne des phrases :", average_sentence_length)
