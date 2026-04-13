• Discussion on Lars Wikman's unchanged operational setup since June 2021
• Recap of past episode "Why Kubernetes" and the follow-up with Gerhard Lazu
• Lars' nuanced feelings about Kubernetes, considering its complexity and mystery
• Current take on Kubernetes landscape and cloud-native technologies
• Comparison of various tools and platforms, including k3s, ArgoCD, and Fly
• Exploration of production setup, including operating system, packages, CI/CD, and server choices
• Lars' experience with client projects using Fly and GitLab for platform engineering
• Discussion on the trade-offs between layering and packaging deployment aspects into the app itself
• The simplicity of certain programming languages like Go and Elixir in handling load and scaling
• Challenges with Node.js in terms of scaling and CPU-bound loads
• Comparison of programming languages for machine learning and AI tasks
• Deployment artifacts and strategies, including use of containers and SCP (Secure Copy Protocol)
• Importance of knowing which hash is being pushed to production environments
• Backup strategy and disaster recovery
• Monitoring and alerting for production environments
• Blue/green deployment on single machines with minimal setup
• Orchestrating releases with CI/CD pipelines and artifact management
• Hot code reloading and upgrading running versions of the application
• Balancing monolithic architecture with operational concerns
• Discussion on running a monolithic architecture with external systems interacting with it
• Importance of simplicity in deployment and operations for smaller teams and organizations
• Concerns about choosing Kubernetes or other widely-used tools as they may not provide a competitive advantage
• The value of taking chances and making decisions that go against common practices, such as Apple's approach to shipping half-finished features
• Personal experiences with tooling and deployment methods, including using Fly.io for cloud deployments
• Considering bare metal or dedicated servers over cloud-native options for certain projects
• Exploring the idea of building a system without persistent data storage for an art project, using Erlang hot code updates
• Hot code updates and their challenges
• Trade-offs between automation and manual configuration
• Importance of clear documentation for system setup and operation
• Balancing complexity with maintainability and understandability
• Staying within one's comfort zone and familiar ecosystem
• Challenges of deploying systems in different programming languages
• Discussion of Dagger and its potential benefits for building SDKs in various languages
• Elixir as a preferred language for CI/CD tooling and its limitations when used with YAML
• Kubernetes and its complexities, including the need to reconcile declarative systems with operational requirements
• Preference for using Linux due to comfort and familiarity, but acknowledging that other systems (e.g. BSDs) may have advantages in certain areas
• Discussion of systemd as a complex system that can be difficult to use effectively
• Mention of exploring new tools and technologies, including the use of non-Linux operating systems (e.g. FreeBSD)
• Introduction of DCH Dave Cottlehuber, an expert in operational systems who works with FreeBSD and has experience with CouchDB.
• The danger of going off the beaten path with technology and tools
• The example of NixOS, PureScript, Haskell, OCaml, and other niche programming languages/systems
• The importance of not over-introducing new technology at once
• The need to balance challenging oneself with the potential risks of incompatibility