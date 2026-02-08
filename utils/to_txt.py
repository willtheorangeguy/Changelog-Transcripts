import sys
from pathlib import Path

def convert_md_to_txt(root_dir):
    root_path = Path(root_dir)

    if not root_path.exists() or not root_path.is_dir():
        print(f"Error: '{root_dir}' is not a valid directory.")
        sys.exit(1)

    for md_file in root_path.rglob("*.md"):
        txt_file = md_file.with_suffix(".txt")

        try:
            with md_file.open("r", encoding="utf-8") as f:
                content = f.read()

            with txt_file.open("w", encoding="utf-8") as f:
                f.write(content)

            print(f"Converted: {md_file} -> {txt_file}")

        except Exception as e:
            print(f"Failed to convert {md_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python to_txt.py <directory>")
        sys.exit(1)

    convert_md_to_txt(sys.argv[1])
