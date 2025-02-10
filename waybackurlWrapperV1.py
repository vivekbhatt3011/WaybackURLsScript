import requests
import argparse
from datetime import datetime

def fetch_urls(domain):
    try:
        search_url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&collapse=urlkey"
        
        print("Fetching URLs from the Wayback Machine...\n")

        response = requests.get(search_url)
        response.raise_for_status()

        data = response.json()
        if len(data) <= 1:
            print("No URLs found for the given domain.")
        else:
            urls = [row[2] for row in data[1:]]
            print(f"Found {len(urls)} URLs.")

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            output_file = f"{timestamp}-wayback_urls.txt"
            with open(output_file, 'w') as file:
                for url in urls:
                    file.write(url + '\n')
            print(f"URLs have been saved to {output_file}.")

            log_file = f"{timestamp}-debug.log"
            with open(log_file, 'w') as log:
                log.write(f"Fetched URLs for domain: {domain}\n")
                log.write(f"Found {len(urls)} URLs\n")
                log.write(f"URLs saved to {output_file}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching URLs: {e}")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f"{timestamp}-debug.log", 'w') as log:
            log.write(f"Error: {e}\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f"{timestamp}-debug.log", 'w') as log:
            log.write(f"Unexpected error: {e}\n")

if __name__ == "__main__":
    try:
        # Check if the domain is provided as a command-line argument
        parser = argparse.ArgumentParser(description="Fetch archived URLs from the Wayback Machine.")
        parser.add_argument("domain", metavar="DOMAIN", type=str, nargs="?", help="The domain to fetch URLs for (e.g., example.com)")
        
        args = parser.parse_args()

        # If no domain is provided as a command-line argument, prompt the user for input
        if not args.domain:
            domain = input("Please enter the domain name (e.g., example.com): ").strip()
        else:
            domain = args.domain

        # Call the function to fetch URLs for the entered domain
        fetch_urls(domain)
    
    except Exception as e:
        print(f"An error occurred: {e}")

