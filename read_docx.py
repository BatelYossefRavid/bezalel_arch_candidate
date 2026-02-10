import zipfile
import re
import xml.etree.ElementTree as ET

def read_docx(file_path):
    try:
        with zipfile.ZipFile(file_path) as z:
            xml_content = z.read('word/document.xml')
            
            # Using lxml would be better but standard library is safer here
            # We need to register namespaces to find tags easily
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            tree = ET.fromstring(xml_content)
            
            full_text = []
            for p in tree.findall('.//w:p', ns):
                paragraph_text = []
                for t in p.findall('.//w:t', ns):
                    if t.text:
                        paragraph_text.append(t.text)
                
                if paragraph_text:
                    full_text.append("".join(paragraph_text))
            
            return "\n".join(full_text)
    except Exception as e:
        return f"Error: {str(e)}"

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python read_docx.py <input_docx> [output_txt]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "extracted.txt"
    
    content = read_docx(input_file)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Done. Content written to {output_file}")
