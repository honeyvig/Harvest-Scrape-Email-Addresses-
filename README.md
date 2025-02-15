# Harvest-Scrape-Email-Addresses-
I need you to locate all email addresses that end with:

@match.com
@mtch.com
-----
To accomplish this task, you can use Python with libraries like requests, BeautifulSoup, and re (regular expressions) to scrape web pages and find email addresses that match specific patterns (like @match.com or @mtch.com).

Below is an example code that combines Google search results with web scraping to find email addresses that match your criteria:
Requirements:

    requests: To make HTTP requests.
    BeautifulSoup: To parse HTML pages.
    re: For regular expression-based matching.

Step-by-Step Code

    Google Search: You will need a custom Google search tool or API since scraping Google results directly might violate Google’s terms of service. You can use the Google Custom Search API or scrape search results directly from Google (not recommended).

    Web Scraping: Once you get URLs from Google search results, you can scrape each page for email addresses using regular expressions.

Install Necessary Libraries:

pip install requests beautifulsoup4 google

Example Code to Scrape Emails:

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

How the Code Works:

    Google Search:
        The google_search() function sends a search query to Google, retrieves the search results, and extracts URLs from the result pages.
        The search query site:match.com email restricts the search to pages from match.com containing the word "email".

    Email Scraping:
        The scrape_emails() function visits each URL found by the Google search and parses the page’s content.
        It uses a regular expression (re.findall) to find email addresses ending with @match.com or @mtch.com.

    Main Execution:
        The script will perform the Google search, scrape emails from the resulting pages, and print any found email addresses.
        A delay (time.sleep(2)) is added between requests to avoid overloading the web servers and being flagged as a bot.

Notes:

    Google Scraping Limitation: Scraping Google search results directly (using this method) could result in your IP being blocked by Google due to scraping restrictions. It is recommended to use Google’s Custom Search API for more reliable and safe access to search results.

    Legal Compliance: Be sure to review and comply with the relevant laws and website terms of service (like GDPR, CCPA) regarding scraping and harvesting email addresses. Unauthorized scraping of personal data might violate regulations.

    Scraping Techniques: Scraping can be blocked by websites using anti-scraping measures (e.g., CAPTCHAs, blocking requests from non-browser clients), so make sure you're aware of any legal or technical restrictions before you proceed.

    Efficiency: Depending on the number of results you want to scrape, you might need to improve efficiency by handling retries, dealing with HTTP errors, or optimizing the number of requests.
