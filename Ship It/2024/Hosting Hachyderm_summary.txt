• Introduction to the podcast Ship It and its host Justin Garrison
• Discussion of ActivityPub and Mastodon, decentralized social networks
• Personal story about how Justin met his wife, Autumn Nash, while working at a college IT department
• Interview with Preston Doster, infrastructure architect at Twilio, discussing their telecommunications company and APIs
• Explanation of what Twilio does and how it's used by companies like Uber Eats and DoorDash
• The importance of 2FA complexity and Twilio's limitations
• Justin Garrison's experience with Twilio and his desire for iMessage or RCS support
• Preston Doster's offer to send documentation on RCS implementation
• Hachyderm.io, a large Mastodon instance, and its infrastructure
• Kris Nova's role in starting Hachyderm and its growth from 500 users to over 30,000
• The challenges of scaling a decentralized platform like Mastodon
• Preston Doster's description of Hachyderm's infrastructure, including metal servers, Postgres, PgBouncer, Redis, and Sidekiq
• Architecture design for Mastodon instances and federations
• Scalability issues with large followings and network traffic
• Comparison to Twitter's architecture and handling of popular users
• Data-driven applications and designing for variable user behavior
• CDN implementation and caching for speed and load distribution
• Storage solutions (NFS, DigitalOcean Spaces) and data management
• Funding model through the Nivenly Foundation and open-source contributions
• Supporting open source contributors and making it possible for them to work full-time on projects
• Nivenly's funding model, including donations and sponsorships
• Transparency in financial reporting for Hachyderm, with plans to publish quarterly reports
• Breakdown of costs for Hachyderm, with most expenses going towards media storage
• Leasing servers through Hetzner, rather than buying hardware outright
• Multi-cloud infrastructure for Hachyderm, with the goal of avoiding a single point of failure
• Rotating team management for Hachyderm, with core individuals and volunteers contributing to maintenance and upgrades
• Challenges in upgrading Hachyderm's database, including potential migrations
• Use of Terraform, Ansible, and Rake for infrastructure management and deployment
• Database migration caused delays
• Current incident response process relies on Uptime Robot and manual checks via Discord
• Preston Doster mentions an upcoming project to integrate OpenTelemetry with Mastodon 4.3.0
• Team has around 11,000-12,000 monthly active users and 55,000 total accounts
• Sidekiq queues are a major stress point and area of focus for scalability improvements
• Database is another concern due to its importance as the primary data storage
• Regular backups (weekly full backup and daily incremental diffs) are in place for disaster recovery
• Team relies on experienced individuals with expertise in infrastructure management to help mitigate risks
• Tuning queues, parallelism, number of queues, and deployment strategies
• Postgres database configuration and scaling challenges
• Metal server infrastructure and its limitations compared to cloud services
• Data residency and legal jurisdiction considerations when hosting social media platforms
• The Mastodon project's approachability and low barrier to entry for users
• Discussion about Ruby programming language and its use in the Mastodon project
• Challenges of hosting Mastodon in multiple jurisdictions due to varying laws and regulations
• DMCA takedown notices and potential liability for hosting user-generated content
• Importance of moderation and community guidelines for maintaining a healthy social network
• Relaying content from other servers and potential issues with spam or illegal activity
• Defederation lists and subscription services for blocking unwanted content
• Relationship between Mastodon, ActivityPub, and Threads (Facebook's new platform)
• Concerns about Meta's potential plans to turn on federation by default and its impact on the Fediverse
• Discussion of ad placement and potential manipulation through federation
• Trust issues with relying on other servers to send content and metadata
• Moderation practices as a key aspect of maintaining a well-functioning community
• Comparison between Mastodon's moderation model (server-based) and others (e.g. Blue Sky, Twitter)
• Migration to a new community with metadata and followers but not content
• Exporting data from social media platforms (e.g. Twitter, Facebook) as a zip file or mini website
• Mass-deleting social media posts due to API limits or third-party services
• Concerns about data ownership and control on large social networks
• Storage costs for servers like Hachyderm and balancing archive vs. deletion of content
• Long-term risks such as rising storage costs, changing laws/jurisdictions, and potential shutdowns
• The importance of hands-on experience in technology infrastructure
• Open source projects as a way for beginners to gain experience and build their resume
• Benefits of contributing to open source projects, including documentation work
• Career paths and experiences in Kubernetes release teams and other tech-related fields
• Preston Doster's background in engineering and his hobby of synthesizer music creation