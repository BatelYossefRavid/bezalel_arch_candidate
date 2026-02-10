
import zipfile
import os
import shutil

docx_path = "c:\\git\\bezalel_arch_candidate\\מה המונח לי על השוחן.docx"
output_dir = "c:\\git\\bezalel_arch_candidate\\extracted_media"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extract_images_from_docx(path, output_folder):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.startswith('word/media/'):
                zip_ref.extract(file, output_folder)
                # Move to flat structure
                source = os.path.join(output_folder, file)
                filename = os.path.basename(file)
                dest = os.path.join(output_folder, filename)
                shutil.move(source, dest)
    
    # Clean up word directory
    shutil.rmtree(os.path.join(output_folder, 'word'), ignore_errors=True)
    print(f"Extracted images to {output_folder}")
    # List files
    files = os.listdir(output_folder)
    print("Files found:", files)

extract_images_from_docx(docx_path, output_dir)
