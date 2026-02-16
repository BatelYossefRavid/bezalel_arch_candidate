import os

source_root = r"c:\git\bezalel_arch_candidate\assets\images\teaching\הוראה"

folders = os.listdir(source_root)
for f in folders:
    print(f"Name: {f}")
    try:
        print(f"  Encoded: {f.encode('utf-8')}")
    except:
        print("  Could not encode")
    print(f"  Length: {len(f)}")
    # Check if any keywords match
    keywords = ["בצלאל", "אזרחית", "אדריכלות", "civic"]
    matches = [k for k in keywords if k in f]
    print(f"  Matches: {matches}")
