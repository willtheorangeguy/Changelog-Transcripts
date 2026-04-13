• Kaizen 11 improvements and changes
• Discussion on improving vs making progress
• New two-month cadence for recording
• Infrastructure and backend changes
• Implementation of Oban for email delivery
• Bug with duplicate emails being sent
• Jerod's struggles with debugging and resolving the issue
• Upcoming changes and features, including a web UI for Oban jobs
• Discussion on developing in production and the importance of visibility in background jobs
• Oban Web distributed as an Elixir package with subscription model
• CI authentication issues with Hex server
• Persistence and replayability of emails
• Duplicate emails issue with multiple app instances
• Distributed app setup with two instances in Ashburn, VA data center
• Plan for future replication of database and app instances across multiple locations
• Caching issues with multiple backends
• Migration to Fly Apps v2 and its requirements for running multiple nodes
• Deployment configuration and blue/green deployment strategy for Changelog app
• Running two instances of the app to prevent downtime in case of host failure
• CLI update resolved some issues
• Discussion of a caching problem causing "flapping" in podcast feeds
• Jerod's temporary workaround to clear caches every 2 minutes
• Review of Service Level Objectives (SLOs) in Honeycomb, including a latency budget
• Analysis of podcast feed response latency in Honeycomb, showing 95% of feeds served within 1 second, but with some spikes
• Discussion of the implications of the caching problem and the temporary workaround
• Discussing the latency of podcast feeds, particularly the Master feed which is around 11 megabytes
• Exploring ways to reduce the size of the Master feed, such as caching or limiting the number of episodes included
• The issue with paginated feeds not being supported by popular podcast apps like Apple Podcasts and Spotify
• The trade-off between serving the full file or paginating it, and the potential impact on user experience
• Analyzing performance metrics, including cache hits and misses, and discussing potential optimizations
• Identifying a possible improvement in cache misses after a database upgrade on August 4th
• Discussing the possibility that the database upgrade improved the speed of database queries, leading to a decrease in latency.
• Discussion on Postgres 16 improvements
• Analysis of cache misses on feed endpoints
• Potential benefits of caching forever vs. clearing cache every 2 minutes
• Proposal to use CDN (Cloudflare, R2) to serve precomputed files
• Exploring Oban for job processing and uploading feeds to CDN
• Considering infrastructure changes for improved performance
• Migration from AWS S3 to Azure R2 object storage
• Discussion of telemetry and logging for crawlers and Fastly
• Comparison of using Cloudflare and Fastly as CDNs
• Review of the migration process and zero downtime achieved
• Explanation of the cost savings from migrating to R2
• Discussion of the cost of object storage and the impact of the Fediverse on storage costs
• Plans to clean up remaining storage costs and configure Storage Lens
• S3 vs R2, comparing their features and limitations
• Deletion of bucket "Changelog Uploads Jerod" on R2
• Discussion of the need for GUI tools for R2, specifically a "D2" app
• Comparison of R2 to S3 in terms of tooling and compatibility
• Use of AWS CLI and scripting for deleting objects on R2
• R2's lack of support for streaming uploads and its API compatibility with S3
• Consideration of keeping a backup of Changelog assets on S3
• Discussion of CDN backup options, including R2 and B2
• Comparison of B2 and S3 pricing for backup storage
• Use of a backup service to mirror R2 backups to B2
• Designing a CI/CD job to move backups between B2 and R2
• Discussion of Dagger and GitHub Actions, including potential acquisition
• Resilience in CI/CD pipelines, including use of GitHub runners as a fallback
• Dagger as a single codebase with multiple runtimes (Fly, GitHub, Kubernetes)
• Kubernetes as a production environment, with a fallback to GitHub if it's unavailable
• Resiliency and fallback mechanisms in the pipeline
• GitHub Actions limitations in defining fallbacks
• Use of Fly, Docker, and R2 as primary and backup storage options
• Business continuity and backup strategy for storing assets and data
• Deletion of an S3 bucket and consideration of deleting old backups
• Discussion of unnecessary backups of Changelog Nightly
• Decision to keep only the most recent backup and delete the rest
• Proposal to set up automatic purging of old backups
• Discussion of the Nightly folder structure and its size
• Mention of the security implications of running Changelog Nightly on an old Digital Ocean droplet
• Idea to move Changelog Nightly to the Fly platform
• Discussion of the challenges and limitations of modernizing Changelog Nightly, including its legacy codebase and dependencies
• Proposal to use a Docker container to host Changelog Nightly
• Discussion of using Docker to run Jekyll and Ruby without installation
• Concerns about spam and malware in Changelog Nightly
• Attempt to use ChatGPT for malware/spam detection with limited success
• Plans to "daggerize" the Nightly system
• Introduction of a status page at status.changelog.com for incident reporting
• Discussion of the next Kaizen sprint
• Upgrading Changelog Nightly on Digital Ocean
• Clustering for Phoenix Pub/Sub
• Installing Oban Web for observability
• Exploring Middleware.io for AI-powered cloud observability
• Discussing limitations of Honeycomb's free plan (2 SLOs)
• Understanding the relationship between SLOs and triggers in Honeycomb
• Discussing the concept of Single Objectives (SLOs) and whether to have multiple SLOs or triggers
• Noting that SLOs have become a "buzzword" and may be overused
• Mentioning the importance of having an open-source codebase and integrating with other tools
• Highlighting the importance of having a community and inviting listeners to join and participate
• Discussing the benefits of open communication and sharing knowledge
• Providing a call to action to join the community and invite others to join