"""
This script downloads show notes from the thechangelog/notes GitHub repository
and saves them locally with proper naming based on the XML feed data.
"""

import sys
import os
import xml.etree.ElementTree as ET
import re
import requests

# Log file name
LOG_FILENAME = "notes.log"

# Mapping of command-line arguments to local folder names
PODCAST_FOLDERS = {
    "practicalai": "Practical AI",
    "jsparty": "JS Party",
    "shipit": "Ship It",
    "founderstalk": "Founders Talk",
    "gotime": "Go Time",
    "rfc": "Request for Commits",
    "brainscience": "Brain Science",
    "spotlight": "Spotlight",
    "backstage": "Backstage",
    "afk": "Away from Keyboard",
    "news": "Changelog News",
    "podcast": "Changelog Interviews",
    "interviews": "Changelog Interviews",
    "friends": "Changelog and Friends"
}

# Mapping of command-line arguments to GitHub transcript folder names
GITHUB_FOLDERS = {
    "practicalai": "practicalai",
    "jsparty": "jsparty",
    "shipit": "shipit",
    "founderstalk": "founderstalk",
    "gotime": "gotime",
    "rfc": "rfc",
    "brainscience": "brainscience",
    "spotlight": "spotlight",
    "backstage": "backstage",
    "afk": "afk",
    "news": "news",
    "podcast": "podcast",
    "interviews": "podcast",
    "friends": "friends"
}

# Mapping of command-line arguments to GitHub transcript filename prefixes
GITHUB_FILENAME_PREFIXES = {
    "practicalai": "practical-ai",
    "jsparty": "js-party",
    "shipit": "ship-it",
    "founderstalk": "founders-talk",
    "gotime": "go-time",
    "rfc": "request-for-commits",
    "brainscience": "brain-science",
    "spotlight": "spotlight",
    "backstage": "backstage",
    "afk": "away-from-keyboard",
    "news": "changelog-news",
    "podcast": "the-changelog",
    "interviews": "the-changelog",
    "friends": "changelog--friends"
}

# Mapping of command-line arguments to XML feed URLs
XML_FEED_URLS = {
    "practicalai": "https://feeds.transistor.fm/practical-ai-machine-learning-data-science-llm",
    "jsparty": "https://changelog.com/jsparty/feed",
    "shipit": "https://changelog.com/shipit/feed",
    "founderstalk": "https://changelog.com/founderstalk/feed",
    "gotime": "https://changelog.com/gotime/feed",
    "rfc": "https://changelog.com/rfc/feed",
    "brainscience": "https://changelog.com/brainscience/feed",
    "spotlight": "https://changelog.com/spotlight/feed",
    "backstage": None,  # Backstage doesn't have a feed
    "afk": "https://changelog.com/afk/feed",
    "news": "https://changelog.com/news/feed",
    "podcast": "https://changelog.com/podcast/feed",
    "interviews": "https://changelog.com/podcast/feed",
    "friends": "https://changelog.com/friends/feed"
}

def sanitize_filename(filename):
    """
    Remove or replace characters that are invalid in Windows filenames.
    """
    # Replace invalid characters with nothing (remove them)
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')

    # Remove trailing dots and spaces (Windows doesn't allow these)
    filename = filename.rstrip('. ')
    return filename

def load_download_log(log_path):
    """
    Load the log file containing previously downloaded episode IDs.
    Returns a set of episode IDs.
    """
    # If the log file doesn't exist, return an empty set
    if not os.path.exists(log_path):
        return set()

    # Read the log file and extract episode IDs
    downloaded_episodes = set()
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Parse the episode ID from the log line
                    # Format: episode_id|title
                    parts = line.split('|')
                    if parts:
                        downloaded_episodes.add(parts[0])
    except Exception as e:
        print(f"Warning: Could not read log file: {e}")
    
    return downloaded_episodes

def append_to_download_log(log_path, episode_id, title):
    """
    Append an episode to the download log.
    """
    # Write the episode ID and title to the log file
    try:
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(f"{episode_id}|{title}\n")
    except Exception as e:
        print(f"Warning: Could not write to log file: {e}")

def download_xml_feed(feed_url):
    """
    Download the XML feed from the given URL.
    Returns the XML content as a string, or None if download fails.
    """
    # Check if feed URL is provided
    print(f"Downloading XML feed from: {feed_url}")
    try:
        response = requests.get(feed_url, timeout=30)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Failed to download XML feed (HTTP {response.status_code})")
            return None
    except Exception as e:
        print(f"Error downloading XML feed: {e}")
        return None

def assign_practicalai_episode_numbers(episodes):
    """
    Assign sequential episode numbers to Practical AI episodes.
    RSS feeds are newest-first, so we reverse to assign numbers from oldest to newest.
    Returns the episodes list with updated episode_id values.
    """
    # Reverse the list so oldest episodes come first
    reversed_episodes = list(reversed(episodes))
    
    # Assign sequential numbers starting from 1
    for i, episode in enumerate(reversed_episodes, start=1):
        episode['original_id'] = episode['episode_id']
        episode['episode_id'] = str(i)
    
    # Return in original order (newest first) for consistency
    return list(reversed(reversed_episodes))

def parse_xml_feed(xml_content):
    """
    Parse the XML feed content and extract episode information.
    Returns a list of dictionaries with title, episode_id, and year.
    """
    # Parse the XML content
    root = ET.fromstring(xml_content)
    # Extract episode information from the feed
    episodes = []

    # Iterate through all <item> elements
    for item in root.findall('.//item'):
        title_elem = item.find('title')
        link_elem = item.find('link')
        pub_date_elem = item.find('pubDate')

        if title_elem is not None and link_elem is not None:
            title = title_elem.text
            link = link_elem.text

            # Extract episode ID from link (e.g., https://changelog.com/afk/12 -> 12)
            episode_id = link.rstrip('/').split('/')[-1]

            # Extract year from pubDate if available
            year = None
            if pub_date_elem is not None:
                pub_date = pub_date_elem.text
                # Parse year from date string like "Fri, 24 Mar 2023 17:00:00 +0000"
                year_match = re.search(r'\b(\d{4})\b', pub_date)
                if year_match:
                    year = year_match.group(1)

            # Append episode info to the list
            episodes.append({
                'title': title,
                'episode_id': episode_id,
                'year': year
            })
    
    return episodes

def download_notes(github_folder, filename_prefix, episode_id):
    """
    Download the notes from GitHub.
    Returns the notes content as a string, or None if not found.
    """
    # Construct the GitHub raw URL
    notes_filename = f"{filename_prefix}-{episode_id}.md"
    github_url = f"https://raw.githubusercontent.com/thechangelog/show-notes/refs/heads/master/{github_folder}/{notes_filename}"

    print(f"Attempting to download: {github_url}")

    # Download the notes content
    try:
        response = requests.get(github_url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Notes not found (HTTP {response.status_code})")
            return None
    except Exception as e:
        print(f"Error downloading notes: {e}")
        return None

def save_notes(content, local_folder, year, title):
    """
    Save the notes to the local folder with proper naming.
    """
    # Sanitize the title for use as a filename
    safe_title = sanitize_filename(title)
    notes_filename = f"{safe_title}_notes.md"
    
    # Construct the full path
    if year:
        folder_path = os.path.join(local_folder, year)
    else:
        folder_path = local_folder
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, notes_filename)
    
    # Write the notes as a .md and .txt file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(file_path.replace('.md', '.txt'), 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved to: {file_path} and {file_path.replace('.md', '.txt')}")
    return file_path

def process_podcast(podcast_key):
    """
    Process all episodes of a podcast: download and save notes.
    """
    # Get mappings
    local_folder = PODCAST_FOLDERS.get(podcast_key)
    github_folder = GITHUB_FOLDERS.get(podcast_key)
    filename_prefix = GITHUB_FILENAME_PREFIXES.get(podcast_key)
    xml_feed_url = XML_FEED_URLS.get(podcast_key)

    # Validate mappings
    if not local_folder or not github_folder or not filename_prefix:
        print(f"Error: Unknown podcast key '{podcast_key}'")
        return

    # Backstage doesn't have an XML feed, so we skip the feed processing for it
    if not xml_feed_url:
        print(f"Error: No XML feed URL available for '{podcast_key}'")
        return
    
    print(f"Processing {local_folder} podcast...")
    
    # Set up the log file path
    log_path = os.path.join(local_folder, LOG_FILENAME)
    
    # Load previously downloaded episodes
    downloaded_episodes = load_download_log(log_path)
    print(f"Found {len(downloaded_episodes)} previously downloaded episodes in log")
    
    # Download the XML feed
    xml_content = download_xml_feed(xml_feed_url)
    if not xml_content:
        print("Error: Could not download XML feed")
        return
    
    # Parse the XML feed
    episodes = parse_xml_feed(xml_content)
    print(f"Found {len(episodes)} episodes in feed")
    
    # Special handling for Practical AI: use sequential episode numbers
    if podcast_key == "practicalai":
        print("Applying sequential episode numbering for Practical AI...")
        episodes = assign_practicalai_episode_numbers(episodes)
    
    # Process each episode
    success_count = 0
    not_found_count = 0
    skipped_count = 0
    
    for episode in episodes:
        episode_id = episode['episode_id']
        # Use original_id for log tracking if available (for Practical AI)
        log_id = episode.get('original_id', episode_id)
        
        # Check if already downloaded
        if log_id in downloaded_episodes:
            print(f"Skipping Episode {episode_id}: {episode['title']} (already downloaded)")
            skipped_count += 1
            continue
        
        print(f"Processing Episode {episode_id}: {episode['title']}")
        
        # Download the notes
        notes_content = download_notes(github_folder, filename_prefix, episode_id)
        
        if notes_content:
            # Save the notes
            save_notes(notes_content, local_folder, episode['year'], episode['title'])
            # Add to log (use original_id for tracking)
            append_to_download_log(log_path, log_id, episode['title'])
            success_count += 1
        else:
            not_found_count += 1
    
    print(f"Processing show {local_folder} complete!")
    print(f"Successfully downloaded: {success_count}")
    print(f"Skipped (already downloaded): {skipped_count}")
    print(f"Not found: {not_found_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 4_notes.py <podcast>")
    podcast_key = sys.argv[1]
    process_podcast(podcast_key)
