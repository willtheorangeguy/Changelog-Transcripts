• Guest Alex Surachi (aka Vito) introduces his feature "rave mode" for Concourse CI and bass
• Rave mode synchronizes Spotify track beats with build output
• Sourcegraph's Code Insights product is featured, allowing teams to track versions of languages and packages
• Joel Cortler discusses the importance of tracking versions and how Code Insights simplifies this process
• Alex Surachi joins as a guest for the rest of the episode
• The background story of Concourse CI, which aimed to improve upon existing CI-CD systems like Jenkins
• The need for a more declarative approach, where users define what they want and the system figures it out
• Struggles with packaging data services (Cassandra, MySQL, Redis, RabbitMQ) for platform teams and developer teams
• Challenges with scaling, degrading gracefully, and delivering CVEs quickly enough
• Jenkins' shortcomings and how Concourse was a solution to its problems
• Personal anecdotes about Chris Brown, who co-founded Concourse with the speaker
• Coincidence that Temporal uses Concourse to deliver services, highlighting the connections between companies using Concourse.
• Concourse's pipeline view is considered one of the best in CI
• Initial concept was created by two individuals after hours at Pivotal
• UI evolved from GraphViz and manual JavaScript implementation
• Collection of pipelines was added later as an improvement
• Early design featured a "groove box-like" layout with bright colors
• Concourse's development progressed from a monolith to multiple pipelines, teams, and pipeline groups
• Biggest early challenge was managing onboarding pace and user adoption
• The difficulty of using Concourse, especially with its configuration and documentation
• Common pain points when working with Concourse, including acquiring and releasing environments
• Integrating Concourse with other tools and systems, such as Git and S3
• The concept of Concourse as a way to codify dependency chains and automation processes
• The idea that Concourse can empower users to get more done through automation and continuous delivery
• Features and capabilities of Concourse, including checks, logs, pipeline views, and resource state tracking
• Distribution mechanisms for large clusters
• Automation and health monitoring of complex systems
• Notifications and debugging tools
• Centralized dashboard or "source of truth" for system status
• Challenges with working from home during COVID-19 pandemic
• Notifying team members about system issues
• Concourse development experience, including team culture and rotation
• Lessons learned from Concourse development and the creation of base
• Critique of declarative systems and YAML configuration
• Declarative vs imperative programming in YAML
• Limitations of using YAML for expressing complex logic
• The need for templating in YAML and its associated problems
• Critique of declarative approaches to CICD and their underlying systems
• The issue with mapping declarative configurations to commands
• Potential drawbacks of adding an extra level of indirection between developers' intentions and actual execution
• Declarative things can be low-maintenance and work well for certain tasks
• Commands in a functional interface feel similar to functions with input and output
• Command-line interfaces (CLIs) can be treated like functional interfaces, where you identify a function call, pass parameters, and get outputs
• Base language's special sauce is its ability to handle results from commands easily
• Some programming languages, such as Erlang, are highly functional and promote thinking in terms of functions
• Functional programming is not always the best approach and can be "weird" at times
• Discussion of the Groovebox theme and its randomization
• Mention of Conqueror's previous color scheme changes and the inspiration for the Groovebox theme
• Resetting the Groovebox theme to allow it to change with each page load
• Introduction to Rose Pine, a theme with multiple variations (including light and dark modes)
• Discussion of the design concepts behind the themes and the use of thunks in the base language
• The conversation is about the design of a website and the use of functional programming languages
• Space Invaders was chosen as an icon to tie in with the color scheme
• The website displays echoes of commands with the same pattern
• The speaker has built other projects, including a static site engine called Booklet
• The speaker enjoys working with Lisp-like structures and languages that allow for building anything from a small set of primitives
• The speaker compares the appeal of Lisp to Go, citing their similar focus on simplicity and expressiveness
• Macro expansion and its relation to kernel
• Operative, a deferred evaluation mechanism used instead of macros
• Comparison with IO and implementation attempts in various languages (Haskell, Python)
• The story of John Shut, the creator of kernel, who passed away and had his ideas live on in base
• Optimizing kernel's performance due to eval after every operation
• Runtime interpreters as a bottleneck in language like base
• Runtime vs interpreter
• Continuation passing style and tail recursion
• Optimizing for infinite loops in continuous systems
• Difference between concourse and base
• Build kit interfacing with base (GRPC interface)
• Base loop component and its purpose
• Running base as a CI system
• Discussion about using AMD CPU for development and its inefficiencies in GitHub Actions
• Introduction of Base Loop, a server that receives GitHub web hooks and evaluates base code by calling out to the user's repository
• Explanation of the runner concept, which exposes local runtimes as a gRPC service
• Comparison between Base Loop and traditional CI/CD systems like Concourse workers
• Discussion on registering own GitHub runners and running them on demand using Kubernetes
• Mention of escaping YAML configuration in favor of lower-level abstractions
• The "ship it" file builds binaries for supported platforms (Linux, Darwin, Windows, ARM)
• It uses a script to reuse functions from the base and pass results into the ghrelease create command
• The script also publishes data representation of thunks in JSON format and SHA-256 hashes of files
• Hermetic data structures are discussed as being idempotent and accounting for every input that might change its result
• Concourse tried to enforce hermetic properties but was too overbearing, making supply chain security more difficult
• Having a reproducible build that can be trusted is essential for CICD, especially with the rise of supply chain security concerns
• Time drift or other variations do not impact the final artifact if it has no state and uses the same inputs.
• Thunks and timestamps
• Reference to Back to the Future in code
• Project called "base" with features such as "rave mode"
• New version of base being prepared for release
• Spotify API integration
• Feature called "rave mode" that syncs with music beats
• Discussion about a new or unfamiliar mode (metamode) and its cool features
• Mention of UPX, a binary compressor, and its use for compressing large binaries
• Explanation of the build process and dependencies required
• Introduction to the Spotify app and discussion about signing up for an account
• Installation and setup of the base software using Docker or Git
• Lima is a project that generalizes the need for developers to use Linux tools like Docker on Macs.
• Lima provides a template toolkit for spinning up VMs with software pre-installed, including build kit.
• The conversation involves testing and troubleshooting Lima's functionality, particularly syncing with another window.
• User registration and development mode are discussed as potential issues with Lima's implementation.
• Setting up Spotify API and authenticating with the user's account
• Running an infinite command in Base CLI and synchronizing it with Spotify
• Using "demos/fib-loop" command to test synchronization
• Adjusting timing using minus and plus keys when out of sync
• Displaying song information, BPMs, and colors matching the music
• Discussion about taking screenshots and adjusting settings for a show notes
• Conversation about shipping an app after confirming it works
• Explanation of the need to change the app's status from "developer" to another category
• Personal anecdote about being a user of the app and feeling special for experiencing its functionality before others
• Sponsorship announcements from Retool and Acuity
• Introduction to the co-founders of Acuity, Jesse Suen and Alexander Matrusenchev, and their platform's features and goals
• Explanation of Acuity's mission to provide a fully managed Argo CD solution and improve the GitOps and developer experience
• Discussion on shipping out a platform without configuration
• Issues with Intuit's previous experience in shipping out platforms
• Acuity.io and its closed beta status
• Attempting to ship out the platform with various technical issues
• Use of multiple cores and re-rendering UI components
• Introduction to Veto Base, an open-source platform
• Discussion on building great software through community contributions
• The importance of not taking oneself too seriously in software development
• Balancing fun and seriousness when dealing with mistakes and challenges
• Concourse's strong opinions and how they affected users who were forced to adopt it
• The importance of meeting people where they are, rather than imposing one's own opinions or patterns
• The value of simplicity and minimalism in software design
• Simple primitives vs complex systems
• Limiting the number of components and interfaces to reduce complexity
• Caching as a way to simplify systems and improve performance
• Base as a scripting language for caching commands and improving efficiency
• BuildKit's role in tracking dependencies between things and optimizing builds
• Discussion of caching strategies for distributed systems
• Importance of cache proximity to compute resources
• Trade-offs between cache placement and job distribution
• Use cases where cache proximity is crucial (e.g. CI/CD pipelines)
• Complexity of rebalancing mechanisms in distributed caches (e.g. hash ring algorithms)
• Difficulty in predicting cache performance due to varying build and transfer times
• Importance of identifying and reusing resources in tasks with hermetic aspects
• Experimentation with multi-layer caching for fine-grained control over task execution
• Potential for systems to learn from runtime data and optimize processes based on output size and duration
• Caching problem and its relation to machine learning
• Iterative process for finding an optimal solution
• Comparison to Conway's Game of Life and pattern recognition
• Stabilization of the caching system
• Recognition that the system is a form of machine learning in a basic sense
• Discussion of complexity and simplicity in understanding systems
• Clearing the cache
• Cache invalidation
• Most enjoyable aspect of working on base: building the language itself
• Reducing concepts to a minimum, leveraging them in interesting ways
• Using scopes as both data structure and scope in base code evaluation
• Overusing or misusing concepts may lead to "foot guns"
• Fitness function for determining progress towards goal is fun
• Difficulty in "gaming" the system and determining if progress towards a goal is being made
• Relationship between "nicks" and "base", specifically their language
• Value of "nicks" as a software package repository, citing its large size and up-to-date content
• Comparison with other systems such as Debian, highlighting nicks' uniqueness
• Missing dashboard for managing the repository
• Congratulations to DJ Daniel Jones on his first pull request to bass
• Mention of previous episode or timestamp
• Discussion of a technical issue involving disconnection while SSHing into a system
• Mention of Ryzen and KVM switch
• Exploration of repology.org and its package repository data
• Discussion of Nix packages and their representation on the site
• Explanation of how some software is automatically updated within a few days after release
• Discussing the need for a package manager that can give precise reproducible builds
• Mention of Nix OS and its capabilities on a Linux system
• Comparison between Nix and Debian, with preference for Nix's features
• Description of setting up Nix OS on an AMD Ryzen 7 workstation
• Issue with updating channels in Nix on Mac
• Discussion about using WSL (Windows Subsystem for Linux) to run Nix within Windows
• Clarification that the host operating system is actually Windows, not Mac
• Explanation of the setup: running Ubuntu with Nix as a package manager on top of Windows
• Building base system using Nix
• Concerns about Nix being a dependency of base, fearing it would add complexity for users
• Using Nix to build images for base, but keeping the two systems separate
• Experimenting with having base start a Nix host to simplify image building
• Wanting to leverage Nix's package management capabilities in building CI images
• The speaker uses Nixery.dev for demos and other tasks
• They discuss the benefits of using a local environment, specifically with Nixery.dev
• Docker Hub rate limits are mentioned as an issue
• The speaker's tests fail due to anonymous rate limit usage
• The conversation turns to waiting for a base build release
• Discussion about using nix3.dev for faster iteration
• Concerns about burdening Vincent with depending on it
• Idea of running nix3 locally to solve both problems
• Observations about CI failures related to images and registries
• Explanation that registries can be thought of as a type of cache
• Network transfer properties, including latency and packet loss
• Building declarative systems with Nix
• Episode 37 discussion on declarative systems
• Implementing version control in Nix OS
• Bass (a tool for building languages) similarities to Concourse
• Wrapping up the conversation and next steps
• bespoke abstractions and CLIs
• latest version of a program with "rave mode"
• connection to Spotify
• goal of keeping the experience fun and light
• hour-long recording process
• discussion on being nerds and enjoying the process
• Upcoming episodes will follow up on previous ones
• Guest Tamer Saleh, former VP of Engineering at Pivotal, will be featured in episode 32
• He shares the "two thumbs up" trick and tries out the Cool Wall of Cloud Native
• The guest's next appearance is mentioned but details are unclear due to audio cut off