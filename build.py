"""Build index.html for GitHub Pages from page.html.

page.html holds the page body (it is also what gets previewed as a Claude artifact).
This wraps it in a full HTML document with the meta tags a public site needs.

Run:  python build.py
"""
from pathlib import Path

HERE = Path(__file__).parent
SITE_URL = "https://athrvaraut.github.io/"  # change if you use a custom domain
DESCRIPTION = (
    "Athrva Raut: B.Tech AI & ML student and sole developer of PackersMart. "
    "Case studies in backend engineering, plant-operations software and machine learning."
)
FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='12' fill='%230e6b55'/%3E"
    "%3Ctext x='32' y='42' font-family='Arial,sans-serif' font-size='28' font-weight='700' "
    "text-anchor='middle' fill='%23ffffff'%3EAR%3C/text%3E%3C/svg%3E"
)

body = (HERE / "page.html").read_text(encoding="utf-8")

head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{DESCRIPTION}">
<meta name="author" content="Athrva Raut">
<meta property="og:type" content="website">
<meta property="og:title" content="Athrva Raut">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:url" content="{SITE_URL}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{FAVICON}">
<style>html{{color-scheme:light dark}} body{{margin:0}} img{{max-width:100%}} [hidden]{{display:none!important}}</style>
"""

# page.html starts with <title>, fonts and <style>; they belong in <head>.
split_at = body.index("</style>") + len("</style>")
page_head, page_body = body[:split_at], body[split_at:]

html = head + page_head + "\n</head>\n<body>\n" + page_body.strip() + "\n</body>\n</html>\n"
(HERE / "index.html").write_text(html, encoding="utf-8")
print("Wrote index.html")
