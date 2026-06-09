import os
import sys
import re

def replace_in_file(filename, target, replacement):
    try:
        # Read the entire file content
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Use re.subn to perform a case-insensitive replacement and count occurrences.
        updated_content, count = re.subn(re.escape(target), replacement, content, flags=re.IGNORECASE)
        
        if count > 0:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated {filename}: replaced {count} occurrence(s).")
        else:
            print(f"No occurrences found in {filename}.")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <target_string> <replacement_string>")
        sys.exit(1)
    
    target_string = sys.argv[1]
    replacement_string = sys.argv[2]

    # Process all JSON files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith(".json"):
            replace_in_file(filename, target_string, replacement_string)

if __name__ == "__main__":
    main()
