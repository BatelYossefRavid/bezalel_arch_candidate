import re

try:
    with open('page_source.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Find og:image
    og_match = re.search(r'og:image\" content=\"([^\"]+)', content)
    if og_match:
        print(f"OG Image: {og_match.group(1)}")
        
    # Find all jpg/png
    images = re.findall(r'https?://[^\s\"\'<>]+?\.(?:jpg|png)', content)
    print("All Images:")
    for img in images:
        print(img)
        
except Exception as e:
    print(f"Error: {e}")
