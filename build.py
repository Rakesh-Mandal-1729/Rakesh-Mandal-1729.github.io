"""Build the GitHub Pages site from page.html.

page.html is the editable source (also used for the private preview). This script
wraps it into a complete index.html and copies the public CV next to it.
Run from anywhere:  python3 07_Website/build.py
"""
import pathlib
import shutil

here = pathlib.Path(__file__).resolve().parent
page = (here / "page.html").read_text(encoding="utf-8")
head, body = page.split("<!-- /head -->", 1)

index = (
    "<!doctype html>\n"
    '<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + head.strip()
    + "\n</head>\n<body>\n"
    + body.strip()
    + "\n</body>\n</html>\n"
)
(here / "index.html").write_text(index, encoding="utf-8")
print("wrote index.html")

cv = here.parent / "06_Scholarships" / "00_General" / "CV_Public.pdf"
if cv.exists():
    shutil.copyfile(cv, here / "cv.pdf")
    print("copied cv.pdf from", cv)
else:
    print("CV_Public.pdf not found; run 06_Scholarships/build_all.sh first")
