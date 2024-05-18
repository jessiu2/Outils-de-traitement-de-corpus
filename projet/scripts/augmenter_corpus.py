import nlpaug.augmenter.word as naw
import random
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Charger les données
with open('/Outils-de-traitement-de-corpus/projet/data/processed/corpus_wiki_fr_cleaned.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Fonction pour augmenter une ligne de texte
def augment_text(text, aug, num_aug=1):
    augmented_texts = []
    for _ in range(num_aug):
        augmented_text = aug.augment(text)
        augmented_texts.append(augmented_text)
    return augmented_texts

# Augmenteur utilisant des synonymes
syn_aug = naw.SynonymAug(aug_src='wordnet')

# Augmenter les données
augmented_lines = []
for line in lines:
    augmented_lines.extend(augment_text(line, syn_aug, num_aug=3))  # Augmenter chaque ligne 3 fois

# Sauvegarder les données augmentées
with open('/mnt/data/corpus_wiki_fr_cleaned_augmented.txt', 'w', encoding='utf-8') as file:
    for line in augmented_lines:
        file.write(line + "\n")
