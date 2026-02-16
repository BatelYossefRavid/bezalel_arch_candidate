
import os

def replace_vision_content():
    file_path = 'c:\\git\\bezalel_arch_candidate\\index.html'
    vision_path = 'c:\\git\\bezalel_arch_candidate\\vision_final.txt'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    with open(vision_path, 'r', encoding='utf-8') as f:
        new_vision_text = f.read()

    # Format new vision text into HTML paragraphs
    paragraphs = new_vision_text.strip().split('\n')
    html_content = '<!-- Vision Chapters -->\n<div class="space-y-8 text-xl font-light leading-relaxed text-gray-800">\n'
    
    # Title from first line
    if paragraphs:
        title = paragraphs[0]
        html_content += f'    <h3 class="text-3xl font-black mb-10 font-arch border-b-2 border-black pb-4 inline-block">{title}</h3>\n'
        paragraphs = paragraphs[1:]

    for p in paragraphs:
        if p.strip():
            html_content += f'    <p>{p.strip()}</p>\n'
    
    html_content += '</div>'

    # Markers for replacement
    start_marker = '<!-- Chapter 1: Introduction -->'
    # We look for the end of the article content, which is before </article> but specifically after Chapter 7
    # Use a unique string from Chapter 7's end to be safe, or just find the start marker and look for the next </article>
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("Start marker not found!")
        return

    # Find the </article> tag after the start marker
    end_marker = '</article>'
    end_idx = content.find(end_marker, start_idx)
    
    if end_idx == -1:
        print("End marker not found!")
        return

    # Within this range, we want to replace everything. 
    # But wait, </article> is line 3562. The content ends at line 3560 (</div>). 
    # We should keep </article>.
    # So we replace from start_idx up to end_idx (exclusive of </article>).
    # We also need to preserve the whitespace before </article> if we care, but it's HTML.
    
    # Let's check if there are other things we might delete by accident.
    # The structure is:
    # <article>
    #   Preface...
    #   <!-- Chapter 1 ... -->
    #   ...
    #   <!-- Chapter 7 ... -->
    #   ...
    # </article>
    
    # So replacing from '<!-- Chapter 1' to just before '</article>' should work perfectly.

    new_content = content[:start_idx] + html_content + '\n\n                    ' + content[end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Successfully replaced vision content.")

if __name__ == '__main__':
    replace_vision_content()
