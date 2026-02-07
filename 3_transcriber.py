"""
This script transcribes audio files from Changelog podcast 
episodes that do not have one using OpenAI's Whisper model.
"""

import os
import sys
import re
import whisper

# Log file name
LOG_FILENAME = "transcribed.log"

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
    "podcast": "Changelog Interviews",
    "interviews": "Changelog Interviews",
    "friends": "Changelog and Friends"
}

# Check for PyTorch
import torch
print("Is CUDA enabled? " + str(torch.cuda.is_available()))
print("Current CUDA GPU: " + str(torch.cuda.get_device_name(0)))

# Windows-incompatible characters to remove from file names
INVALID_CHARS = '<>:"/\\|?*'

def transcribe_audio(folder_path):
    """Transcribes only .mp3 files in the specified directory and subdirectories using Whisper.
    Skips files that already have a transcript file (either .md or .txt)."""
    # Path to the log file in the podcast folder
    log_path = os.path.join(folder_path, LOG_FILENAME)

    # Read already transcribed files from log
    transcribed_files = set()
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as log_file:
            for line in log_file:
                transcribed_files.add(line.strip())

    # Open log file for appending
    with open(log_path, "a", encoding="utf-8") as log_file:
        # Loop through all subdirectories
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".mp3") and file not in transcribed_files:
                    full_path = os.path.join(root, file)
                    
                    # Check if transcript files already exist
                    dir_path = os.path.dirname(full_path)
                    file_name = os.path.basename(full_path)
                    base_name = re.sub(r"\s*\[.*?\]", "", os.path.splitext(file_name)[0])
                    # Remove Windows-incompatible characters
                    for char in INVALID_CHARS:
                        base_name = base_name.replace(char, "")
                    
                    transcript_txt = os.path.join(dir_path, f"{base_name}_transcript.txt")
                    transcript_md = os.path.join(dir_path, f"{base_name}_transcript.md")
                    
                    # Skip if either transcript file exists
                    if os.path.exists(transcript_txt) or os.path.exists(transcript_md):
                        print(f"Skipping {file} - transcript already exists")
                        continue
                    
                    success = transcribe(full_path)
                    if success:
                        log_file.write(file + "\n")
                        log_file.flush()

def transcribe(file_path):
    """Transcribes a single audio file using Whisper and saves the output with timestamps.
    Returns True if successful."""
    try:
        print("Loading model...")
        model = whisper.load_model("turbo")

        print(f"Transcribing: {file_path}")
        result = model.transcribe(file_path, language="en", verbose=True)

        # Get the directory and filename separately
        dir_path = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        
        # Create base name from just the filename
        base_name = re.sub(r"\s*\[.*?\]", "", os.path.splitext(file_name)[0])
        # Remove Windows-incompatible characters
        for char in INVALID_CHARS:
            base_name = base_name.replace(char, "")
        
        # Construct output path in the same directory as the source file
        output_path = os.path.join(dir_path, f"{base_name}_transcript")

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

# When script is run, transcribe all audio files in the current directory
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 3_transcriber.py <podcast>")
        sys.exit(1)
    podcast_key = sys.argv[1]
    folder_path = PODCAST_FOLDERS.get(podcast_key)
    transcribe_audio(folder_path)
