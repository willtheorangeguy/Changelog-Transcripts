• Discussion of the new year and starting Kaizen for 2024
• Sharing of humorous moment from a previous gathering in Chicago
• Explanation of Fly app versioning and continuous improvement
• Debate over the naming and organization of subdirectories in the codebase
• Discussion of the Fly.io directory and app instance organization
• Discussion about a specific app or project
• Changelogs and multiple apps running at the same time
• Goal setting and planning for the new year
• Gerhard Lazu's personal goal of creating a content-related project combining audio, video, and AI
• Project scope, timeline, and potential impact
• Discussion of project scope, timeline, and potential impact continuing with Gerhard Lazu's personal project
• Gerhard Lazu's goal of creating something that can be tracked over decades
• Discussing past video production experience
• Adam Stacoviak's goal for the year: bringing Plus Plus in-house and creating a job board to sustain podcasts and promote jobs
• Idea for Changelog.jobs: a SaaS-based job board that integrates with the Changelog network and podcast
• Importance of execution and value in creating a successful job board
• Community feedback and perspective on building software in teams well
• Connection between Changelog's values and goals, and the potential for a job board to be a valuable addition to the community
• Discussion about rebranding Changelog Plus Plus 2.0 and bringing it in-house
• Adam Stacoviak's change of tone on the value of Changelog Plus Plus
• Plan to embed Changelog Plus Plus into shows and make it more dynamic
• Changelog Plus Plus subscription growth and desire to provide more value
• Migrating Postgres to Neon.tech (pull request 492)
• Upgrading dependencies, including Postgres from 15 to 16
• Setup of Neon.tech as a managed Postgres alternative to current Postgres on Fly.io
• Fly.io's ambitions and limitations with databases
• Neon's serverless managed Postgres and branching concept
• Jerod's use case for a dev mode branch of production data
• Simplifying development workflow and reducing dependencies
• Concerns about contributor access to production data and data sanitization
• Migrating to Neon's database service and issues with latency and query performance
• Exploring ways to sanitize a database branch for easier contribution
• Reducing database query latency by optimizing queries and caching
• Discussing the possibility of using read replicas to reduce latency
• Considering connection pooling and other optimizations to reduce per-query cost
• Discussion of potential 20-year project for read replicas and distributing app instances across regions
• Issues with Fastly CDN, including high cache misses and lack of clear explanation from support
• Proposal to build custom CDN using NGINX instances on Fly, serving requests from local disks
• Consideration of moving to Cloudflare or building a custom CDN due to difficulties with Fastly support
• Importance of integrated, embedded partners for infrastructure services
• Embedded sponsorship and partnership with Cloudflare
• Comparison of Fly's services with Fastly and Cloudflare
• Discussion of building a custom CDN and its potential challenges
• Analysis of Fly's limitations and areas for improvement
• Consideration of reliability and uptime of services
• Comparison of burdens of building a custom CDN vs relying on third-party services
• Distributing the app across Fly regions and using Anycast IP
• Using Fly's features for load balancing and instance management
• Configuring NGINX instances for local ephemeral caching
• Handling logs and statistics, including using NATS and an open-source tool called vector.dev
• Comparing costs and pricing with Fastly and Fly
• Exploring the idea of creating an open-source template for a simple CDN on Fly
• Considering alternative CDN tools, such as Traefik and Varnish
• Evaluating the complexity of the existing Varnish config on Fastly
• Discussion of using Varnish and NGINX for caching and configuration
• Comparison of Varnish and NGINX, with Jerod Santo preferring NGINX due to familiarity and ease of use
• Frustration with complexity and lack of straightforward solutions
• Adam Stacoviak suggests investigating Cloudflare as a potential alternative
• Discussion of the potential for hacking and tinkering with infrastructure
• Idea of leaving cdn.changelog.com alone and focusing on Changelog.com
• Investigation of Cloudflare features, including log push and Website Analytics
• Jerod Santo's experience with Cloudflare being limited due to the need for the enterprise plan
• Adam Stacoviak's suggestion that they could "bless" them to turn on the necessary features
• Discussion of the history of considering Cloudflare and Fastly side by side
• Cloudflare and Fastly CDN issues
• Personalized Fly CDN setup
• Supabase on Fly
• KeyCDN research
• Vercel and Neon acquisition speculation
• Fly CDN feature request
• Discussion of Vercel's acquisition of various companies and potential impact on embedded
• Overview of Neon Postgres and its features, including Dev Mode and copy-on-write
• Paradox of choice in the grand scheme of options for developers
• Gerhard Lazu's "Easter egg" feature in pull request 492, which introduces a single secret for app access to all necessary secrets
• Explanation of how 1Password's vault is used to securely store and retrieve secrets
• Discussion of the benefits of using 1Password's vault, including reduced infrastructure and improved security
• Future possibilities, including automatic rotation of leaked secrets and improved integration with 1Password
• 1Password integration for managing secrets
• Using 1Password webhooks
• Comparing dev and prod environments for secrets
• Plan to merge Neon tech into production
• Discussion of building a CDN
• Upcoming move to Neon.tech for hosting and latency improvements