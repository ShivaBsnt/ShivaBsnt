import requests
import re

CREDLY_USER = "shivabahadurbasnet"
README_FILE = "README.md"

BADGE_SECTION_START = "<!--START_SECTION:badges-->"
BADGE_SECTION_END = "<!--END_SECTION:badges-->"

def fetch_credly_badges():
    url = f"https://www.credly.com/users/{CREDLY_USER}/badges.json"
    response = requests.get(url, verify=False)
    response.raise_for_status()
    return response.json()["data"]

def generate_badge_markdown(badges):
    badges_md = ""
    for badge in badges:
        name = badge["badge_template"]["name"]
        img_url = badge["badge_template"]["image_url"]
        badge_id = badge["id"]  # use this to construct URL
        badge_url = f"https://www.credly.com/badges/{badge_id}"  # link to credential page
        badges_md += f'<a href="{badge_url}" target="_blank"><img src="{img_url}" alt="{name}" width="80" height="80" /></a> '
    return badges_md


def update_readme(content):
    with open(README_FILE, "r") as f:
        readme = f.read()

    pattern = re.compile(
        f"{BADGE_SECTION_START}[\\s\\S]*?{BADGE_SECTION_END}"
    )

    replacement = f"{BADGE_SECTION_START}\n{content}\n{BADGE_SECTION_END}"

    new_readme = pattern.sub(replacement, readme)

    with open(README_FILE, "w") as f:
        f.write(new_readme)

if __name__ == "__main__":
    badges = fetch_credly_badges()
    markdown = generate_badge_markdown(badges)
    update_readme(markdown)
