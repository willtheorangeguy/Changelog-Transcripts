• Introductions and welcome to the show
• Discussion of "chasing the nines" and high availability
• Setting Service Level Agreements (SLAs) and Service Level Objectives (SLOs)
• Gerhard Lazu's history with the company, including his first contributions in 2016
• Overview of the GORCE tool and its use in visualizing codebase history
• Reminiscing about past collaborations and episodes of Ship It
• Kaizen is a concept of continuous improvement for the better
• Agile principles include small improvements, iteration, and continuous delivery
• Changelog has been implementing Kaizen by discussing improvements every 10 episodes or every 2.5 months
• New cadence will be every other month on Changelog and Friends
• Changelog.com is an open source podcasting platform written in Elixir and Phoenix
• Platform is continuously improved and experimented with for learning and hacking
• Discussion of balancing work and personal time, with a focus on giving oneself permission to try new things
• Mention of Dagger, a tool for configuring pipelines, and its switch from Q to Go configuration language
• Explanation of Dagger's benefits, including running pipelines locally and container runtime
• History of Dagger's development, including its upgrade to 0.5 and addition of new features
• Discussion of the ability to write pipelines in various languages, including Go and Python
• Mention of future plans, including the addition of Elixir support
• Dagger is a tool for deployment and pipelines
• Dagger was created by a team that also worked on E-deliver, a fork of the Deliver Bash framework
• Dagger introduced SDKs for writing pipelines in Go, Python, or Node.js
• The speaker prefers to write pipelines in Go
• Dagger has been migrated to use Go for pipelines, replacing YAML
• The speaker demonstrated running Dagger on Fly Apps Version 2, with Mage CI inside Dagger
• The speaker showed a pipeline with multiple tasks, including building runtime and production images and running tests
• Dagger's UI shows the different pipelines and how they combine
• Discussing the process of updating an image in the assets folder without touching Elixir code
• The new code running the mix Phoenix digest command and not recompiling everything
• Future improvements to the pipeline, including splitting static assets from dependencies and application code
• The current performance of the pipeline, which takes around one minute and 39 seconds to recompile everything
• The use of ASDF for managing multiple versions of runtime dependencies and languages
• The past use of RVM, NBM, and other version managers in different ecosystems, and the creation of ASDF as a unified tool
• The benefits of using ASDF, including ease of use and version management
• Using ASDF to manage dependencies
• Solving versioning issues across different dependencies
• Capturing every single dependency version, including patch versions
• Avoiding subtle differences in local development vs production environments
• Using Nix package manager as an alternative, but with trade-offs
• Reusing the tools versions file in the pipeline for consistent versioning
• Simple syntax and format of the .tool-versions file
• Using ASDF for managing tool versions and dependencies
• Concurrency of tool versions (ASDF vs Homebrew)
• ASDF integration with shell and its effects on tool versions
• Dagger pipeline and its use of containers
• Handling Postgres upgrades and data migrations in the pipeline
• Consistency of tool versions across dev, test, and production environments
• Upgrading Elixir is straightforward, but upgrading Postgres requires data migration
• The tools versions file determines the Postgres SQL version at deployment time
• The current pipeline is not fully parallelized, causing long build times
• A recent change to the pipeline has reduced build times from 6-7 minutes to 2 minutes
• A future change will switch to the Fly Apps V2 Dagger Engine, which can start up quickly and stop when not in use
• The current pipeline is a starting point, but reusable pipeline fragments or components are desired
• There are still some issues with the pipeline, such as the lack of a component for running Elixir tests
• The pipeline is being iteratively improved with a focus on progress over perfection.
• The conversation is about improving deployment speed and efficiency of the changelog app
• Current deployment speed is 3-4 minutes, which is a significant improvement over the previous 8-9 minutes
• The team is discussing ways to further improve deployment speed, but acknowledges that achieving zero deployment time may not be possible
• Chasing zeros refers to aiming for a deployment time of zero, but the team recognizes that this is difficult due to factors like code compilation and instance spinning
• Clustering is identified as a necessary step to enable multiple instances of the app and improve deployment efficiency
• The conversation concludes with a discussion of the importance of clustering and the need to solve this problem to further improve deployment speed
• Plans to update changelog news' web pages for a better user experience
• Introduction of Honeycomb tracing and its benefits for monitoring speed changes
• Prototype from Losh Vickman for a clusterable caching solution
• New features in Honeycomb, including open AI integration and query assistant
• Discussion of the potential for Grafana and other tools to integrate similar features
• Generative AI is not a disruptor, but rather a tool that fine-tunes the useful experience of something
• Honeycomb and Sentry are developer tools that provide upgrades to make them more usable and useful
• Honeycomb's integration with app traces is a powerful feature, and a blog post by AJ Foster provides a good guide on how to do the integration
• Bard and ChatGPT are compared, with Bard having default access to the internet, but GPT-4 being considered better for certain tasks
• Bard has been found to be 100% inaccurate on Elixir code and has not improved with the new browsing feature.
• Kaizen event and pull requests
• Deploys per day between March 8th and May 20th
• ChatGPT accuracy in calculating deploys per day
• Commit process and batch deployment
• Comparison of commit and pull request process
• Leap year and date reference in ChatGPT question
• Discussion of leap year implications on day counts
• Ken Kost's contributions to W3C HTML validation fixes
• Possibility of integrating Tailwind with the app
• Challenges of handling contributions and open-source development
• Adapting to changing project direction and decision-making process
• Renaming the "Change All News" show
• Schema and visualization work for feed organization
• Adam and the speaker's differing opinions on project decisions
• Difficulty in getting the right product, price, and availability in software development
• Importance of considering user input and feedback in software development
• Example of the Homer Simpson car analogy for software development
• Discussion of Apps V2, a platform that uses nomad scheduling and has limitations
• Explanation of Apps V2's proprietary scheduling system and its benefits
• Mention of clustering and CDN to ensure availability of software
• Importance of considering machine versus Apps V2 considerations in software development
• Discussion of the challenges of building in public and taking user input
• Transparency and empathy in software development and its challenges
• Discussion of a past internet outage and how the company took a "day off" and walked in the park
• Comparison to the movie "Cable Guy" where a character's broadcast falls onto a dish, causing TV signals to fail
• Explanation of the impact of a Fastly outage on the internet
• Discussion of Apps V2 and its limitations, including the inability to schedule an app to run on another host if the primary host is unavailable
• Explanation of the benefits of clustering in Apps V2, including resilience and the ability to mitigate the impact of a single host failure
• Discussion of the company's current setup, including the use of Dagger Engine and PostgreSQL, and the need to cluster PostgreSQL for redundancy
• Proposal to explore managed PostgreSQL services, such as crunchy or super-based
• Discussion of the need to cluster apps in Apps V2 to ensure resilience and mitigate the impact of a single host failure
• Changelog infrastructure and its evolution
• Abandoning news items and simplifying content structure
• Single table inheritance (STI) concept and its use in the past
• Outdated code and potential for deletion
• Changes to content creation and publishing process
• Infrastructure built for outdated methods and potential for refactoring
• Legacy systems and their continued use in certain areas
• Code cleanup and elimination of unused features
• Transitioning from old system to new one
• Scheduling and sponsorship management
• Kaizen approach to incremental changes and improvement
• Commitment to consistency and avoiding sudden changes
• Discussion of shipping change log news and feedback from users
• Introduction of Kaizen, a podcast with a discussion thread on GitHub
• Explanation of the podcast's format and consistency
• Encouragement for user participation and feedback
• Shoutout to Jason Bosco for participating in Kaizen 10 and TypeSense
• Discussion of TypeSense and its fast in-memory search capabilities
• Mention of deleting Algolia code and cleaning up the codebase
• Changelog and new format for the show
• HomeLab material and upcoming topics (Unify, Ubiquity, VLANs, IoT)
• Importance of separate networks for kids and IoT devices
• Routers, networks, and ISPs for redundancy and failover
• Starlink and its costs as a backup option
• Metered use and failover capabilities
• Ubiquity (company) and Unify (product) discussion
• Desire for Wi-Fi Base Station XG for broadcasting Wi-Fi over a large area
• Discussion of the host's Wi-Fi setup for their land, including their desire for blanket coverage
• Review of Wi-Fi Base Station and alternative options, such as the AC Mesh Professional
• Comparison of Ubiquiti and Microtech wireless systems
• Microtech's features, including container support and a Linux-like operating system
• Discussion of the trade-off between polished UI and stability in network setup
• Recommendation to check out Microtech's YouTube channel for network-related content
• Brief discussion of future show topics, including Microtech and networking setup
• Improve integration with 1Password and secrets in GitHub actions
• Configure and better understand SLOs in Honeycomb
• Run Uptime Kuma locally and on Fly.io
• Upgrade to PostgreSQL and Apps v2
• Investigate Cloudflare for logging and integration with Honeycomb
• Consider switching to Cloudflare R2 for storage with zero egress fees
• Test and migrate to R2, addressing technical differences and hardcoded URLs
• Billing issue with a $130 increase from $30
• Discussion of migrating from Supercast to a first-party platform
• Clustering and caching setup requirements
• Customization of feeds for podcast members
• Managing subscriptions and email notifications
• Handling refunds and cancellations through Stripe integration
• Investigating an issue with multiple instances of a changelog
• Concerns about a second production sending emails or notifications
• Idea to call the current process a "Kaizen" or "changelog"
• Upcoming events:
  • WWDC keynote on Monday
  • Discussion of Apple announcements with homebrew lead maintainer Mike McQuaid
• Call to action: share the changelog with friends, leave feedback in comments, and tune in next time