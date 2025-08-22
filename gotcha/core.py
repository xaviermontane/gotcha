import requests
from bs4 import BeautifulSoup
import time
from config import PLATFORMS, RATE_LIMIT_SECONDS

def main():
    return "Gotcha CLI - Social Media Spam Scanner"

def social_scan(username: str, platforms: str) -> dict:
    """Scans a username across multiple platforms."""
    requested = [p.strip() for p in platforms.split(',')]
    results = {"username": username, "platforms": {}}
     
    # Scan ALL requested platforms, whether they exist in PLATFORMS or not
    for platform_name in requested:
        if platform_name in PLATFORMS:
            url = PLATFORMS[platform_name]
            exists = username_scan(username, url)
            results["platforms"][platform_name] = {"exists": exists}
            time.sleep(RATE_LIMIT_SECONDS)
        else:
            # Platform not supported - mark as doesn't exist
            results["platforms"][platform_name] = {"exists": False}
     
    return results
def username_scan(username: str, platform_url: str) -> bool:
    """Checks if a username exists on a specific platform."""
    try:
        response = requests.get(platform_url.format(username), timeout=5)
        if response.status_code == 200:
            # Analyze content (example: look for a specific text)
            soup = BeautifulSoup(response.content, "html.parser")
            return "Profile Not Found" not in str(soup)
        elif response.status_code == 404:
            return False # Not found
        else:
            print(f"Error checking {platform_url}: {response.status_code}")
            return False # Treat as not found 
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e} for {platform_url}")
        return False  # Treat as not found

if __name__ == "__main__":
    main()