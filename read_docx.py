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

if __name__ == "__main__":
    content = read_docx("חזון לבצלאל.docx")
    with open("vision_content.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Done.")
