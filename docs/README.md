# The Changelog Transcripts — Documentation

This archive holds machine-generated transcripts and summaries for Changelog Podcast Universe podcast episodes, together with the pipeline that produces them. The pipeline runs as 7 numbered stages; `main.py` executes them in order.

```
Changelog-Transcripts/
├── docs/
│   ├── README.md      this page
│   ├── usage.md       installing, running, and the helper scripts
│   └── pipeline.md    what each numbered stage does
├── main.py            runs every stage in order
├── 1_download.py
├── 2_tagger.py
├── 3_transcripts.py
├── 4_transcriber.py
├── 5_notes.py
├── 6_summarizer.py
├── 7_cleanup.py
├── Away from Keyboard/
├── Backstage/
├── Brain Science/
├── Changelog Interviews/
├── Changelog News/
├── Changelog and Friends/
└── ... 7 more show directories
```

## Pages

- [Usage](./usage.md) — prerequisites, running the pipeline, and the PowerShell helpers
- [Pipeline](./pipeline.md) — what each stage does and what it writes

## Before reusing the transcripts

The code is MIT. The transcript text is not — see [`CONTENT_LICENSE.md`](../CONTENT_LICENSE.md).
