import pandas as pd
import spacy
import sys

def load_data(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df

def annotate_text(text, nlp):
    # Process the text through the NLP pipeline
    doc = nlp(text)
    # Extract lemmas and parts of speech
    annotations = [{'text': token.text, 'lemma': token.lemma_, 'pos': token.pos_} for token in doc]
    return annotations

def main(file_path, output_path):
    # Load the French language model
    nlp = spacy.load('fr_core_news_sm')

    # Load the data
    df = load_data(file_path)

    # Apply annotation to each content of the article
    df['annotations'] = df['contenu'].apply(lambda x: annotate_text(x, nlp))

    # Display the first few annotations for verification
    print(df['annotations'].head())

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <path_to_input_csv> <path_to_output_csv>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        main(input_path, output_path)
