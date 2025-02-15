import requests
from bs4 import BeautifulSoup
import re
import time

# Function to perform a Google search using the "google" module (You can replace this with Custom Search API if preferred)
def google_search(query, num_results=10):
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(search_url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if "url?q=" in href:
            links.append(href.split("url?q=")[1].split("&")[0])
    
    return links

# Function to scrape emails from a given URL
def scrape_emails(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return []
        
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Regex pattern to match emails ending with @match.com or @mtch.com
        email_pattern = r'[a-zA-Z0-9._%+-]+@(match\.com|mtch\.com)'
        
        # Find all matching emails
        emails = re.findall(email_pattern, soup.text)
        
        return emails
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

# Main function
def main():
    query = 'site:match.com email'
    search_results = google_search(query, num_results=5)
    
    all_emails = set()  # Using a set to avoid duplicate emails
    
    for url in search_results:
        emails = scrape_emails(url)
        all_emails.update(emails)
        time.sleep(2)  # Be respectful to servers by adding a delay
    
    if all_emails:
        print("Found emails:")
        for email in all_emails:
            print(email)
    else:
        print("No emails found.")

if __name__ == '__main__':
    main()
