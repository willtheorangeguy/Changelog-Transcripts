• Gerhard Lassou announces his departure from ShipIt after the current episode
• Embracing change is a key concept discussed, with constant change being inevitable
• Gerhard wants to focus on experimentation and smaller projects instead of rushing ShipIt episodes
• Dagger is mentioned as one of the areas that requires more attention and headspace for Gerhard
• The importance of knowing when to stop and rearrange priorities is emphasized
• A pause in ShipIt will allow for new ideas and improvements to be explored
• Future possibilities for ShipIt, including videos and guest episodes, are discussed
• Completion of 90 episodes and the upcoming hiatus
• Discussion on why 100 episodes would be a more natural ending point for the show
• Appreciation for the unique format and content of the Kaizen series
• Plans to continue the Kaizen series in some form, possibly on the Changelog or as a separate show
• Desire to maintain Gerhard's involvement with the platform and encourage experimentation
• Reflection on the origins and evolution of the Kaizen series within the Shibit show
• Discussing the highlights of progress and improvement in work
• Importance of knowing when to pause or quit projects to avoid burnout and regret
• Experimentation and flexibility in content creation, including video content on YouTube
• The challenge of maintaining a consistent schedule for a podcast
• Exploring new formats and ideas, such as "behind the scenes" or "deep dive" content
• Potential experimentation with the show's format and future
• Maintaining connection with listeners beyond the show, including social media platforms (Twitter, changelog social) and community tools (Slack, GitHub)
• Pause in podcasting until a new direction is determined
• Exploring alternative formats for episodes, potentially releasing them less frequently than once a week
• Reflecting on how the show's format was originally established through shipping and delivering content
• Going back to a more traditional infrastructure setup, improving partnerships
• Pausing the podcast "extra" and returning to normal episodes
• Discussing the Changelog++ membership program for supporting the work of Changelog
• Describing a major update to Dagger version 0.3, including migrating from CircleCI to GitHub Actions and introducing CI running locally first and remotely next through a thin interface called Dagger
• The release of SDKs for writing CI/CD pipelines in code (Python, Go, Node.js)
• Transition from Dagger 0.1 using Q to Go in the codebase
• Removal of YAML, Q, and makefiles
• Introduction of Mage, a task runner similar to Make or Rake, written in Go
• Creation of entry points for Dagger pipelines using Mage
• Building and publishing runtime image to GitHub Container Registry (GHCR) using Dagger 0.3
• Discussion of using Elixir 1.14.2 as a runtime image
• Explanation of Dagger engine provisioning inside Docker
• Introduction to function chaining for complex operations
• Demonstration of automating dependency management and build processes
• Comparison of new approach with previous manual steps
• Excitement about simplified process for bumping dependencies
• The conversation discusses updates to a project and how they affect various aspects of the system, including code, images, pipelines, and deployment.
• A change was made to allow running the code base on GitHub Code Spaces using a dev container.json file.
• This update includes a Docker compose file and some JSON, making it easy to open in Code Spaces.
• The integration with Code Spaces allows for faster development and testing.
• Future plans include templating and automating updates across multiple places in the system.
• The speaker describes Dagger as cutting edge and state-of-the-art technology for Continuous Integration and Continuous Deployment (CICD).
• Dagger allows users to spin up containers in code, making it easier to manage CICD processes.
• The introduction of services support in Dagger enables the use of external services such as PostgreSQL within the tool, simplifying workflows.
• The speaker is excited about the advancements in Dagger and sees it as a "poster child" for the technology.
• The conversation touches on the importance of maintaining up-to-date documentation, particularly with automated release processes.
• PRs and branches deployment
• Running tests for every pull request using Docker engine in GitHub Actions
• Deployment previews
• Services support in Dagger
• Routing and running a lightweight changelog in CI/CD
• Previewing the changelog in CI/CD during a pull request
• Infrastructure MD diagram update
• Rotating all company secrets
• Migration from LastPass to 1Password
• Key rotation and updating API keys for various services (Slack, Campaign Monitor, GitHub)
• Issues with AWS credentials and stat system downtime
• Issue 442: cleaning up 79 tasks related to secret management
• Discovery of numerous service integrations (e.g. Slack, GitHub, Fastly) and API tokens
• Plan to swap out Algolia for TypeSense search engine
• Implementing a clustered world with multiple nodes running apps without changing Erlang's caching system
• Evaluating the need for caching and considering pre-computation of expensive pages (specifically feeds) instead
• Solving issues with Overcast ping due to caching conflicts
• Considering Postgres as an alternative cache store, which resulted in consistent 50 millisecond responses in initial testing
• The desire to test this solution in production, but lacking necessary metrics and observability tools
• Discussing a project to integrate something that was previously experimented with
• Jared's experience and confidence in making the integration work
• Need to test the integration in production, possibly using feature flags or 50/50 split
• Introducing feature flags as a possible solution for testing and deployment
• Alternative solutions such as an if statement with random number generator
• Discussion of implementation and deployment options
• Finding a use for an unused system
• Limited development on the system due to lack of demand
• Relationship with Darkloos (formerly friendly but no longer directly collaborating)
• New sponsorship from DevCycle and potential opportunity for feature flag use
• Observability issues, including log file problems and inability to see results
• Discussion about a recent commit and mistake made in code changes
• Discussion of an issue with production where a line was removed, causing telemetry to drop off
• Mention of the Honeycomb integration and its use of the open telemetry plug
• Explanation of an overaggressive deletion in code review that caused an honest mistake
• Review of a PR and realization that it wasn't reviewed thoroughly enough before merging
• Discussion of an experiment going into production and its potential success with a Postgres feature
• Explanation of how a successful experiment would serve live requests from Postgres, reducing latency
• Mention of the ability to run multiple instances of changelog due to solved caching issues
• Serving different feeds to different requesters (e.g. Spotify)
• Using Postgres to store pre-computed text for chapters
• Potential issues with large data storage in Postgres (2.3 megabytes)
• Benefits of using Fly's global proxy and caching capabilities
• Reducing reliance on CDN and distributing apps around the world
• Moving changelog.com behind a CDN due to single instance issues
• Bringing app closer to users with Fastly, making it easier to code and troubleshoot
• The speaker mentions that their app's data center is in Virginia (IAD) and not locally hosted.
• They discuss the challenges of getting data to users and propose caching on write instead of read to reduce latency.
• The speaker suggests using a PostgreSQL as a service, specifically Crunchy Data, for database management at a global scale.
• They mention that their app runs on Fly, but the database is currently managed in-house.
• The speaker emphasizes the importance of scaling both the app and the database together.
• Discussion about the limitations of PostgreSQL when used across continents due to reading large amounts of data
• Idea of using multiple PostgreSQL read replicas in Fly to improve performance
• Mention of alternative database services such as PlanetScale and Superbase
• Conversation about not having enough time to experiment with different approaches
• Discussion about Jared's preference for vanilla PostgreSQL and the creation of a "Just Postgres" t-shirt design
• Plan to double down on improving PostgreSQL functionality
• Next episode of Kaizen
• Publishing on changelog feed vs. Shippet feed
• Upcoming episodes (90, 91, 92, potentially skipping 93-99)
• Fahrenheit and Celsius temperature discussion
• 1Password integration and secrets management
• Request for 1Password contact to test beta feature
• Discussion of biometric logging and passwordless systems
• Mention of a blog post on the 1Password blog about PassKeys
• Plans to implement passwordless authentication in Ship It episodes
• Personal discussion, including birthdays and family involvement
• Recap and closing remarks, including announcements for future episodes
• Wrap-up of the guests
• Positive sentiment towards the experience
• Goodbye and farewell message
• Repetition of "Game on"