import nlpaug.augmenter.word as naw
import random
import nltk
import sys

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Fonction pour augmenter une ligne de texte
def augment_text(text, aug, num_aug=1):
    augmented_texts = []
    for _ in range(num_aug):
        augmented_text = aug.augment(text)
        if isinstance(augmented_text, list):
            augmented_text = ' '.join(augmented_text)
        augmented_texts.append(augmented_text)
    return augmented_texts

def main(input_file_path, output_file_path):
    # Charger les données
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Augmenteur utilisant des synonymes
    syn_aug = naw.SynonymAug(aug_src='wordnet')

    # Augmenter les données
    augmented_lines = []
    for line in lines:
        augmented_lines.extend(augment_text(line, syn_aug, num_aug=3))  # Augmenter chaque ligne 3 fois

    # Sauvegarder les données augmentées
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in augmented_lines:
            file.write(line + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    main(input_file_path, output_file_path)
