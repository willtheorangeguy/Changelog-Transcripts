import os
import sys
import json
import subprocess
import re
from datetime import datetime
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TDRC, TRCK

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
    "afk": "Away from Keyboard",
    "news": "Changelog News",
    "interviews": "Changelog Interviews",
    "friends": "Changelog and Friends"
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
    "afk": "https://changelog.com/afk/feed",
    "news": "https://changelog.com/news/feed",
    "interviews": "https://changelog.com/interviews/feed",
    "friends": "https://changelog.com/friends/feed"
}

# Log file name
LOG_FILENAME = "tagged.log"

def backstage():
    """Special handling for Backstage podcast, which does not have a feed."""
    root_path = "Backstage"
    podcast_name = "Backstage"

    if not os.path.isdir(root_path):
        print(f"Podcast folder not found: {root_path}")
        return

    for root, _, files in os.walk(root_path):
        mp3_files = sorted(file for file in files if file.lower().endswith(".mp3"))
        if not mp3_files:
            continue

        folder_name = os.path.basename(root)
        year_match = re.search(r"\b(19|20)\d{2}\b", folder_name)
        album_year = year_match.group(0) if year_match else folder_name

        log_path = os.path.join(root, LOG_FILENAME)
        tagged_files = set()
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as log_file:
                for line in log_file:
                    tagged_files.add(line.strip())

        print(f"Processing Backstage folder: {root}")
        with open(log_path, "a", encoding="utf-8") as log_file:
            for filename in mp3_files:
                if filename in tagged_files:
                    print(f"Skipping (already tagged): {filename}")
                    continue

                filepath = os.path.join(root, filename)
                try:
                    audio = EasyID3(filepath)
                    audio["artist"] = podcast_name
                    audio["albumartist"] = podcast_name
                    audio["album"] = album_year
                    audio["title"] = os.path.splitext(filename)[0]
                    audio.save(filepath)

                    id3 = ID3(filepath)
                    id3.delall("TRCK")
                    id3.delall("TDRC")
                    id3.add(TDRC(encoding=3, text=f"{album_year}-01-01"))
                    id3.save(filepath)

                    log_file.write(filename + "\n")
                    log_file.flush()
                    tagged_files.add(filename)
                    print(f"Updated: {filename}")
                except Exception as e:
                    print(f"Error with {filepath}: {e}")

def all():
    """Run the tagger for all podcasts."""
    for podcast_key in PODCAST_FOLDERS.keys():
        print(f"Running tagger for podcast: {podcast_key}")
        playlist_url = XML_FEED_URLS.get(podcast_key)
        output_path = PODCAST_FOLDERS.get(podcast_key)
        if playlist_url and output_path:
            title_map = fetch_playlist_data(playlist_url)
            process_podcast_folder(output_path, output_path, title_map)
        else:
            print(f"Skipping {podcast_key}: Missing feed URL or folder mapping.")

def normalize(text):
    """Normalize strings for reliable matching."""
    text = text.lower()
    text = re.sub(r"\.mp3$", "", text) # remove .mp3 extension
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip() # collapse whitespace
    return text

def fetch_playlist_data(url):
    """Fetch all playlist entries in one go (fast)."""
    cmd = [
        "yt-dlp",
        "--dump-single-json",
        url
    ]
    # Process resulting JSON
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)

    # Map normalized title to upload date
    title_map = {}

    # Loop through entries and build the map
    for entry in data.get("entries", []):
        title = entry.get("title")
        upload_date = entry.get("upload_date")
        if title and upload_date:
            dt = datetime.strptime(upload_date, "%Y%m%d")
            title_map[normalize(title)] = dt

    return title_map

def process_year_folder(folder_path, year, podcast_name, title_map):
    """Process all MP3 files in the given folder, 
    matching them to playlist data and updating ID3 tags."""
    files_with_dates = []

    # Path to the log file
    log_path = os.path.join(folder_path, LOG_FILENAME)

    # Read already tagged files from log
    tagged_files = set()
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as log_file:
            for line in log_file:
                tagged_files.add(line.strip())

    # Gather all MP3 files and corresponding upload dates
    for file in os.listdir(folder_path):
        if not file.lower().endswith(".mp3"):
            continue
        # Normalize filename for matching
        norm_name = normalize(file)
        # Check for matching title in playlist data
        if norm_name not in title_map:
            print(f"Skipping (no match): {file}")
            continue
        # Store full path and upload date for sorting
        full_path = os.path.join(folder_path, file)
        files_with_dates.append((full_path, title_map[norm_name]))

    # Sort by upload date
    files_with_dates.sort(key=lambda x: x[1])

    # Update ID3 tags in sorted order
    with open(log_path, "a", encoding="utf-8") as log_file:
        for idx, (filepath, date) in enumerate(files_with_dates, start=1):
            filename = os.path.basename(filepath)

            if filename in tagged_files:
                print(f"Skipping (already tagged): {filename}")
                continue

            try:
                audio = EasyID3(filepath)
                audio["artist"] = podcast_name
                audio["albumartist"] = podcast_name
                audio["album"] = year
                audio["title"] = os.path.splitext(filename)[0]
                audio["tracknumber"] = str(idx)
                audio.save(filepath)
                id3 = ID3(filepath)

                # Album date = Jan 1 of year
                id3.delall("TDRC")
                id3.add(TDRC(encoding=3, text=f"{year}-01-01"))

                # Track number
                id3.delall("TRCK")
                id3.add(TRCK(encoding=3, text=str(idx)))
                id3.save(filepath)

                log_file.write(filename + "\n")
                log_file.flush()
                tagged_files.add(filename)

                print(f"Updated: {filename} → Track {idx}")
            except Exception as e:
                print(f"Error with {filepath}: {e}")

def process_podcast_folder(output_path, podcast_name, title_map):
    """Recursively process MP3 files in all subfolders under a podcast folder."""
    if not os.path.isdir(output_path):
        print(f"Podcast folder not found: {output_path}")
        return

    for root, _, files in os.walk(output_path):
        # Only process folders that actually contain MP3 files.
        if not any(file.lower().endswith(".mp3") for file in files):
            continue

        folder_name = os.path.basename(root)
        year_match = re.search(r"\b(19|20)\d{2}\b", folder_name)
        album_year = year_match.group(0) if year_match else folder_name

        print(f"Processing folder: {root}")
        process_year_folder(root, album_year, podcast_name, title_map)

if __name__ == "__main__":
    if sys.argv[1] == "practicalai":
        playlist_url = "https://feeds.transistor.fm/practical-ai-machine-learning-data-science-llm"
        output_path = "Practical AI"
    elif sys.argv[1] == "jsparty":
        playlist_url = "https://changelog.com/jsparty/feed"
        output_path = "JS Party"
    elif sys.argv[1] == "shipit":
        playlist_url = "https://changelog.com/shipit/feed"
        output_path = "Ship It"
    elif sys.argv[1] == "founderstalk":
        playlist_url = "https://changelog.com/founderstalk/feed"
        output_path = "Founders Talk"
    elif sys.argv[1] == "gotime":
        playlist_url = "https://changelog.com/gotime/feed"
        output_path = "Go Time"
    elif sys.argv[1] == "rfc":
        playlist_url = "https://changelog.com/rfc/feed"
        output_path = "Request for Commits"
    elif sys.argv[1] == "brainscience":
        playlist_url = "https://changelog.com/brainscience/feed"
        output_path = "Brain Science"
    elif sys.argv[1] == "spotlight":
        playlist_url = "https://changelog.com/spotlight/feed"
        output_path = "Spotlight"
    elif sys.argv[1] == "afk":
        playlist_url = "https://changelog.com/afk/feed"
        output_path = "Away from Keyboard"
    elif sys.argv[1] == "news":
        playlist_url = "https://changelog.com/news/feed"
        output_path = "Changelog News"
    elif sys.argv[1] == "podcast":
        playlist_url = "https://changelog.com/podcast/feed"
        output_path = "Changelog Podcast"
    elif sys.argv[1] == "interviews":
        playlist_url = "https://changelog.com/interviews/feed"
        output_path = "Changelog Interviews"
    elif sys.argv[1] == "friends":
        playlist_url = "https://changelog.com/friends/feed"
        output_path = "Changelog and Friends"
    elif sys.argv[1] == "backstage":
        backstage()
        sys.exit(0)
    elif sys.argv[1] == "all":
        all()
        sys.exit(0)
    else:
        print("Usage: python 2_tagger.py <podcast>")
        sys.exit(1)

    print("Fetching playlist metadata...")
    title_map = fetch_playlist_data(playlist_url)
    print(f"Processing podcast path recursively: {output_path}")
    process_podcast_folder(output_path, output_path, title_map)
