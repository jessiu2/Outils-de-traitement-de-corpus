import sys
import matplotlib.pyplot as plt
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist
from textblob import TextBlob
from collections import Counter

def load_corpus(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_text_statistics(text):
    return {
        'char_count': len(text),
        'word_count': len(word_tokenize(text)),
        'sentence_count': len(sent_tokenize(text))
    }

def plot_text_length_distribution(texts):
    text_lengths = [calculate_text_statistics(text) for text in texts]
    df_lengths = pd.DataFrame(text_lengths)

    fig, ax = plt.subplots(3, 1, figsize=(8, 12))
    df_lengths['char_count'].hist(ax=ax[0], bins=30)
    ax[0].set_title('Character Count Distribution')
    df_lengths['word_count'].hist(ax=ax[1], bins=30)
    ax[1].set_title('Word Count Distribution')
    df_lengths['sentence_count'].hist(ax=ax[2], bins=30)
    ax[2].set_title('Sentence Count Distribution')
    plt.tight_layout()
    plt.show()

def plot_zipfs_law(text):
    all_words = word_tokenize(text.lower())
    freq_dist = FreqDist(all_words)
    ranks = range(1, len(freq_dist) + 1)
    frequencies = [freq for _, freq in freq_dist.most_common()]
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, marker=".")
    plt.title('Zipf\'s Law - Log-Log Plot of Word Frequencies')
    plt.xlabel('Rank of words')
    plt.ylabel('Frequency of words')
    plt.grid(True)
    plt.show()

def perform_sentiment_analysis(texts):
    sentiments = [TextBlob(text).sentiment.polarity for text in texts]
    plt.figure(figsize=(10, 6))
    plt.hist(sentiments, bins=30, color='blue')
    plt.title('Sentiment Polarity Distribution')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Number of Documents')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_corpus_file>")
    else:
        file_path = sys.argv[1]
        corpus_text = load_corpus(file_path)
        texts = corpus_text.split('\n\n')  # Assuming documents are separated by two newlines
        plot_text_length_distribution(texts)
        plot_zipfs_law(corpus_text)
        perform_sentiment_analysis(texts)
