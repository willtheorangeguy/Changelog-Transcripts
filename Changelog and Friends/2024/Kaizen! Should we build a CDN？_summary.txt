• Recap of the hosts' return to the podcast after a break
• Discussion of a unique way of saying "cheers" in Adam and Jared's style
• Chicago meetup and potential pictures of the hosts' antics
• Fly.io infrastructure versioning and continuous improvement
• Kaizen process and versioning of the changelog app
• Complaint about an outdated subdirectory in the codebase
• Defense of the decision to version the "fly" folder by year
• Explanation of the new "flooded io" directory and app organization
• Clarification of the relationship between apps, machines, and the directory structure
• Multiple apps running at the same time on change.org
• Plans to achieve a big goal for change.org in 2024
• Creating a new project in the content space combining audio, video, and AI
• Wanting to start something big but not finish it, instead tracking progress over decades
• Adam's goal to get plus plus in-house, not on supercast
• Mention of a previous project, rabbitmq videos, and the goal of making a smaller project that can grow over time
• Discussing the idea of creating a job board to sustain podcasts and provide value to the community
• Exploring the concept of changelog.jobs, a subscription-based job board with a unique economic footprint
• Considering the potential for a job board to be a revenue driver and a way to support the community
• Reflecting on the importance of building software and teams in a way that aligns with the changelog community's values
• Addressing the challenge of balancing perfection with progress and the importance of taking action to achieve goals
• Discussing the potential for the job board to be a valuable resource for the community and a way to support shows like Go Time
• The speaker has had a change of heart about a certain idea, now seeing it as "true value" rather than a "bolt-on money maker"
• Changelog plus plus 2.0 is being discussed, with the speaker wanting to bring it on-site and improve it
• The speaker wants to "embed" certain elements into shows and swap them out dynamically
• Vetting and providing value to users is discussed, with the speaker wanting to do a good job on vetting users and provide value in return
• The conversation shifts to changelog plus plus, with the speaker and others wanting to bring it on-site and improve it
• A guest, Ross of Buka DJ, joins to discuss the problem of security concerns in open source dependencies and how Socket solves these problems
• Ross explains that Socket analyzes dependencies, detecting vulnerabilities and malware, and brings this information to the developer at the moment of choosing a package
• The install process for Socket is discussed, with Ross stating it's "super easy"
• The speaker's company built Socket to solve security and alert issues with other security tools.
• Socket is a developer-friendly tool with integrations like a CLI, GitHub app, and API.
• The majority of users install Socket through the GitHub app, which provides fast and accurate analysis of dependencies.
• The company is migrating from Postgres on Fly.io to Neon.tech, a managed Postgres alternative.
• The migration process involves upgrading Postgres from 15 to 16 and changing the app instance configuration.
• The speaker and team discussed the migration process with the Neon.tech team and CTO, including Kurt Mackie and Nikita Sham.
• The decision to switch to Neon.tech was driven by a desire for a future-focused, managed Postgres solution.
• Serverless managed Postgres and plans to expand to geo
• Bringing dev mode to Neon and Postgres, allowing for experimentation without cloning production databases
• Using branches of production databases for development, similar to Planet Scale's Vitess concept
• Concerns about slower query times, but willingness to try the new dev mode approach
• Need for fresh data in development, and how the new approach could simplify this process
• Concerns about contributors and access to production data, and the need to provide sanitized and reduced data for contributors
• Discussion about the potential issue with latency due to remote Postgres in Neon
• Exploring the idea of creating a sanitized branch to allow contributors to work with a stable database
• Mention of a SQL script to sanitize and reduce the production database
• Comparison of database query latency in Fly vs Neon
• Optimizing database queries to reduce the number of queries and improve performance
• Discussion of reducing network latency between Fly and Neon
• Mention of using read replicas to improve database performance
• Network latency and its impact on SQL statements and queries
• Connection pooling and other methods to reduce per-query cost
• The concept of "kaizen" and iteratively improving the speed of light
• Read replicas and their potential to reduce latency
• Fastly CDN issues, including a significant increase in cache misses
• Possible solutions, including deploying nginx instances worldwide with local disks for caching
• Discussion of challenges with Fastly and the need for a CDN
• Option to build own CDN vs. partnering with a company like Cloudflare
• Importance of integrated embedded partners for deep relationship and conversation
• Criticism of Fastly's lack of support and desire to work with Cloudflare
• Analysis of what it takes to build a CDN for a company like theirs
• Consideration of whether a small operation like theirs should build its own CDN
• Comparison of needs with big companies and the simplicity required for their operation
• The organization's use of fly.io as a service
• fly.io's improvements and benefits
• Issues with fly.io, including intermittent connection issues and wireguard gateway problems
• Comparison to other services, such as fastly and cloudflare
• Plans to build a custom CDN and the associated challenges and responsibilities
• The process of deploying a custom CDN on fly.io, including distributing applications across regions and setting up local ephemeral caching
• Discussion of log management and distribution for the 3383.32-3394.94 application
• Use of NATS for log distribution and its limitations
• Concerns about reliable log delivery from NGINX instances to S3
• Introduction to Vector.dev, an open-source tool for log processing and distribution
• Consideration of costs and pricing for using Fly vs. Fastly
• Idea to create a simple CDN using Fly and open-source tools, based on the team's current setup
• Alternative CDN solutions, including Varnish and NGINX, and potential for using existing configurations
• Concerns about complexity and the need for a simple CDN solution
• Discussing Varnish Cache vs NGINX and the challenges of using Varnish
• Comparing Varnish and NGINX configurations and experiences
• Considering the idea of building a CDN and the potential benefits and drawbacks
• Evaluating Cloudflare as a potential partner for building a CDN
• Exploring the possibility of "tinkering" with the existing CDN setup to test new ideas
• Discussing the potential risks and benefits of building a CDN in-house vs partnering with a CDN provider
• Proposing a "poor man's" approach to testing new CDN ideas with minimal risk
• Reviewing the features and requirements of Cloudflare's enterprise plan
• Discussing difficulties with accessing specific Cloudflare features
• Exploring the potential use of Cloudflare's log push service
• Considering alternative CDNs, such as Fly
• Evaluating the cost and feasibility of implementing a new CDN
• Discussing the importance of serverless Postgres and participating in the software development lifecycle
• Introducing Neon's managed Postgres serverless offering and its proprietary technology supporting branch-based deployment
• Mentioning the benefits of supporting branches for a modern deployment to production
• Benefits of serverless development environments, including cost savings and ability to create multiple copies of production databases
• Features of neon, including data branching and on-demand scalability
• Partnership between Superbase and fly.io for managed Postgres database
• Discussion of potential future investment by fly.io in a CDN
• Mention of Key CDN as a possible option for a CDN service
• The speaker discusses a personal experience of getting stuck in a cycle of frustration and eventually deciding to build their own solution.
• The speaker mentions that Vercel Postgres is powered by Neon, which they think is an unusual revelation and potentially an advertisement.
• The speaker raises the possibility of Neon being acquired by Vercel due to Vercel's history of acquisitions and mentions the idea of Neon Postgres being integrated with Fly.
• The speaker wonders if the acquisition of Neon by Vercel is a possibility and discusses the potential benefits of having a more integrated solution with reduced latency.
• The concept of choice in development and the paradox of choice in the green scheme
• Overwhelming number of options and standards, leading to indecision and inaction
• Release of an open source CDN and the resulting increase in standards
• A "hidden" feature or Easter egg snuck into a pull request
• Discussion of an auto-scaling slider in Neon and its counterintuitive behavior
• Integration with 1Password for secure secrets and application access
• Explanation of a single secret token and its usage in boot time
• Clarification on the hosting of 1Password cloud and infrastructure requirements
• The app loads secrets from 1Password into its memory
• Secrets are configured in 1Password, not in Fly
• Updating secrets in 1Password restarts the app, which then loads the new secrets
• The possibility of using a webhook or trigger from 1Password Vault to automate the process
• Limitations of the current system, including a barrier to the touch point of secrets
• The potential for a future feature to automatically rotate secrets in 1Password if a leak occurs
• Collaboration with 1Password to make the embedded partnership more apparent
• The speaker mentions that they are being paid for a tech, and this payment is the reason they are not promoting it, but rather because they love the tech.
• The speaker mentions that they are pursuing a relationship with the company that provides the tech, where they can share the story of how they are using it.
• The company provides a web hook, which allows the speaker to integrate the tech into their system.
• The speaker discusses their use of One Password, a tech that allows them to securely store and access sensitive information.
• The speaker mentions that they are considering a One Password sponsorship, as they are already using and improving the tech in their infrastructure.
• The speaker discusses the process of integrating One Password into their system, including the use of a token and a CLI to load secrets directly from One Password.
• The speaker also mentions that they are using a file called env.op to store secrets for development purposes.
• The speaker discusses the possibility of using One Password in development environments, and mentions that running the One Password command locally is an option.
• Discussion of env.op file and its potential changes
• Concerns about setup and secrets being affected by changes
• Confirmation that setup can remain as is
• Additional configuration for production
• CDN build debate and decision to "tinker" with it
• Merging of Neon techs and plans for production
• Discussion of Elixir configuration issues and workaround
• Plans for switching to Neon.tech for shipping
• Discussion of website latency and the role of Fastly in serving requests
• Introduction to the Changelog's Kaizen series and invitation to revisit past episodes
• Announcement of the return of the Ship It podcast, with a new host
• Promotion of Changelog Plus Plus membership, offering ad-free content, stickers, and discounts on merchandise
• Upcoming episode schedule, featuring news, interviews, and a discussion on the state of the home lab
• Potential audience for a project
• Upcoming conversation next week
• Changelog and updates
• Home lab setup
• Exclusive content and challenges
• Involvement of friends and community
• Show and game elements
• Business and marketing