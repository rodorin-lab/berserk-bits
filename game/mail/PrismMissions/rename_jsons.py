import os
import sys

def rename_files(old_sub, new_sub):
    for filename in os.listdir('.'):
        if filename.endswith(".json") and old_sub in filename:
            new_filename = filename.replace(old_sub, new_sub)
            try:
                os.rename(filename, new_filename)
                print(f"Renamed: {filename} -> {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python rename_jsons.py <old_substring> <new_substring>")
        sys.exit(1)
    
    old_sub = sys.argv[1]
    new_sub = sys.argv[2]
    rename_files(old_sub, new_sub)

if __name__ == "__main__":
    main()
