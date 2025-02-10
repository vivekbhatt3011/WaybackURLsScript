Description

This script retrieves archived URLs from the Wayback Machine for a specified domain. It extracts and saves the URLs into a timestamped text file, providing a useful way to analyze historical snapshots of a website.

Implementation

Uses the Wayback Machine's CDX API to fetch URLs.

Sends an HTTP request using requests.

Extracts URLs and saves them to a file.

Logs execution details and errors.

Handles user input via command-line arguments or interactive input.

Usage

Prerequisites

Python 3.x

requests library (install using pip install requests if needed)

Running the Script

To fetch URLs for a specific domain, run:

python script.py example.com

Alternatively, if no domain is provided as an argument, the script will prompt for input:

python script.py

Then enter the domain when prompted.

Output

Found URLs are saved in a file named {timestamp}-wayback_urls.txt.

Errors and logs are stored in {timestamp}-debug.log.

License

This script is open-source. Feel free to modify and distribute it.

