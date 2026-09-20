import re
from pathlib import Path

ROOT = Path("/home/user/project")
build_py = ROOT / "build_book.py"
content = build_py.read_text(encoding="utf-8")

# Replace any generic onrender URLs with https://aushadhasahaya-api.onrender.com
content = content.replace("https://aushadhasahaya.onrender.com", "https://aushadhasahaya-api.onrender.com")

build_py.write_text(content, encoding="utf-8")
print("Updated build_book.py with live Render URL.")
