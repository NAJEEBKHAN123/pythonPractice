# import sqlite3

# conn = sqlite3.connect("webScraper.db")

# cursor = conn.cursor()


# # cursor.execute("""
# # CREATE TABLE IF NOT EXISTS webScraper(
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name TEXT,
# #         description TEXT       
# #  )
# # """)

# # conn.commit()


# cursor.execute(
#     "INSERT INTO webScraper (id, name, description) VALUES (?, ?, ?)",
#     (1,"ali", "this is my last time", )
# )

# conn.commit()



# JOB TITLE SCRAPER FROM INDEED

import requests
from bs4 import BeautifulSoup

URL = "https://pk.indeed.com/jobs?q=python+developer&l=Pakistan"
HEADERS = {"User-Agent": "Mozilla/5.0"}
OUTPUT_FILE = "indeed_jobs.txt"

def scrape_indeed():
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code != 200:
            print("❌ Failed to fetch Indeed page")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # Indeed job titles are usually inside <h2> or <span> tags
        jobs = soup.find_all("h2")
        
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            for job in jobs:
                title = job.get_text(strip=True)
                if title:
                    file.write(title + "\n")

        print(f"✅ Scraped {len(jobs)} job titles and saved to {OUTPUT_FILE}")
    except ValueError:
        print("value error:")

# Run scraper
scrape_indeed()



