import sys
import spacy

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
        
def split_text(text, max_length=1000000):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]
    
def analyze_sentence_structure(text, nlp)
    doc = nlp(text)
    sentences = list(doc.sents)
    if len(sentences) == 0:
        return 0
    return sum(len(sent) for sent in sentences) / len(sentences)

def process_text_chunks(text_chunks, nlp):
    lengths = [analyze_sentence_structure(chunk, nlp) for chunk in text_chunks if len(chunk) > 0]
    if lengths:
        return sum(lengths) / len(lengths)
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_text_file>")
    else:
        file_path = sys.argv[1]
        text_corpus = load_text(file_path)

        nlp = spacy.load("fr_core_news_sm")

        nlp.max_length = max(len(text_corpus), nlp.max_length)

        text_chunks = split_text(text_corpus)
        
        average_sentence_length = analyze_sentence_structure(text_corpus)
        print("Longueur moyenne des phrases :", average_sentence_length)
