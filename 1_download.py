"""
This script uses yt-dlp to download audio, by year, from the
The Standup podcast website playlist.
"""

import sys
import yt_dlp

def download_playlist(playlist_url, output_path):
    """
    Downloads all audio from the podcast site.
    """
    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "download_archive": f"{output_path}/downloaded.log",
        "outtmpl": f"{output_path}/%(upload_date>%Y)s/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        'concurrent-fragments': True,
        'no-mtime': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    if sys.argv[1] == "practicalai":
        playlist_url = "https://changelog.com/practicalai/feed"
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
    elif sys.argv[1] == "backstage":
        playlist_url = [ # Backstage doesn't have a feed, so we hardcode the URLs here
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/1/backstage-1.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/2/backstage-2.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/3/backstage-3.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/4/backstage-4.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/5/backstage-5.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/6/backstage-6.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/7/backstage-7.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/8/backstage-8.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/9/backstage-9.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/10/backstage-10.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/11/backstage-11.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/12/backstage-12.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/13/backstage-13.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/14/backstage-14.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/15/backstage-15.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/16/backstage-16.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/17/backstage-17.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/18/backstage-18.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/19/backstage-19.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/20/backstage-20.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/21/backstage-21.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/22/backstage-22.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/23/backstage-23.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/24/backstage-24.mp3",
            "https://op3.dev/e/https://cdn.changelog.com/uploads/backstage/25/backstage-25.mp3",        
        ]
        output_path = "Backstage"
    elif sys.argv[1] == "afk":
        playlist_url = "https://changelog.com/afk/feed"
        output_path = "Away from Keyboard"
    elif sys.argv[1] == "news":
        playlist_url = "https://changelog.com/news/feed"
        output_path = "Changelog News"
    elif sys.argv[1] == "podcast":
        playlist_url = "https://changelog.com/interviews/feed"
        output_path = "Changelog Interviews"
    elif sys.argv[1] == "friends":
        playlist_url = "https://changelog.com/friends/feed"
        output_path = "Changelog and Friends"
    else:
        print("Usage: python 1_download.py <podcast>")
        sys.exit(1)

    download_playlist(playlist_url, output_path)
    print(f"Downloaded all audio from the {output_path} podcast feed.")
