• Introduction of guests and sponsors
• Discussion of backup software, specifically Restic and Alexander Neumann's project
• Comparison of Restic with other backup programs, focusing on security, speed, and usability
• Why Alexander Neumann chose Go as a programming language for his project
• Personal anecdotes about hacking and old computer systems, including Delphi and Trojan horses
• Importance of separate specification for Go versions
• Committing vendor directory for reproducible builds
• Design and implementation of Restic's build script
• Use case for Restic: backing up large directories with multiple revisions
• Thread model for storing data on potentially untrusted servers
• Detection of file changes using SHA-2 hash sums in pack files
• Popularity of Restic and managing contributors and releases
• Dealing with support requests from companies and users
• New Restic release with improved S3 backend support
• Reduced memory allocations by 98% using Minio's lower-level API
• Discussion of deduplication in Restic and its benefits
• Explanation of rsync algorithm for detecting file changes
• Introduction to Rabin fingerprinting algorithm used in Restic
• Implementation of Rabin fingerprinting in Go for efficient blob creation
• Overview of how Restic stores and manages blobs, including encryption and hashing
• Restic's ability to efficiently store snapshots of changed data
• Fuse Mount feature for browsing snapshots and restoring data on demand
• Importance of backups and detecting silent hard drive failures
• Password protection and key derivation functions in Restic
• Responsibility and guilt associated with open-source software development
• Ease of use and simplicity of backup programs as a factor in users' willingness to back up their data
• Borg vs Restic workflow and usability
• Restic's use of Viper and Cobra for CLI and configuration
• Concerns about config files and key management
• Restic's design philosophy: simplicity and robustness over flexibility
• Upcoming features: compression, new repository format, and caching
• Repository versioning and backwards-compatibility
• Go version compatibility and backup capabilities
• Kelsey Hightower's DevOps Days speech and his keynote presentation on deploying a Kubernetes cluster with voice control
• Releases of Go 1.8.2 and 1.8.3, including security fixes and other minor updates
• Delve release candidate for version one
• Visual Studio Code update with Delve integration and code lenses
• Upcoming guest Ramya on the show next week
• Discussion about missed episodes and catching up on news
• #FreeSoftwareFriday pick: rofi-pass, an interactive input tool for shell scripts
• Discussion of rofi-pass for password management
• Introduction to barista, an i3 status bar written in Go
• Shoutouts and recommendations:
	+ Kelsey Hightower's talk
	+ Visual Studio Code (by Matt)
	+ Brendan Gregg's website and tools for profiling and performance tuning
• Upcoming workshop by Brian Ketelsen on FlameGraphs at GopherCon
• Ashley McNamara leaves the conversation to attend a meeting 
• Conversation ends with goodbyes from Erik and Alexander