"""
Main script to run a series of Python scripts in order.
This script takes the podcast and the year as an argument
and runs each script sequentially.
"""

import sys
import subprocess

# Scripts for Changelog Universe podcasts
scripts = [
    "1_download.py",
    "2_transcripts.py",
    "3_transcriber.py",
    "4_notes.py",
    "5_summarizer.py",
    "6_cleanup.py"
]

# Scripts for Practical AI podcast
practical_ai_scripts = [
    "1_download.py",
    "3_transcriber.py",
    "5_summarizer.py",
    "6_cleanup.py"
]

# List of Changelog Universe podcasts
pods = [
    "jsparty",
    "shipit",
    "founderstalk",
    "gotime",
    "rfc",
    "brainscience",
    "spotlight",
    "backstage",
    "afk",
    "news",
    "podcast",
    "friends"
]

def all():
    """Runs all scripts for all podcasts."""
    for podcast in pods:
        main(podcast, podcast)

def practical_ai():
    """Main function to run the scripts in order."""
    print(f"Running scripts for podcast: Practical AI")

    for script in practical_ai_scripts:
        print(f"Running {script} for podcast practicalai...")
        result = subprocess.run([sys.executable, script, "practicalai"], check=False)
        if result.returncode != 0:
            print(f"Error: {script} failed with exit code {result.returncode}")
            sys.exit(result.returncode)
    print("All scripts completed successfully.")

def main(output_path, podcast_key):
    """Main function to run the scripts in order."""
    print(f"Running scripts for podcast: {output_path}")

    for script in scripts:
        print(f"Running {script} for podcast {podcast_key}...")
        result = subprocess.run([sys.executable, script, podcast_key], check=False)
        if result.returncode != 0:
            print(f"Error: {script} failed with exit code {result.returncode}")
            sys.exit(result.returncode)
    print("All scripts completed successfully.")

if __name__ == "__main__":
    if sys.argv[1] == "practicalai":
        practical_ai()
    elif sys.argv[1] == "jsparty":
        podcast_key = "jsparty"
        output_path = "JS Party"
    elif sys.argv[1] == "shipit":
        podcast_key = "shipit"
        output_path = "Ship It"
    elif sys.argv[1] == "founderstalk":
        podcast_key = "founderstalk"
        output_path = "Founders Talk"
    elif sys.argv[1] == "gotime":
        podcast_key = "gotime"
        output_path = "Go Time"
    elif sys.argv[1] == "rfc":
        podcast_key = "rfc"
        output_path = "Request for Commits"
    elif sys.argv[1] == "brainscience":
        podcast_key = "brainscience"
        output_path = "Brain Science"
    elif sys.argv[1] == "spotlight":
        podcast_key = "spotlight"
        output_path = "Spotlight"
    elif sys.argv[1] == "backstage":
        podcast_key = "backstage"
        output_path = "Backstage"
    elif sys.argv[1] == "afk":
        podcast_key = "afk"
        output_path = "Away from Keyboard"
    elif sys.argv[1] == "news":
        podcast_key = "news"
        output_path = "Changelog News"
    elif sys.argv[1] == "podcast":
        podcast_key = "podcast"
        output_path = "Changelog Interviews"
    elif sys.argv[1] == "interviews":
        podcast_key = "podcast"
        output_path = "Changelog Interviews"
    elif sys.argv[1] == "friends":
        podcast_key = "friends"
        output_path = "Changelog and Friends"
    elif sys.argv[1] == "all":
        all()
        sys.exit(0)
    else:
        print("Usage: python main.py <podcast>")
        sys.exit(1)
    main(output_path, podcast_key)
