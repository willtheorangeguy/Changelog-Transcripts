• Announcement of CPU.fm, a new podcast network and media machine
• Gerhard Lazu presents a slideshow on the Kaizen episodes
• Discussion on the font used in the slideshow (Inter)
• Adam Stacoviak shares a quote from Sir Isaac Newton about progress and change
• Announcement of the new format for CPU.fm, focusing on the Changelog Podcast Universe
• Discussion on the retirement of some shows and the spinoff of others
• Explanation of the reasoning behind the change, including the need to scale the team or compromise on production quality
• Introduction to CPU.fm as a new vision for the future of the podcast network and media machine
• Restructuring the Changelog podcast to focus on main shows and let others spin off independently
• Embracing change and being in control of one's own path
• The concept of "The Joy of Missing Out" (JOMO) and leaving room for new opportunities
• Expanding the Changelog's capacity to help brands reach developers through CPU (Centralized Podcast Universe)
• Launching a new index or hub for developer podcasts, with a single subscribe point for multiple shows
• Jerod Santo and Adam Stacoviak discuss their desire to focus on development and experiment with new ideas
• They mention that with the current production schedule, they didn't have time for experimentation or building new things
• The Changelog podcast will take some productions off its weekly calendar, giving them more time to develop and innovate
• Kaizen will be embedded into the Changelog podcast, with a focus on continuous improvement and iteration
• Gerhard Lazu, a friend and contributor, is excited about the changes and believes they will lead to something amazing
• Gerhard teases a "big announcement" and hints at new developments, including a potential new Mac and Just Contribute
• Discussing the M4 upgrade and whether it's worth it
• Macs and their specifications, with Jerod Santo's current MacBook Pro being maxed out
• The Just Contribute tool, which Gerhard Lazu was trying to promote
• Gerhard Lazu's home lab, which is a LattePanda Sigma that can run Kubernetes and serve 300 billion requests per month
• The Jellyfin media player and its ability to transcode video with Intel's video sync technology
• Gerhard Lazu's talk at Taloscon about taking his home lab into production and showing off his home theater setup
• kaizen and kaizen 17 project updates
• development of a CLI utility for infrastructure tasks
• creating a seamless experience for team members to replace Changelog dev with a prod dbdump
• enabling team members to run dev with a Neon DB branch and configure apps automatically
• discussing video series and podcast content related to infrastructure and development
• Discussion of developing against production as a branch, including syncing between branches
• Comparison of two commands for pulling data: one that downloads the entire database and another that syncs with a remote database
• Trade-offs between waiting for a longer initial load time versus slower load times with each use
• Switch from Slack to Zulip for team communication and its benefits (threaded conversations, topic-based organization)
• User experience with Zulip, including preferences for a non-threaded main channel and concerns about topic-based organization
• Threads and thread-per-episode functionality in Zulip
• Benefits of threaded discussions, including ease of use and ability to revisit conversations
• Mobile app issues and UI problems in Zulip
• Deeplinking and URL issues in Zulip
• Gradual transition from Slack to Zulip, including blue/green deployment
• Desire to close the Changelog Slack channel and switch to Zulip
• Wish for Slack to support communities better, including non-enterprise features
• Potential for Zulip to reach more users and compete with Slack
• Hidden potential in Zulip's features and team, but held back by certain beliefs or perceptions
• Zulip features "Kaizen, just do it" thread where Matt Johnson found solution to issue
• Markdown chapters feature in Zulip, allowing easy navigation of podcast episodes
• Discussion on linking chapters to start time and making them clickable
• Workflow challenges with video-first world and integration with YouTube
• Differences between YouTube and audio audience expectations and content needs
• Separating audio and YouTube content to cater to different audiences
• Notifying deploy in Zulip for easy tracking of updates
• Three types of content (audio, YouTube, and video) needed for different audiences
• Discussion of a code deploy process in the Kaizen app
• Uncertainty about who implemented the Zulip integration
• Explanation of how the Zulip API is used and its simplicity
• Clarification that the integration is implemented through a GitHub Action
• Comparison of different approaches to code deployment and communication (PR-driven vs. commit-driven)
• Review of the GitHub Action configuration used for the integration
• Discussion of the costs of using namespace runners (options A, B, and C)
• Discussion of a sponsor, namespace.so, and their concurrent runners offering
• Fixing a GitHub issue with Zulip auth integration
• Introduction of a "pipe dream" concept for a single-purpose CDN on fly.io
• Development of a test suite for the CDN using Hurl.dev and Just tool
• Review of the Hurl.dev tool and its use in testing HTTP endpoints
• Discussion of a Hurl-specific DSL for testing
• Review of a pull request and associated video
• Analysis of a test report and its output
• Explanation of the test's purpose and scope
• Discussion of the need for automated testing of the deployed configuration
• Proposal to run Varnish locally and use mocking to test interactions with other systems
• Proposal to use VCR (Video Cassette Recorder) to record and replay HTTP requests
• Tangential discussion of the original meaning of VCR (Video Cassette Recorder)
• Discussion about the VCP (Video Cassette Player) and the importance of separating concerns
• Introduction of Dagger and its ability to create containers quickly and programmatically
• Review of previous Kaizen discussion about name ideas for a project, including Pipely
• Discovery that the domain Pipely.tech is already registered by someone else, leading to a humorous exchange about the owner's intentions
• Gerhard Lazu's enthusiasm for the name Pipely and his suggestion to build a CDN with the same name
• Adam Stacoviak's excitement about the domain and the potential for a new CDN
• Mention of a future episode featuring a conversation with Kurt Mackey from fly.io and a discussion about the Rebel Alliance
• Discussion of the idea of a new CDN project, Pipely, and its potential to improve existing CDN services
• Recalling a conversation between the speakers about the idea, and the excitement and support it generated
• Reflection on the importance of having a clear name and identity for a project, and the role of storytelling in its development
• Adam Stacoviak sharing his vision for Pipely, including its potential to provide a more effective and user-friendly CDN service
• Gerhard Lazu expressing his support and enthusiasm for the project, and his willingness to dedicate time and effort to its development
• Discussion of the potential for a community-driven approach to developing Pipely, and the idea that it can be a fun and rewarding project
• Adam Stacoviak asking about the feasibility of implementing Pipely's vision, and Gerhard Lazu outlining the roadmap for the project's development
• Discussion of the potential for Pipely to become a reality, and the importance of taking a step-by-step approach to its development.
• Varnish config and HTTPS
• Sending logs to Honeycomb and S3
• Swapping out S3 for R2 or MinIO
• Purge across app instances with Oban
• Edge Redirects and VCL config
• TLS termination and HTTP origins
• Vector.dev for log and metrics sending
• Pipely CDN project status and next steps
• Discussion about a new CDN (content delivery network) called Pipely.tech
• Confirmation that the CDN is a real project
• Reference to the concept of Kaizen (continuous improvement)