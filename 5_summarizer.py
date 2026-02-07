"""
This script summarizes a transcript file by splitting it into manageable chunks,
summarizing each chunk using the Ollama API, and then combining the summaries into a final summary.
"""

import os
import sys
import ollama
from transformers import AutoTokenizer

# Log file name
LOG_FILENAME = "summarized.log"

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

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def split_text_by_tokens(text, max_tokens=2000):
    """Splits the input text into chunks that do not exceed the specified token limit."""
    words = text.split()
    chunks = []
    current_chunk = []

    # Split the text into words and process them
    for word in words:
        current_chunk.append(word)
        tokens = tokenizer(" ".join(current_chunk))["input_ids"]
        if len(tokens) > max_tokens:
            current_chunk.pop()
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_chunk(text, model="llama3.1:8b"):
    """Summarizes a chunk of text using the specified Ollama model."""
    # Ollama prompt
    prompt = (
        "You are an expert summarizer. Summarize the following transcript into a short list "
        "of the main topics discussed or mentioned. Use only bullet points. "
        "Do not include any pleasantries to the user, or any sort of heading.\n\n"
        f"{text}"
    )

    # Ollama response handler
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You summarize transcripts into concise topic overviews."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']

def summarize_transcript(full_path, model):
    """Summarizes a single transcript file by splitting 
    it into chunks and summarizing each chunk."""
    with open(full_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    # Split transcript into chunks
    print("Splitting transcript into chunks...")
    chunks = split_text_by_tokens(transcript)

    print(f"{len(chunks)} chunks created. Summarizing each...")

    # Summarize each chunk
    partial_summaries = []
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1}/{len(chunks)}...")
        summary = summarize_chunk(chunk, model)
        partial_summaries.append(summary)

    print("Generating final summary from chunk summaries...")

    # Combine partial summaries
    combined_summary = "\n".join(partial_summaries)

    # Save result
    base_name = os.path.splitext(full_path)[0]
    base_name = base_name.replace("_transcript", "")
    summary_path_txt = f"{base_name}_summary.txt"
    with open(summary_path_txt, "w", encoding="utf-8") as f:
        f.write(combined_summary)
    summary_path_md = f"{base_name}_summary.md"
    with open(summary_path_md, "w", encoding="utf-8") as f:
        f.write(combined_summary)

    print(f"Summary saved to: {summary_path_txt} and {summary_path_md}")

def summarize_transcripts(file_path, model="llama3.1:8b"):
    """Loops through all year folders and .txt files in the specified directory,
    skipping already processed files and summary files."""

    # Use the folder path directly (already looked up in main)
    podcast_folder = file_path

    # Check if podcast folder exists
    if not os.path.exists(podcast_folder):
        print(f"Error: Podcast folder '{podcast_folder}' does not exist.")
        return

    # Loop through all subdirectories (year folders) in the podcast folder
    for year_folder in os.listdir(podcast_folder):
        year_path = os.path.join(podcast_folder, year_folder)
        
        # Skip if not a directory
        if not os.path.isdir(year_path):
            continue
        
        print(f"Processing year folder: {year_folder}")
        
        # Create a log file to track processed files for this year
        log_path = os.path.join(year_path, LOG_FILENAME)
        processed_files = set()

        # Load already processed files from log
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as log_file:
                processed_files = set(line.strip() for line in log_file if line.strip())

        # Loop through all .txt files in the year directory
        for file in os.listdir(year_path):
            full_path = os.path.join(year_path, file)
            # Skip summary files and already processed files
            if file.endswith(".txt") and not file.endswith("_summary.txt") and not file.endswith("corrected.txt") and not file.endswith("_notes.txt") and not file.endswith("_summary.md") and not file.endswith("corrected.md") and not file.endswith("_notes.md") and file not in processed_files:
                print(f"Processing {file}...")
                summarize_transcript(full_path, model)
                with open(log_path, "a", encoding="utf-8") as log_file:
                    log_file.write(file + "\n")
                    log_file.flush()
            elif file in processed_files:
                print(f"Skipping (already summarized): {file}")
            
# When script is run, summarize all transcripts in the current directory
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 5_summarizer.py <podcast>")
        sys.exit(1)
    podcast_key = sys.argv[1]
    folder_path = PODCAST_FOLDERS.get(podcast_key)
    if folder_path is None:
        print(f"Error: Unknown podcast key '{podcast_key}'.")
        print(f"Valid options: {', '.join(PODCAST_FOLDERS.keys())}")
        sys.exit(1)
    summarize_transcripts(folder_path)
