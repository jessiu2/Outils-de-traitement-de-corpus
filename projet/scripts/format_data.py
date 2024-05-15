import pandas as pd

# lire le fichier
with open('cleaned_data.txt', 'r', encoding='utf-8') as file:
    articles = file.read().split('---\n\n')  

# analyser le contenu des articles
data = []
for article in articles:
    if article.strip():  
        lines = article.strip().split('\n')
        title = lines[0].replace('Title: ', '')  
        text = '\n'.join(lines[1:])  
        data.append({
            'id': '',  
            'url': '',  
            'title': title,
            'text': text
        })

# 创建DataFrame
df = pd.DataFrame(data)

# 保存DataFrame到CSV文件，不包含索引
df.to_csv('data/processed/wikipedia_articles.csv', index=False)
