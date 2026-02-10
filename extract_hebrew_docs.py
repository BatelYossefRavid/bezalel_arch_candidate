
import docx
import os

files = [
    'מה המונח לי על השוחן.docx', 
    'עבודות בתחום אדריכלות- העבר ההרחוק.docx', 
    'בצלאל ראשית דבר------.docx', 
    'קורות חיים.docx'
]

for i, f in enumerate(files):
    try:
        # Use simple ASCII name for output file
        out_name = f'extracted_doc_{i}.txt'
        
        if not os.path.exists(f):
            print(f"Skipping {i}: File not found")
            continue
            
        doc = docx.Document(f)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
            
        with open(out_name, 'w', encoding='utf-8') as out:
            out.write('\n'.join(full_text))
            
        print(f"Successfully extracted content from file {i} to {out_name}")
        
    except Exception as e:
        print(f"Error processing file {i}: {str(e)}")
