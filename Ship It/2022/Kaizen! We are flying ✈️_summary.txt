• Migrating changelog.com to fly.io and managed Postgres SQL
• Importance of partner relationships (e.g. Honeycomb, fly.io)
• Congratulating Adam on reaching 50 episodes with the podcast
• Discussion of podcast consistency and longevity
• Request for listener feedback on favorite guests or topics
• Request from Simi DeClerc to discuss Changelaw on Heroku
• Exploring alternative platforms and services (Fly.io)
• Reviewing past episode on migrating static assets to AWS S3
• Discussing recent issues with high AWS bills and cost optimization efforts
• Implementing caching layers and surrogate cache control keys for cost reduction
• The speaker expresses gratitude for Kaizen and acknowledges a few manual tasks needed to set up Amazon S3.
• The speaker estimates Changelog's daily traffic at around 1-2 terabytes, with some days reaching 3 terabytes.
• Fastly is praised for effectively fronting large amounts of global traffic, particularly from Taiwan.
• The speaker calculates the total monthly traffic at approximately 45-50 terabytes, citing an example month (March) where they served 45.6 terabytes.
• Changelog's episode sizes are mentioned to range from 40-100 megabytes, with some episodes being partially listened to and ranges being frequently requested.
• Discussion about a migration from LKE to Fly.io
• Noticing any changes in app behavior or errors since the migration
• The concept of "invisible" work, where users don't notice any changes
• Robots.txt issue and its resolution
• Dynamically served robots.txt for limitless subdomains
• SEO implications of indexed subdomains with duplicate content
• Transition to Fly and issues with Google indexing
• Fixes for robots.txt issue after migration to Fly
• Importance of reviewing codebase for edge cases
• Plans for multi-origin setup on Fly platform
• Lessons from past migrations (LKE, S3)
• Unknown unknowns in migration process
• Issues noticed since migrating (e.g. caching issues)
• The speaker is investigating a problem where the page was not updating, but updated after saving it again.
• The issue might be related to the fly proxy or caching, as the speaker suspects that something may be happening at this layer.
• The fly proxy is a new component introduced recently and its behavior is not well understood due to lack of logs.
• Missed latency has increased significantly, from 115ms to over 250ms, when requests can't be served from the CDN and need to go to the origin.
• Shielding was removed, which means that requests now directly go to the origin instead of being cached by another Fastly pop.
• Importance of documenting deploys in the service catalog
• Incident analytics for extracting meaningful insights on reliability and incident response
• Role of incident runbooks in automation and custom rules
• Features of Fire Hydrant, including Slack channels and Jira tickets creation
• Migration from Kubernetes and reasons behind it (not due to listener request)
• Discussion of why the podcast host app is not written in a specific programming language (Go or Rust)
• Reintroduction to Kurt Mackey and his company
• Desire for great relational partnerships with the company
• Interest in their fly platform and how it engages with developers
• Influence on Elixir and other frameworks/platforms
• Attraction of being a fun and easy partner to work with
• Opportunity to help improve the platform and share benefits
• Previous experience with PostgreSQL issues and downtime
• Consideration of managed PostgreSQL options, including MySQL
• Upgrading Kubernetes from version 120 to 122 due to end-of-life notice
• Migration issues and testing of S3 assets with the new app configuration
• PostgreSQL data stored on local storage due to reliability concerns with block storage and volumes
• Force upgrade to Kubernetes 121 being forced, causing potential system breakage
• Requesting a deferral or delay in the upgrade process due to prior commitments and pressures
• The speaker and others had a frustrating experience with Linode's support, feeling it lacked empathy and understanding.
• A deeper partnership between the company and Linode would have helped avoid issues.
• Working with Fly makes sense because of the potential for a more collaborative relationship.
• The speaker desires to partner at a deeper level with companies like Fly due to their show and work.
• Having a deeper partnership would allow for better communication, guidance, and forgiveness in case of issues.
• The speaker is excited about the shift to Fly from Linode due to past experiences with Heroku.
• The speaker is discussing their experience with various development platforms, including Heroku and Kubernetes.
• They mention feeling overwhelmed by the complexity of other platforms and preferring the simplicity of Heroku.
• The speaker expresses excitement about being able to manage Heroku without needing help from others.
• The conversation turns to exploring alternative platforms that might be suitable for a colleague named Jared.
• The interaction with Fly.io was amazing, with a feedback loop that allowed for quick issue resolution.
• A genuine issue on the platform was fixed within a day due to active iteration and comments from Kurt on the PR.
• The team migrated from Kubernetes 120 to 122 at 4am due to issues with Fastly and Fly.io not working together.
• The experience highlighted the challenges of using PaaS (Platform-as-a-Service) when it is not easy or straightforward as expected.
• The team eventually resolved the issue by reverting to a previous version, doing an LK upgrade, which took only 15 minutes.
• Incident with PR407 where requests were not being served from AWS S3
• VCL misconfiguration was the problem, caused by a subroutine termination before backend setup
• Large amount of "gibberish" code in 12,000 lines of VCL config
• Click ops generated code is complex and hard to navigate
• A hack is used to make it work but it's not fixed
• Issues with integrating VCL snippets and merging them into valid code
• Removing an origin and adding another caused routing problems despite correct configuration
• Nested if statements causing issues
• Difficulty determining order of domain/origin entry
• Alphabetical ordering issue with VCM
• Using Fastly and Lazer.ch services to troubleshoot
• Migration to Fly.io delayed due to procedural code issues
• Reference to the movie Swordfish and a 48-hour deadline
• Upgrading to newer Kubernetes version due to complexity and lack of time
• Migration process involved upgrading from Kubernetes 1.20 to 1.21
• Potential consequences of not upgrading, including app breaking and data loss
• Linode's refusal to grant an extension or offer a different solution
• Emergency migration to avoid app failure and data loss
• Utilizing an LK1.22 solution as a last resort
• Normal mistakes happen in VCL
• Factoring in mistakes when creating or editing VCL
• Behind-the-scenes explanation of a recent issue with the VCL
• Discussion of the complexity of Fastly's VCL generation
• Impact of shielding on VCL readability and difficulty
• Complicated setup process for Fastly shields
• Potential to introduce bugs through UI-generated VCL
• Specific bug example related to backend configuration and subroutine exit
• Frustration with certificate issue still unresolved after two years
• Importance of partnerships and feedback loops in improving platforms
• Desire to not just leverage existing platforms but also contribute to their improvement
• Feedback loop as a key reason for starting Shipit and its importance in improving systems
• Open-source code and integration with well-tuned applications in production
• License and permissions
• Community involvement in innovation
• Observability solutions for cloud-native teams
• Challenges with Prometheus monitoring
• The importance of visibility and control in observability data management
• Benefits of using Chronosphere's platform
• Chronosphere.io demo
• OpenZD and its benefits for zero trust networking
• NetFoundry and their SaaS offering
• VPNs and DNS limitations
• Postgres integration with NetFoundry
• Using SSH to access a server
• Familiar tools like PG Dump and PSQL
• Automated backups for Postgres databases
• Managing secrets in the Fly platform
• Difficulty with accessing environment variables
• Desire for more user-friendly features
• Concerns about security and user experience with encrypted SSH connections
• Discussion of Postgres backups and automation
• User's request for a solution to improve their experience while waiting for improvements
• Reflecting on past experiences and lessons learned
• Importance of backups before application migration
• Issues with Heroku's lack of nice hooks for application lifecycle events
• Difficulty in triggering backup processes manually
• Crash dump storage and management
• Integration with Phoenix, Elixir, and Erlang
• Fly logs and logging features
• Honeycomb integration and querying logs
• Gerhard's feature request for integrating Fly with Honeycomb
• General discussion of features and capabilities
• App telemetry and integration
• Migration to new system and focusing on app logs
• Getting app logs into JSON format for Honeycomb
• Integrating fly proxy logs with Honeycomb
• Accessing ingress nginx logs in kubernetes
• Understanding interface between fastly and application
• Certificates will expire in two months
• Problem with certificates due to private key issue
• Using cert manager in LKE (Lightweight Kubernetes Environment)
• Private key cannot be uploaded to CDN (Content Delivery Network) on fly
• New deadline set for resolving the problem within two months
• Certificate management
• Fastly and Fly integration with ACME
• Limitations of multiple providers managing certificates simultaneously
• Using Fastly for certificate management
• Simplifying certificate management process with a single provider
• Integration of logs with Honeycomb
• Discussion of unique features of Honeycomb for data analysis
• Upcoming episode of "Ship It" featuring Mark from Fly, discussing improvements to the platform and collaboration between companies
• Exploration of Fly's capabilities and potential areas for improvement from a Kubernetes perspective
• Feature requests and implementation by Fly, including certificate management and key sharing
• Kubernetes management at a higher level
• Partnership and exploration of alternative platforms like Cloud Run and Fly
• Concerns about relying on a single platform (e.g. Fly) and mitigating against potential outages
• The importance of having a "plan B" for business continuity and failover scenarios
• Migrating a PostgreSQL database to a different platform
• Future plans, including reaching out to GearHost about KubeCon EU and digging deeper into issue 407
• Six years since using Kubeflow for production
• Many changes have likely occurred in that time
• Invitation to share migration stories from Kubernetes to Kubeflow