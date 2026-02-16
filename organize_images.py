import os
import shutil

source_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching\הוראה"
target_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching_organized"

# Mapping Hebrew/Complex folder names to simple English names
mapping = {
    " סמי שמעון- הדרום הגלובי SCE": "sce_global_south",
    " SCE מדע נתונים": "sce_city_science",
    "עיצוב עירוני- רובע החדשנות SCE": "sce_innovation",
    "HCI+GIS SCE": "sce_hci_gis",
    "שכבות במרחב האורבני SCE": "sce_layers",
    "טכניון עיצוב עירוני": "technion_urban_studio",
    "טכניון - מבוא לעיצוב עירוני": "technion_intro",
    "טכניון תכנון חברתי": "technion_social",
    "בצלאל סטודיו אדריכלות אזרחית": "bezalel_civic",
    "בצלאל מראה מקום": "bezalel_marei_makom"
}

if not os.path.exists(target_root):
    os.makedirs(target_root)

for folder_name in os.listdir(source_root):
    source_path = os.path.join(source_root, folder_name)
    if not os.path.isdir(source_path):
        continue
    
    # Try to find a match in mapping
    target_folder = None
    for heb, eng in mapping.items():
        if heb in folder_name or folder_name in heb:
            target_folder = eng
            break
    
    if not target_folder:
        continue
    
    target_path = os.path.join(target_root, target_folder)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    try:
        files = [f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))]
        for i, file_name in enumerate(files):
            ext = os.path.splitext(file_name)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.gif', '.mp4']:
                new_name = f"{target_folder}_{i+1}{ext}"
                shutil.copy2(os.path.join(source_path, file_name), os.path.join(target_path, new_name))
    except Exception:
        continue

print("Organization complete.")
