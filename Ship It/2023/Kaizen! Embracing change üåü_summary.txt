• Gerhard Lazu is leaving Ship It after 90 episodes
• The decision is due to burnout and needing headspace for other projects
• Change is constant and embracing it is key to moving forward
• Gerhard wants to focus on experimentation and improvement in the future
• The possibility of reviving Kaizen-style shows or podcasts in some form is discussed
• Discussing a podcast's new format and infrastructure
• Reflecting on past shows and their successes
• The importance of knowing when to pause or quit projects
• Experimentation with video content and GitHub discussions
• Changes in the podcast's schedule and future plans
• Keeping up with the hosts' online presence (Twitter, Changelog Slack, etc.)
• Exploring ways for listeners to stay connected with the hosts
• Regressing to the original podcast format and schedule
• Pausing continuous podcast delivery to focus on improving infrastructure and developing partnerships
• Improving CI/CD workflows with Dagger, a code-based pipeline management system
• Migrating from Circle CI to GitHub Actions using Dagger
• Releasing SDKs for writing CI/CD systems in code (Python, Go, Node.js)
• Eliminating YAML, CUE, and makefiles in favor of Go code and mage files
• Dagger v0.1 released, replacing old pipeline
• Introduction of namespace runtime "image"
• Building and publishing Changelog runtime image to GitHub Container Registry (GHCR) using Dagger v0.3
• New features for building and publishing images with various dependencies (e.g. Elixir, Node.js)
• Automated caching and reusing of dependencies to speed up build process
• Ability to easily update dependencies by changing a single string in code
• Pipeline will automatically update dependent files (e.g. README) when dependency is bumped
• The host company's codebase can be run on GitHub Codespaces using a devcontainer.json file
• Chris made a pull request allowing the codebase to be run on Codespaces, and Gerhard followed up with another PR that references an already built runtime image from GHCR for faster performance
• Dagger is being used to redefine CI/CD as code, making it possible to orchestrate containers in code rather than using scripting or YAML
• The company is one of the first to use Dagger's services support feature, which allows spinning up a PostgreSQL container for tests inside the Dagger engine
• The company deploys every push to master as a release and runs tests on pull requests
• Implementing GitHub Actions to run tests for every pull request
• Leveraging Docker engine for CI/CD tasks, including building and running longer-running environments for deployment previews
• Exploring Dagger services support for longer-running processes in CI/CD
• Rotating secrets and integrating 1Password as a team
• Addressing the LastPass leak and migrating to 1Password
• Key rotation and updating API keys for various integrations (Slack, Campaign Monitor, etc.)
• Discussing improvements to infrastructure documentation and diagrams
• Replacing Algolia with Typesense as search index
• Exploring alternative caching solutions due to performance issues with Erlang caching system
• Using Postgres as a cache for pre-computed feeds and serving them as static content
• Integrating Phoenix with Honeycomb for observability and metrics
• Planning to test the new caching solution in production
• Discussion of using feature flags for testing a new implementation
• Proposals to test the new implementation on a limited set of users (50/50 split)
• Alternatives to feature flags (simple if statement with random selection)
• Observability and logging issues, including a recent change that caused log files to stop logging
• Explanation of how telemetry plug disables logging in production
• Discussion of using Honeycomb for observability
• OpenTelemetry plug-in integration
• Review and merging process discussion
• Changelog experiment production results: serving live feeds from Postgres cache
• Enabling multiple instances of Changelog and global distribution
• Serving different feeds to different requesters (e.g. Spotify)
• Precomputed text storage limitations in Postgres
• Fly's role in reducing reliance on CDN and enabling distributed apps
• Technical difficulties with understanding and troubleshooting cache issues
• Using Fastly to create a dynamic app close to users, but complexities and challenges
• Embodiment of the Fly vision and overcoming cache limitations
• Cache experiment results and implications on app performance
• Discussion on caching on write vs. read and potential solutions
• PostgreSQL as a service (e.g., Crunchy Data or Supabase) for scalability and management
• Trade-offs between managed databases and self-hosted options
• Plans for the next Kaizen episode and publication on the Changelog feed
• Discussion of a business plan to turn Postgres into dollars
• Efforts to use 1Password secrets programmatically in CI systems without running the Connect server
• Consideration of migration from 1Password or using an alternative secret management solution
• Review of passwordless systems, including 1Password's "Pass keys" feature
• Adam Stacoviak teases Jerod Santo about singing a song poorly on a previous episode
• Gerhard Lazu announces he will take time off from recording Ship It episodes and go to Dan-Tan instead
• The group discusses and jokes about the idea of going to Dan-Tan every week
• They discuss future plans for the podcast, with an upcoming episode in 2.5 months