• Celebrating 50 episodes and one year of consistency in releasing weekly podcasts
• Discussing podcast longevity and burnout, citing examples of shows that didn't reach 50 episodes
• Congratulating Gerhard Lazu on achieving 50 episodes with the current show
• Request system for listeners to suggest guests or topics they'd like to see return
• Discussion about the Changelog's technical setup, including hosting on Fly.io and AWS S3
• Kaizen episode where Jerod Santo added CDN shielding live during the recording, resulting in significant cost savings
• Discussion of Changelog's massive traffic volume, with 1.5-3 terabytes per day
• Importance of proper caching and CDN configuration to manage traffic and costs
• Ship It podcast popularity in Taiwan and lack of popularity in Japan
• Analysis of Changelog's total monthly traffic (45.6 terabytes in March)
• Comparison of episode file sizes (40-100 megabytes) and range requests being served
• Discussion of the switch from LKE to Fly.io as a new origin for static assets
• Dynamic robots.txt causing indexing issues on subdomains
• Lost host header information after migrating to Fly
• Blocking Google from indexing website due to technical issue
• Desiring multiple origins (e.g. not just Fly) for platform flexibility
• Issues with page updates and caching, potentially related to Fly proxy
• Miss latency and speed concerns when requesting content from CDN
• Increased latency from Fastly CDN to origin
• Removal of shielding on Changelog.com domain or origin
• Comparison of traffic hitting Fly vs Kubernetes
• Reasons for migrating off Kubernetes: 
  • Desire for deeper relational partnerships with Fly
  • Need for a managed PostgreSQL service
  • Forced migration due to end-of-life notice from Kubernetes 1.20
• Previous platform issues and complexities, including downtime with PostgreSQL
• Forced upgrade to 1.21 by Linode resulted in issues with PostgreSQL data and local storage
• Desire for deeper partnership with a cloud provider, including empathy and technical advocacy
• Migrated from Linode to Fly.io due to lack of access and support from Linode
• Enjoyment of PaaS (Platform-as-a-Service) model, as seen with Heroku
• Simplification of platform administration is a key benefit of the new setup
• Kubernetes 1.20 to 1.22 migration issues due to Fastly and Fly.io integration
• VCL misconfiguration caused requests not to be cached or served correctly
• ClickOps-generated VCL code resulted in complex, hard-to-debug configuration (12,000 lines)
• Temporarily implemented a VCL hack to work around the issue
• Migration to newer Kubernetes version was necessary due to time constraints and potential app breakage or data loss
• Plan C (migration to new Kubernetes) was successfully executed
• Difficulty with forced upgrade from Linode to Fly
• Issues with data loss, app breakage, and dire situation during migration
• Experience with Fastly's VCL (Version Control Language) and its complexity
• Challenges in collaborating with Fastly support for resolution of issues
• Importance of empathy and partnership in platform development
• Discussion on the value of feedback loops and community involvement in improving platforms
• Jerod Santo discusses his wishlist for Fly.io features, including automated Postgres backups and improved secret management
• He mentions the lack of certain features compared to Heroku and suggests ways to improve user experience
• Gerhard Lazu agrees that these are important issues and mentions Fly's differences in application lifecycle management
• They discuss integrating Fly logs with Honeycomb for easier querying and analysis
• Certificates and certificate management are brought up as a significant issue, specifically the inability to obtain private keys on Fly
• Cert-manager to manage certificates
• Fly's limitations with robots.txt and private keys
• Upcoming podcast episode 51 featuring Mark from Fly discussing improvements and new features
• Collaboration and strengthening partnership between Changelog and Fly
• Business continuity planning in case of platform failure (e.g. Fly going down)
• Portability and multi-platform support for the Changelog system
• Kubernetes and cloud-native discussed
• Gerhard's contact information shared (Twitter, Changelog Slack, email)
• Issue 407 mentioned as a resource for learning about migration
• Upcoming topics suggested (KubeCon EU, microservices, Knative, Cloud Run)