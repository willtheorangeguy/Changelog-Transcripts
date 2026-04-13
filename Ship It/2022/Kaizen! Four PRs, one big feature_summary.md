• The hosts of Ship It discuss their previous episode where they announced a significant new development that was not yet ready to ship.
• Lars Wikman is a guest on the show for the first time in over 7 years and is interviewed about his background and projects.
• Gerhard Lazu mentions a connection between Lars and another person, but doesn't reveal further details, teasing that this person will be a future guest.
• The hosts discuss their previous experience with Kubernetes and how they have since switched to Nomad.
• Lars Wikman is introduced as a self-taught Elixir developer who runs a consultancy and has multiple projects, including blogging, YouTube, and podcasts.
• The speaker has a background in Go programming, but hasn't worked with it much lately.
• Lars Wikman mentions he's busy with Elixir and prefers working in smaller communities.
• Jerod Santo explains that their team has shipped chapters to various platforms since their last update.
• Chapters have been implemented on episode details pages, notification emails, RSS feeds, and mp3 ID3 tags.
• The team was able to remove FFmpeg from their container image after implementing ID3 VX with Lars' help.
• Lars discusses the challenges of working with ID3 VX, which requires following a specific binary format spec.
• Testing ID3 V2 spec and implementing chapter support for podcasts
• Using FFmpeg to parse chapter frames and identify issues with library code
• Difficulty testing with podcast players such as Overcast and Pocket Casts
• Identifying and resolving issues with specific podcasts, including Accidental Tech Podcast and Pocket Cast
• Library maintenance and future plans for ID3 V2.4 implementation
• McBull's contributions to the project while on the consultancy's bench
• Issues with development vs production environment and Elixir version mismatch
• Upgrading dependencies and software versions
• Fixing a TLS bug in the Erlang OTP Elixir version 24.3.4
• Troubleshooting HTTPS requests failing due to SSL module issues
• Implementing a workaround for failed HTTPS requests
• Considering staying behind the curve on Erlang updates to avoid unexpected issues
• Discussion of difficulties with the OpenSSL dependency
• The history and development process of adding chapters feature
• Reasons why it took a long time to implement the chapters feature
• Support for chapters feature in various podcast apps
• Production workflow changes and UI updates required for chapters feature
• Chapter support in podcast apps
• Difficulty in implementing chapter support due to lack of emphasis from podcast creators
• Comparison of various podcast apps' implementation of chapter support (Pocket Casts, Overcast, Castro)
• CircleCI and GitHub Actions integration issues for the show's CI/CD pipeline
• Discussion on redundancy and backup systems (e.g. having multiple CI tools)
• Discussing pull requests and GitHub Actions issues
• Adam Stacoviak mentions new sponsors/partners Fastly and Fly
• Jerod Santo updated the show's footer with the new sponsor information
• Gerhard Lazu discusses a Slack notification for successful deploys, and potential reasons for people leaving the channel
• Lars Wikman suggests that the dev channel is quiet and dominated by bots
• Team members discuss the importance of using the public dev channel for discussions and updates
• Improving GitHub integration for Changelog.com
• Discussing the usefulness of deployment/commit messages
• Introducing SSH commit verification and its benefits
• Debating the importance of commit signing for security and privacy
• Planning next Kaizen episode (episode 80) improvements, including migrating from LastPass to 1Password
• Plans to implement chapters in podcast app
• Update of mp3 files with chapter information to be automatic
• Background task to update mp3 files with new chapter information
• Integration of chapters into on-site player
• Clustering support for multiple instances of application
• Review and potential replacement of caching library (ConCache) with Cachex
• Recap of a previous episode's smallest Kaizen
• Discussion of the current episode being the biggest Kaizen ever
• General appreciation and acknowledgement from participants