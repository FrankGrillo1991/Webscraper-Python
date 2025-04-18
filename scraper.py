import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://example.com"

# Send GET request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Example Extract all headings (h1)
headings = soup.find_all('h1')
for i, h in enumerate(headings, 1):
    print(f"H1-{i}: {h.get_text(strip=True)}")