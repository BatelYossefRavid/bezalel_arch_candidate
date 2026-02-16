import os
import shutil

source_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching\הוראה"
target_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching_organized"

# Specific mapping for Bezalel files that are in the same folder
bezalel_map = {
    "אדריכלות אזרחית": "bezalel_civic",
    "מראה מקום": "bezalel_marei_makom"
}

if not os.path.exists(target_root):
    os.makedirs(target_root)

# Recursively find all files
for root, dirs, files in os.walk(source_root):
    # Determine target folder based on path or filename
    target_folder = None
    
    # Check parent folder name
    folder_name = root
    is_tech = any(k in folder_name for k in ["טכניון", "Technion"])
    is_sce = any(k in folder_name for k in ["SCE", "סמי שמעון"])
    is_bezalel = any(k in folder_name for k in ["בצלאל", "Bezalel"])
    
    if is_tech:
        if any(k in folder_name for k in ["חברתי", "Social"]): target_folder = "technion_social"
        elif any(k in folder_name for k in ["מבוא", "Intro"]): target_folder = "technion_intro"
        elif any(k in folder_name for k in ["עיצוב", "Design"]): target_folder = "technion_urban_studio"
    elif is_sce:
        if any(k in folder_name for k in ["HCI", "GIS"]): target_folder = "sce_hci_gis"
        elif any(k in folder_name for k in ["מדע", "Science"]): target_folder = "sce_city_science"
        elif any(k in folder_name for k in ["החדשנות", "Innovation"]): target_folder = "sce_innovation"
        elif any(k in folder_name for k in ["שכבות", "Layers"]): target_folder = "sce_layers"
        elif any(k in folder_name for k in ["דרום", "Global"]): target_folder = "sce_global_south"

    for i, file_name in enumerate(files):
        ext = os.path.splitext(file_name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png', '.gif', '.mp4']:
            continue
            
        file_target = target_folder
        
        # Override for Bezalel based on file name
        if is_bezalel:
            if "אזרחית" in file_name or "Civic" in file_name:
                file_target = "bezalel_civic"
            elif "מראה" in file_name or "Marei" in file_name:
                file_target = "bezalel_marei_makom"
            else:
                file_target = "bezalel_marei_makom" # Default Bezalel
        
        if not file_target:
            continue
            
        target_path = os.path.join(target_root, file_target)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            
        new_name = f"{file_target}_{i+1}{ext}"
        # Avoid collisions if walking nested folders
        count = 1
        while os.path.exists(os.path.join(target_path, new_name)):
            new_name = f"{file_target}_{i+1}_{count}{ext}"
            count += 1
            
        shutil.copy2(os.path.join(root, file_name), os.path.join(target_path, new_name))

print("Organization complete.")
