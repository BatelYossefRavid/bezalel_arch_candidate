import os

source_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching\הוראה"
folders = os.listdir(source_root)

with open(r"c:\git\bezalel_arch_candidate\folder_dump.txt", "w", encoding="utf-8") as f:
    for folder in folders:
        f.write(f"Folder: {folder}\n")
        f.write(f"Hex: {folder.encode('utf-8').hex()}\n")
        f.write("-" * 20 + "\n")
