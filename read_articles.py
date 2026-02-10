import docx
import os

docx_path = 'articles.docx'
if not os.path.exists(docx_path):
    print("File not found")
    exit()

doc = docx.Document(docx_path)
full_text = []
for para in doc.paragraphs:
    full_text.append(para.text)

with open('articles_content.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(full_text))

print("Content extracted to articles_content.txt")
