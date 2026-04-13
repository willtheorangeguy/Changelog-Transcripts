• Discussion on the format and tone of Kaizen 6
• Introduction of Shipit.show as the new vanity domain for the podcast
• History of short URLs, including tinyurl.com and bit.ly
• Importance of vanity domains in podcasting, particularly for easy sharing and discovery
• The team's attempts to secure shipit.fm and ship.it before settling on Shipit.show
• Banning Unfurl on changelog.com due to abuse
• Fixing 404 error pages for Shipit podcast episodes
• Implementing Kaizen-driven development for Shipit's website and codebase
• Vanity URL redirects (e.g. Shipit.show/apple, Shipit.show/spotify) for easier podcast access
• Handling listener requests and episode proposals through the Shipit.show/request URL
• Discussing communication methods for show ideas and episodes
• Reviewing episode 51's discussion on clustering and multi-region PostgreSQL integration
• Mentioning episode 59, which features SQLite instead of PostgreSQL, but not yet released
• Moving on from managed Kubernetes (LKE) to Fly
• Discussing the importance of keeping old systems in case of problems or need for rollback
• Setting a cadence for regular review of systems
• Using Kaizens as a method for forced change and improvement
• The importance of having a plan B (e.g. an old system) in case something goes wrong with the new system
• Implementing a 30-day rule for reviewing services to determine whether they should be continued or deleted
• Managing certificates for multiple providers (e.g. cert-manager, Fastly)
• Documentation and keeping track of changes and decisions made
• Discussion of the need to purge unnecessary content on podcasts and websites
• Mention of specific directories (2021, 2022) and files (fly.toml) that are no longer needed
• Explanation of Dagger configuration and migration issues
• Reference to a previous episode about migrating from Circle CI to GitHub Actions
• Discussion of using Docker Engine integration with Fly.io
• Explanation of Tailscale authentication issues with GitHub Actions runners
• Dagger and Docker Engine setup on Fly.io
• Caching issues with volumes in Docker
• GitHub Actions runner setup with WireGuard
• Introduction of Fly Machines for on-demand spinning up of instances
• Gerhard's dev box setup with NixOS and multiple hosts
• Dagger package vendoring in the source code
• Docker Engine and BuildKit issues with PostgreSQL containers
• Migration to Fly for better performance and ease of use
• Connecting directly to production database using Fly Proxy
• Fly Machines for on-demand spin up and down of instances
• Clustering support for Changelog app integration
• Chapter support for podcast episodes with Lars Wikman
• Discussion of Ruby on Rails vs Elixir in a library context
• Potential issue with FFmpeg usage in a specific application
• Chapter support for podcasts and its importance
• Migration from local volumes to object storage, S3
• Plans for clustering Changelog apps across multiple regions
• Use of Honeycomb to optimize data center placement based on traffic
• Exploration of using SQLite or alternative solutions
• Benefits of Fly proxy caching and its impact on request times
• Discussion of Litestream and its features, including automatic directory synchronization for SQLite databases
• Potential use of HashiCorp Vault for secrets management and integration with 1Password
• Experimentation with 1Password as an alternative to LastPass for password storage
• Considerations for consolidating password storage at 1Password and integrating it with HashiCorp Vault
• Sharing and discussion of community comments on the Ship It Slack channel
• Discussion of using the Shipit platform for team management
• Plans for adding multiple plans and storing secrets within the platform
• Request to add Gerhard Lazu and Jerod Santo to a plan on Shipit
• Review of the format and content of the Kaizen episode, including laughter and technical content
• Joke about "Boaty McBoatface" and public engagement
• Discussion of the importance of not giving people ideas for trolling
• Conclusion of the episode