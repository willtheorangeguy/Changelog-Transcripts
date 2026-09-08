# The Changelog Transcripts — Pipeline

The archive is built by 7 scripts run in numeric order. `main.py` is a thin runner that calls each one in turn with the arguments you gave it, so running a stage by hand and letting `main.py` do it are equivalent.

| Stage | Script | What it does | Resume log |
|---|---|---|---|
| 1 | `1_download.py` | This script uses yt-dlp to download audio, by year, from the Changelog Universe podcast feeds. | — |
| 2 | `2_tagger.py` | Writes ID3 tags (title, date, track number) onto the downloaded audio using metadata pulled from the show's RSS feed. | `tagged.log` |
| 3 | `3_transcripts.py` | This script downloads transcripts from the thechangelog/transcripts GitHub repository and saves them locally with proper naming based on the XML feed data. | `transcripts.log` |
| 4 | `4_transcriber.py` | This script transcribes audio files from Changelog podcast episodes that do not have one using OpenAI's Whisper model. | `transcribed.log` |
| 5 | `5_notes.py` | This script downloads show notes from the thechangelog/notes GitHub repository and saves them locally with proper naming based on the XML feed data. | `notes.log` |
| 6 | `6_summarizer.py` | This script summarizes a transcript file by splitting it into manageable chunks, summarizing each chunk using the Ollama API, and then combining the summaries into a final summary. | `summarized.log` |
| 7 | `7_cleanup.py` | This script processes all .txt and .md files in the current directory, correcting their grammar and spelling using LanguageTool. | `cleaned.log` |

## Running a single stage

Every stage takes the same arguments as `main.py`, so any one of them can be re-run on its own without repeating the stages before it:

```bash
python 1_download.py <show> <year>
```

### Show arguments

The first argument selects a show. Valid values, read from the `PODCAST_FOLDERS` map the stages share:

```text
practicalai
jsparty
shipit
founderstalk
gotime
rfc
brainscience
spotlight
afk
news
interviews
friends
```

## Re-running and resume logs

The expensive stages append to a log file as they finish each item, and skip anything already listed there on a later run. That is what makes the pipeline resumable after an interruption.

| Log | Written by |
|---|---|
| `tagged.log` | `2_tagger.py` |
| `transcripts.log` | `3_transcripts.py` |
| `transcribed.log` | `4_transcriber.py` |
| `notes.log` | `5_notes.py` |
| `summarized.log` | `6_summarizer.py` |
| `cleaned.log` | `7_cleanup.py` |

Delete a log to force its stage to redo everything.

## A note on accuracy

Transcription and summarisation are both lossy. Neither the transcripts nor the summaries in this repository are an authoritative record — check the original recording where it matters. See [`CONTENT_LICENSE.md`](../CONTENT_LICENSE.md).
