• The host, Gerhard Lazu, has prepared a slideshow with talking points and screenshots for the Kaizen discussion
• The discussion will start with the "pipe dream" project, which was a topic from the previous Kaizen
• The pipe dream is a simple CDN built using Varnish Cache, running on Fly.io, and is a smaller version of their current CDN
• The project has its own GitHub repository and has had two pull requests, including one for dynamic backends
• Gerhard has outlined a roadmap for the project, including adding a feeds backend, sending logs to Honeycomb, implementing purging across all instances, and importing edge redirects from the current CDN
• The hosts discuss the project's progress and potential next steps
• Handling logs: decision to track feed requests like MP3 requests and store them in Honeycomb and/or S3
• Purge functionality: discussion on implementing purge across all app instances, with options for using Oban, DNS, or another approach
• Cache storage: clarifying where cache data is stored (in Pipe Dream, a CDN) and how it's managed (e.g. Varnish storing cache locally)
• Expiring cache: discussion on automating cache expiry when content is updated, and using Pipe Dream to purge caches
• Pipe Dream: considering renaming it, but Gerhard Lazu likes the name and its origin story
• Discussion of the name of a project or product, specifically "Pipedream" and its various spellings
• Proposal to run a poll to determine the final name
• Mention of the project's goal to become a CDN (Content Delivery Network) and its importance
• Discussion of the project's roadmap and potential for success
• Idea to open-source the project and its related issues
• Discussion of the project's potential as a product, single-tenant and single-purpose, and its potential to be integrated with Fly.io
• Mention of a competitor, Tigris, and its success with Fly's platform
• Discussing the creation of a simple CDN called Pipe Dream built on Fly, its potential as a product, and its private version
• Decision to build Pipe Dream in the open and then genericize it in a separate effort if it turns into a product
• Shout-outs to contributors, including Matt Johnson and James A. Rosen
• Transparency and open discussion about Pipe Dream's development and potential
• Live streaming the CDN journey with Peter Mbanugo
• Moving on to discussing custom feeds, a feature for Changelog.com that allows members to build their own feeds
• Explaining the technical limitations of Supercast and how to overcome them to implement custom feeds
• Realizing that a simple Stripe integration can provide membership information and enable custom feeds
• Planning to implement custom feeds without fully moving away from Supercast
• Creating custom feeds on Changelog.com
• Gerhard Lazu builds his first custom feed, "Gerhard's Feed"
• Custom feed settings and options, including cover art, title format, and podcast selection
• Issues with custom feed cover art and title format
• Bug report for custom feed cover art issue
• Discussion of Changelog++ member benefits and custom feed adoption
• Plans for future Changelog features, including custom artist-created cover art options
• Adam Stacoviak is having issues with creating a custom feed URL, which is not being recognized by Overcast
• Gerhard Lazu identifies the issue as the copy URL button not copying the entire URL, only the path
• A quick fix is provided by right-clicking and selecting "Copy URL" instead of clicking the button
• The issue is also related to a previous fix made by Jerod Santo that may have caused the problem
• Adam Stacoviak also asks about the "This feed should contain Plus Plus" checkbox, which is only visible to Plus Plus members or admins
• Jerod Santo explains that the checkbox is only visible to Plus Plus members or admins, and that custom feeds are a marginal cost
• The conversation also discusses the user experience of creating custom feeds, and how it requires some technical knowledge
• Implementing email notifications for URL changes in a feature
• Adding an "Email this to me" button for convenience
• Introducing Zulip chat and the process of joining it
• Discussion of custom feeds and their benefits for Plus Plus subscribers
• The idea of creating a Kaizen channel for continuous improvement
• Feedback on the latest news feature and its improvements
• Discussing slow application deploys and the goal of achieving a 2x faster time to deploy
• Historically, deploys have been too slow, taking 7-10 minutes
• The team aims for a threshold where deploys feel instantaneous or take around 1-2 minutes
• Previous deploys were slowed down by a Dagger engine on Fly, which often failed to connect
• A recent change used Namespace.so, which provides faster GitHub Actions runners and caches operations
• This change has improved deploy times, with the goal of achieving a 2-minute deploy time
• The team is now analyzing build times and deploy times separately to optimize the deployment process
• The goal is to halve the deployment time by optimizing the deployment process itself
• Application boot time and optimization
• Understanding the application deployment process and flow
• Investigating the cause of variability in build times
• Evaluating the use of third-party services, specifically Namespace
• Calculating costs and pricing for the Namespace service
• Understanding the features and capabilities of the Namespace service
• Discussion of a credit card issue
• Hugo Santos is identified as a potential contact for Namespace
• Review of Neon's performance, including metrics and resource usage
• Plans to use Neon for development databases
• Discussion of the need for more arbitrary workloads to test Neon's capabilities
• Review of branching and integration of features in Neon
• Discussion of a tool for automating Neon CLI installation and setup
• Discussion of 1Password CLI vs SDK for native integrations
• Review of Dagger and containerization for tooling and development
• Introduction of new tooling, Just, a command runner written in Rust
• Comparison of Just to manual tooling and Dagger for simplicity and ease of use
• Plans to implement Just db-prod-import and Just db-fork for database management
• Personal experiences with Dagger and manual tooling for development and pain points
• Demo and testing of Just tooling for local development and database management
• Switching from ASDF to brew install Postgres due to compilation issues
• Introduction to Just, a tool for automating local development tasks
• Using Just to install and manage dependencies, such as Postgres
• Comparison with Dagger and potential for improvement
• Using Just in a GitHub repository for local development
• Exploring the Just community and Casey Rodarmor, the author
• Gerhard Lazu will be giving a talk called "Homelab to production" at TalosCon (now referred to as the GarrisonCon)
• He plans to bring his mobile lab to the conference and will be doing a live demo of migrating workloads from his homelab to production using Talos, Kubernetes, and Dagger
• The talk will be recorded, and Gerhard will also be recording himself and the conference with two cameras and a Rode Pro microphone
• The team discussed future plans, including continued progress on Pipe Dream (now referred to as Pipely.tech) and the possibility of buying the domain name pipe.ly
• They also discussed the idea of raising $50,000 to buy the domain name