import os
import shutil

source_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching\הוראה"
target_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching_organized"

# Using key words to match
keywords = {
    "global": "sce_global_south",
    "דרום": "sce_global_south",
    "גלובי": "sce_global_south",
    "מדע": "sce_city_science",
    "science": "sce_city_science",
    "החדשנות": "sce_innovation",
    "innovation": "sce_innovation",
    "HCI": "sce_hci_gis",
    "GIS": "sce_hci_gis",
    "שכבות": "sce_layers",
    "layers": "sce_layers",
    "עיצוב עירוני": "technion_urban_studio",
    "מבוא": "technion_intro",
    "חברתי": "technion_social",
    "social": "technion_social",
    "אזרחית": "bezalel_civic",
    "civic": "bezalel_civic",
    "מראה מקום": "bezalel_marei_makom",
}

# Special handling for "עיצוב עירוני" which appears in SCE and Tech.
# Tech Tech folder has "טכניון" or tech
# SCE folders have SCE or סמי שמעון

if not os.path.exists(target_root):
    os.makedirs(target_root)

for folder_name in os.listdir(source_root):
    source_path = os.path.join(source_root, folder_name)
    if not os.path.isdir(source_path):
        continue
    
    target_folder = None
    
    # Check for Technion vs SCE vs Bezalel keywords
    is_tech = any(k in folder_name for k in ["טכניון", "Technion"])
    is_sce = any(k in folder_name for k in ["SCE", "סמי שמעון", "סמואל"])
    is_bezalel = any(k in folder_name for k in ["בצלאל", "Bezalel"])
    
    if is_tech:
        if any(k in folder_name for k in ["חברתי", "Social"]):
            target_folder = "technion_social"
        elif any(k in folder_name for k in ["מבוא", "Intro"]):
            target_folder = "technion_intro"
        elif any(k in folder_name for k in ["עיצוב", "Design"]):
            target_folder = "technion_urban_studio"
    elif is_sce:
        if any(k in folder_name for k in ["HCI", "GIS"]):
            target_folder = "sce_hci_gis"
        elif any(k in folder_name for k in ["מדע", "Science"]):
            target_folder = "sce_city_science"
        elif any(k in folder_name for k in ["החדשנות", "Innovation"]):
            target_folder = "sce_innovation"
        elif any(k in folder_name for k in ["שכבות", "Layers"]):
            target_folder = "sce_layers"
        elif any(k in folder_name for k in ["דרום", "Global"]):
            target_folder = "sce_global_south"
    elif is_bezalel:
        if any(k in folder_name for k in ["אזרחית", "Civic"]):
            target_folder = "bezalel_civic"
        elif any(k in folder_name for k in ["מראה", "Marei"]):
            target_folder = "bezalel_marei_makom"

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
                new_full_path = os.path.join(target_path, f"{target_folder}_{i+1}{ext}")
                shutil.copy2(os.path.join(source_path, file_name), new_full_path)
    except Exception:
        pass

print("Organization complete.")
