# -*- coding: utf-8 -*-
"""crawler_script.py

This script uses the crawl4ai library to crawl a website and save the output to a markdown file.
"""
from crawl4ai import WebCrawler
import datetime
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting the crawler script")

        # Create an instance of WebCrawler
        logging.debug("Creating WebCrawler instance")
        crawler = WebCrawler()

        # Warm up the crawler (load necessary models)
        logging.info("Warming up the crawler")
        crawler.warmup()

        # Run the crawler on a URL
        url = "https://www.eu-startups.com/directory/"
        logging.info(f"Running the crawler on URL: {url}")
        result = crawler.run(url=url)

        # Check if result is None or empty
        if result is None or not result.markdown:
            logging.warning("Crawler returned empty or None result")
            return

        # Get current date
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Create filename
        filename = f"Salida{current_date}.md"

        # Save the extracted content to a file
        logging.info(f"Saving content to file: {filename}")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(result.markdown)

        logging.info(f"Content saved to {filename}")
        
        # Print the first 100 characters of the content for verification
        print(f"First 100 characters of content: {result.markdown[:100]}")

    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()