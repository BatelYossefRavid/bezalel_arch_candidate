
import sys
import zipfile
import re
import os

sys.stdout.reconfigure(encoding='utf-8')
docx_path = r'c:\git\bezalel_arch_candidate\פרסומים לא אקדמים.docx'
if os.path.exists(docx_path):
    try:
        with open(docx_path, 'rb') as f:
            zip = zipfile.ZipFile(f)
            xml_content = zip.read('word/document.xml').decode('utf-8')
            text_content = re.sub('<[^<]+?>', '', xml_content)
            with open('clean.txt', 'w', encoding='utf-8') as outfile:
                outfile.write(text_content)
            print("Successfully wrote to clean.txt")
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print(f"File not found: {docx_path}")
