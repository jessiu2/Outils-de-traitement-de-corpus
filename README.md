## Cours 1
### Tâche  
Text Generation, sous-tâche de language-modeling
### Corpus choisi
wikipedia/20220301fr (https://huggingface.co/datasets/wikipedia#20220301fr)
C'est un corpus de Wikipédia en français
### Type de prédiction possible 
Ce corpus peut être utilisé pour plusieurs types de prédictions dans le domaine du traitement automatique du langage tels que classification de texte et génération de texte, etc.
### Modèles utilisés 
Ce corpus a pu servir à l'entraînement de divers modèles de traitement automatique du langage. Pour les modèles de génération de texte : En utilisant ce corpus comme ensemble de données d'entraînement, les développeurs peuvent entraîner des modèles de génération de texte capables de produire du texte en chinois simplifié, par exemple pour la traduction automatique ou la génération de contenu.
### Autres
Ce corpus a une taille de 128 Mo qui contient les articles en chinois simplifié. Il est construit à partir des fichiers de sauvegarde de Wikipédia （https://dumps.wikimedia.org/）. Chaque exemple contient le contenu d'un article complet de Wikipédia après un traitement pour supprimer le markdown et les sections non désirées (références, etc.).

## Cours 2
Au début, j'utilisais la bibliothèque `wikipedia` pour obtenir le contenu des pages de titres spécifiques sur le site de Wikipédia. Cependant, en raison du manque de généralité de cette méthode, j'ai réécrit un script en utilisant les bibliothèques `requests` et `BeautifulSoup`. Ce script, nommé `get_data2.py`, qui extrait automatiquement le contenu de chaque page de 200 articles sur le thème du "tourisme" à partir de la version française de Wikipedia.

Ensuite, pour le texte récupéré, j'utilise le script `clean_data.py` pour nettoyer les données.

Enfin, je fais appel à la bibliothèque `pandas` pour formater les données afin de correspondre au format du corpus choisi lors de la première leçon. Les données sont sauvegardées au format CSV en utilisant le script `format_data.py`.

## Cours 3
### Ouvrir le Corpus avec Pandas
J'ai écrit un script `read_corpus.py` qui ouvrir un csv avec Pandas et qui accept un chemin de fichier comme un argument.
En fait, pour le travail du cours 2, on a déjà transformé le corpus de `.txt` à `.csv`.

### Lancer l'Annotation Morphosyntaxique
Utilisation de module spacy pour effectuer des annotations morphosyntaxiques sur le contenu de chaque article, et sauvegarder les résultats, voir `annoter_corpus.py`.

## Cours 4
### TP2
Hugging Face Datasets offre des méthodes et des outils pour évaluer la qualité du texte comme calculer la longueur du texte, la diversité lexicale, la structure des phrases, et d'autres indicateurs. De plus, il est également possible d'utiliser des modèles pré-entraînés pour calculer la similarité sémantique des textes, ce qui permet une évaluation plus approfondie de la qualité du texte.

J'ai écrit aussi des scripts pour évaluer mon corpus selon ces indicateurs, voir `calcul_corpus.py` qui calculer la diversité lexicale et `structure_corpus.py` qui calculer la longueur moyenne des phrases. Lors du calcul de la longueur moyenne des phrases du texte, étant donné que la longueur maximale par défaut des textes dans spaCy est de 1 000 000 de caractères et que la longueur de mon corpus texte est de 2 015 529, j'ai donc divisé le texte en parties plus petites, puis j'ai traité chaque partie séparément.

### TP3
Voir `visualisation_corpus.py`

## Cours 5
### Corrélation 
Mon corpus est basé sur des textes collectés par une recherche sur le mot-clé "tourism", donc j'ai écrit un script `correlation_corpus.py` pour calculer le coefficient de corrélation de Pearson entre la longueur des textes et la fréquence du mot "tourism". Le résultat obtenu est d'environ 0,376, ce qui signifie qu'il existe une légère corrélation positive entre les deux variables.

Si la p-value n'est pas significative, on peut utiliser quelques approches pour augmenter, par exemple, augmenter la taille de l'échantillon, contrôler les variables confondantes ou améliorer la qualité des données. 

### Eliminer les données abérrantes
pour détecter et éliminer des données aberrantes, j'utilisé la méthode du Z-score dans le script `z-score.py`.

### Augmenter ses données
Voir le code `augmenter_corpus.py` utilisant la bibliothèque `nlpaug` pour augmenter des données textuelles, ici, j'ai utilisé des synonymes comme la méthode de l'augmentation.
