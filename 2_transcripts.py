"""
This script downloads transcripts from the thechangelog/transcripts GitHub repository
and saves them locally with proper naming based on the XML feed data.
"""

import sys
import os
import xml.etree.ElementTree as ET
import re
import requests
import whisper

# Log file name
LOG_FILENAME = "transcripts.log"

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
    "practicalai": "https://changelog.com/practicalai/feed",
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

# Check for PyTorch
import torch
print("Is CUDA enabled? " + str(torch.cuda.is_available()))
print("Current CUDA GPU: " + str(torch.cuda.get_device_name(0)))

def transcribe(file_path):
    """Transcribes a single audio file using Whisper and saves the output with timestamps.
    Returns True if successful."""
    try:
        print("Loading model...")
        model = whisper.load_model("turbo")

        print(f"Transcribing: {file_path}")
        result = model.transcribe(file_path, language="en", verbose=True)

        # Create output file name
        base_name = re.sub(r"\s*\[.*?\]", "", os.path.splitext(file_path)[0])
        output_path = f"{base_name}_transcript"

        # Save timestamped + punctuated transcription as .txt
        with open(output_path + ".txt", "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{start:.2f} --> {end:.2f}] {text}\n")

        # Save timestamped + punctuated transcription as .md
        with open(output_path + ".md", "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                f.write(f"[{start:.2f} --> {end:.2f}] {text}\n")

        # User feedback
        print(f"Transcription saved to: {output_path}.txt and {output_path}.md")
        return True
    # Catch any exceptions and report failure
    except Exception as e:
        print(f"Failed to transcribe {file_path}: {e}")
        return False

def sanitize_filename(filename):
    """
    Remove or replace characters that are invalid in Windows filenames.
    """
    # Replace invalid characters with underscores
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')

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
    # Check if log file exists, if not create it and write first entry
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

def parse_xml_feed(xml_content):
    """
    Parse the XML feed content and extract episode information.
    Returns a list of dictionaries with title, episode_id, and year.
    """
    # Parse the XML content
    root = ET.fromstring(xml_content)
    # Extract episode information
    episodes = []
    
    # Iterate through all <item> elements
    for item in root.findall('.//item'):
        title_elem = item.find('title')
        link_elem = item.find('link')
        pub_date_elem = item.find('pubDate')
        
        if title_elem is not None and link_elem is not None:
            title = title_elem.text
            link = link_elem.text
            
            # Extract episode ID from link
            episode_id = link.rstrip('/').split('/')[-1]
            
            # Extract year from pubDate if available
            year = None
            if pub_date_elem is not None:
                pub_date = pub_date_elem.text
                # Parse year from date string
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

def download_transcript(github_folder, filename_prefix, episode_id):
    """
    Download the transcript from GitHub.
    Returns the transcript content as a string, or None if not found.
    """
    # Construct the GitHub raw URL
    transcript_filename = f"{filename_prefix}-{episode_id}.md"
    github_url = f"https://raw.githubusercontent.com/thechangelog/transcripts/refs/heads/master/{github_folder}/{transcript_filename}"

    print(f"Attempting to download: {github_url}")

    # Download the transcript content
    try:
        response = requests.get(github_url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Transcript not found (HTTP {response.status_code})")
            return None
    except Exception as e:
        print(f"Error downloading transcript: {e}")
        return None

def save_transcript(content, local_folder, year, title):
    """
    Save the transcript to the local folder with proper naming.
    Replaces any existing Whisper-generated transcript if found.
    """
    # Sanitize the title for use as a filename
    safe_title = sanitize_filename(title)
    transcript_filename = f"{safe_title}_transcript.md"
    
    # Construct the full path
    if year:
        folder_path = os.path.join(local_folder, year)
    else:
        folder_path = local_folder
    
    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, transcript_filename)
    
    # Check if transcript already exists (from previous Whisper generation)
    if os.path.exists(file_path):
        print("Replacing existing transcript...")
        # Delete both .md and .txt versions
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            txt_path = file_path.replace('.md', '.txt')
            if os.path.exists(txt_path):
                os.remove(txt_path)
        except Exception as e:
            print(f"Warning: Could not delete old transcript: {e}")
    
    # Write the transcript as a .md and .txt file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(file_path.replace('.md', '.txt'), 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Saved to: {file_path} and {file_path.replace('.md', '.txt')}")
    return file_path

def find_audio_file(local_folder, year, title):
    """
    Find the audio file for a given episode.
    Returns the path to the audio file if found, None otherwise.
    """
    # Sanitize the title for use as a filename
    safe_title = sanitize_filename(title)
    
    # Construct the folder path
    if year:
        folder_path = os.path.join(local_folder, year)
    else:
        folder_path = local_folder
    
    # Check if folder exists
    if not os.path.exists(folder_path):
        return None
    
    # Look for audio files with the title in the name
    # Common patterns: title.mp3, title [something].mp3
    for file in os.listdir(folder_path):
        if file.endswith('.mp3'):
            # Check if the sanitized title is in the filename
            file_without_ext = os.path.splitext(file)[0]
            # Remove any bracketed content for comparison
            file_base = re.sub(r'\s*\[.*?\]', '', file_without_ext)
            if safe_title in file or file_base == safe_title:
                return os.path.join(folder_path, file)
    
    return None

def generate_transcript_with_whisper(audio_file_path, local_folder, year, title):
    """
    Generate a transcript using Whisper for the given audio file.
    Returns True if successful, False otherwise.
    """
    print("Transcript not found on GitHub, generating with Whisper...")
    
    # Use the existing transcribe function
    success = transcribe(audio_file_path)
    
    if success:
        print("Whisper transcription completed successfully")
        return True
    else:
        print("Whisper transcription failed")
        return False

def process_podcast(podcast_key):
    """
    Process all episodes of a podcast: download and save transcripts.
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
    
    # Process each episode
    success_count = 0
    not_found_count = 0
    skipped_count = 0
    updated_count = 0
    
    for episode in episodes:
        episode_id = episode['episode_id']
        
        # Check if already downloaded
        if episode_id in downloaded_episodes:
            # Check if a GitHub transcript is now available (to replace Whisper-generated one)
            transcript_content = download_transcript(github_folder, filename_prefix, episode_id)
            
            if transcript_content:
                print(f"Updating Episode {episode_id}: {episode['title']} (GitHub transcript now available)")
                # Save the transcript (will replace existing Whisper transcript)
                save_transcript(transcript_content, local_folder, episode['year'], episode['title'])
                updated_count += 1
            else:
                print(f"Skipping Episode {episode_id}: {episode['title']} (already downloaded)")
                skipped_count += 1
            continue
        
        print(f"\nProcessing Episode {episode_id}: {episode['title']}")
        
        # Download the transcript
        transcript_content = download_transcript(github_folder, filename_prefix, episode_id)
        
        if transcript_content:
            # Save the transcript
            save_transcript(transcript_content, local_folder, episode['year'], episode['title'])
            # Add to log
            append_to_download_log(log_path, episode_id, episode['title'])
            success_count += 1
        else:
            # Transcript not found on GitHub, try to generate with Whisper
            audio_file_path = find_audio_file(local_folder, episode['year'], episode['title'])
            
            if audio_file_path:
                print(f"Found audio file: {audio_file_path}")
                whisper_success = generate_transcript_with_whisper(
                    audio_file_path, local_folder, episode['year'], episode['title']
                )
                
                if whisper_success:
                    # Add to log
                    append_to_download_log(log_path, episode_id, episode['title'])
                    success_count += 1
                else:
                    not_found_count += 1
            else:
                print("No audio file found to transcribe")
                not_found_count += 1
    
    print(f"Processing show {local_folder} complete!")
    print(f"Successfully downloaded: {success_count}")
    print(f"Updated (replaced Whisper with GitHub): {updated_count}")
    print(f"Skipped (already downloaded): {skipped_count}")
    print(f"Not found: {not_found_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2_transcripts.py <podcast>")
    podcast_key = sys.argv[1]
    process_podcast(podcast_key)
