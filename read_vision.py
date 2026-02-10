import docx
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
try:
    doc = docx.Document('c:\\git\\bezalel_arch_candidate\\בצלאל ראשית דבר------.docx')
    for p in doc.paragraphs:
        print(p.text)
except Exception as e:
    print(f'Error: {e}')
