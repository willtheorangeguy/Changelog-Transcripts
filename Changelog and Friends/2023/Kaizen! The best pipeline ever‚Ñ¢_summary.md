• Gerhard Lazu is a long-time contributor to Changelog and has been involved since 2015.
• Kaizen is a process of continuous improvement, where small changes are made regularly to improve something over time.
• Changelog's previous show, Ship It, had a Kaizen episode every 10 episodes, where they discussed improvements made to the platform.
• The new show, Changelog & Friends, will have a Kaizen episode every other month, where they discuss recent improvements and changes made to Changelog.com.
• Changelog.com is an open-source podcasting platform written in Go, and Gerhard discussed some of the improvements made to the platform.
• Discussion of Changelog.com's deployment infrastructure, including its use of Fly, Fastly, Postgres, and the Dagger tool
• Mention of the platform's purpose as a testing ground for new services and techniques, as well as a way to learn and experiment
• Description of the platform's "kaizen" process, where they continuously improve and refactor their infrastructure
• Explanation of the switch from using CUE to Go for configuring pipelines, and the benefits of using a programming language for this purpose
• Mention of Gerhard Lazu's involvement with Dagger, including his role at the company and his passion for deployment and CI/CD tools
• Discussion of the Dagger Go SDK 0.5 and its introduction of SDKs for writing pipelines in Go, Python, and Node.js
• Mention of the platform's migration from CUE to Go, and the gradual improvement of their pipeline infrastructure
• Running Dagger on Fly Apps version 2, using WireGuard tunnel and Dagger CLI to connect to remote engine
• Integrating Mage pipeline with Dagger and Fly Apps, showing a pipeline with three stages: building runtime image, production image, and running tests
• Caching and dependency management, with Mage detecting code changes and only re-running necessary steps
• Using ASDF to manage multiple runtime versions of dependencies (Erlang, Elixir, Node.js) and install tools (Mage, PostgreSQL) with versioning down to patch level
• Discussing the benefits of using ASDF to manage versioning and dependencies, and avoiding versioning issues in development and production environments
• Discussion of a bug in a TLS library in an Erlang patch version
• Use of ASDF for dependency management and specifying tool versions
• Explanation of the .tool-versions file format and its simplicity
• Comparison of ASDF with Homebrew and Nix Package Manager
• Overview of how ASDF integrates with pipelines and containers
• Discussion of PostgreSQL upgrade and data migration requirements
• Explanation of how ASDF handles PostgreSQL upgrades and versions across dev, test, and prod environments
• Review of the limitations of ASDF, including PostgreSQL upgrades.
• Discussing the potential generalizability of their infrastructure for use in other projects
• Pipeline parallelization and performance improvements
• Switching to Fly Apps v2 Dagger Engine for faster deployment
• Clustering and scaling to support multiple instances of the Changelog app
• Targeting a deployment time of under 20 seconds
• Migration of Changelog News onto its own podcast and meta feed
• Upcoming changes to Changelog News' web pages
• Integration of Honeycomb tracing into the system
• Prototype for clusterable caching solution
• New Open AI integration in Honeycomb for generating queries
• Discussion of generative AI and fine-tuning user experience
• Similar integrations in other tools, such as Sentry
• Shout-out to A.J. Foster and Dave Lucius for blog posts on integrating Honeycomb tracing
• Discussion of Google's Bard and Open AI's GPT-4, with opinions on their accuracy and capabilities
• Comparison of Bard and GPT-4, with specific examples of Bard's inaccuracy in code understanding
• ChatGPT's ability to accurately answer a question about deploy frequency, using a specific date range
• The hosts' development process and use of pull requests, with a preference for trunk development
• Ken Kost's contribution to the project, specifically his work on W3c HTML Validation Fixes
• Discussion of contributions and how to facilitate them, including infrastructure needs and project vision
• Future plans and ideas, including integrating Tailwind into the app and moving away from an old design
• Personal anecdotes and humor throughout the conversation
• Managing contributors to an open-source repository
• Difficulty in creating a clear roadmap and making decisions for the website
• Challenges in balancing features and pricing for software products
• Overview of Apps v2, a platform for building and deploying applications, and its benefits
• Discussion of infrastructure and availability, including the use of Fastly and CDN for high availability
• Discussion of the impact of a Fastly outage, where Jerod Santo compares it to a day off for the whole world
• Limitations of Apps v2, specifically that apps cannot be scheduled elsewhere if the host is unavailable
• Need for clustering to make Apps v2 more resilient
• Review of infrastructure and services, including PostgreSQL, Dagger Engine, and Docker
• Discussion of deleting old code and infrastructure, including news items and obsolete features
• Reflection on the design and architecture of the Changelog platform, including the use of single-table inheritance
• Discussion about the obsolescence of certain parts of the Changelog codebase
• Plans to refactor and remove outdated news item-related code
• Commitment to incremental change and Kaizen approach
• Review of the Changelog pipeline and discussion of improvements
• Importance of consistency and adapting to changes
• Invitation for community participation in Kaizen discussions and code contributions
• Shout-out to Jason Bosco for contributing to Kaizen 10
• Discussion of search functionality and potential deletion of Algolia code
• Gardening principle of constantly improving codebase
• Discussion of Typesense, a super-fast in-memory search technology
• Introduction of new show format, Changelog & Friends, and discussion of future topics
• Home lab setup, including UniFi, Ubiquiti, and VLANs
• Discussion of network setup, including IoT and backup network options
• Ubiquiti and Mikrotik products, including WiFi coverage and mesh networking
• Discussion of Mikrotik and UniFi routers, with a focus on their UI, stability, and features
• Upcoming plans for the Changelog & Friends podcast, including potential guests and topics
• Review of current infrastructure and potential upgrades, including 1Password integration, Honeycomb, and Uptime Kuma
• Discussion of Cloudflare and its potential as a replacement for current infrastructure
• Plans for migrating to Cloudflare R2, including testing and potential issues with Transmit and S3 clients
• Review of current AWS costs and potential for significant savings with Cloudflare R2
• Plans for clustering, caching, and other infrastructure improvements
• Desire to migrate off SuperCast and onto a new platform
• Offering a customizable feed for Plus Plus members
• Current limitation of SuperCast only allowing one feed
• Plan to move to own platform for more customization and control
• Discussion of subscription management and email handling
• Gerhard's request for help with duplicate instance of Changelog not sending emails
• Kaizen process for continuous improvement and iteration