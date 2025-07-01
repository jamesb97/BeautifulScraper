#!/usr/bin/env python3
"""
Web scraper script that fetches content from a website and prints it to console.
"""

import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin, urlparse

def scrape_website(url):
    """
    Scrape content from a website and return the text content.
    
    Args:
        url (str): The URL to scrape
    
    Returns:
        str: The text content of the webpage
    """
    try:
        # Add headers to mimic a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make the HTTP request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up the text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except requests.RequestException as e:
        return f"Error fetching the webpage: {e}"
    except Exception as e:
        return f"Error parsing the webpage: {e}"

def main():
    """Main function to run the web scraper."""
    if len(sys.argv) != 2:
        print("Usage: python web_scraper.py <URL>")
        print("Example: python web_scraper.py https://example.com")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Basic URL validation
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        print("Error: Please provide a valid URL with http:// or https://")
        sys.exit(1)
    
    print(f"Scraping content from: {url}")
    print("-" * 50)
    
    content = scrape_website(url)
    print(content)

if __name__ == "__main__":
    main()