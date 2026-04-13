• Discussion of Prometheus contributors and their backgrounds
• Overview of Prometheus's growth and adoption
• Graduation of Prometheus from CNCF and its impact on the project
• PromCon conference and its evolution
• OpenMetrics and its role as a standard for metrics
• Relationship between OpenMetrics and OpenTelemetry
• Standard instrumentation library for tracing, metrics, and logging
• Importance of a stable, long-term transport format for metrics (OpenMetrics)
• Role of Loki in event logging and its potential to combine with Prometheus
• Promoting layering approach to observability, separating tools for different use cases
• Prometheus growth and evolution, particularly in the last six months
• Prometheus's focus on core metrics and server, with expansion in connected projects and vendors
• Remote write interface and its improvements, including write-ahead-log and persistent on-disk buffer
• The functionality of a Prometheus feature hasn't changed, but its implementation has improved in robustness.
• Importance of the core Prometheus being robust, performant, and dependable for supporting extensions and growth.
• Discussion of the remote read feature, which is still experimental, and its potential impact on memory usage.
• The problem with remote read was decompressing and serializing data, which wasted bandwidth.
• The improvement of remote read through streaming data, reusing Prometheus's block format.
• Thanos's use of the improved remote read feature for data retrieval.
• The growing need for remote write and read due to users' growing beyond a single Prometheus server's capacity.
• The importance of regular releases, with a strict six-week cadence, to keep up with growing needs and monitor regressions.
• The benefits of regular releases, including controlled benchmarking and user feedback.
• The consistency and predictability of regular releases, allowing users and maintainers to plan and contribute.
• Counters for download and Docker image pulls
• GitHub download counters
• Phone-home mechanism into Prometheus
• Grafana tracking and metrics
• Deprecation and support for older versions
• Upgrades and compatibility between major versions
• Unit testing of alerting rules
• Roadmap and future developments, including a new UI for the Prometheus server and support for Language Server Protocol (LSP)
• Adding a user interface to Prometheus to display metric names, extended help information, and explicit types
• Utilizing help strings and metadata API to provide additional context to metrics
• Introducing a new React-based UI to make the project more accessible and attract new contributors
• Discussing the decision-making process behind switching to a new UI framework (React) and the importance of letting passionate individuals drive change
• Mentioning ongoing efforts to improve Prometheus' memory usage, including exploring offloading mechanisms and new data compression techniques
• Chunk encoding for Prometheus data storage
• Potential for optimizing data at runtime or compaction time
• Comparison of Prometheus 1 and 2 storage engines
• CPU vs memory usage in Prometheus servers
• Optimization of compression to reclaim memory
• Histograms in Prometheus, their importance, and current limitations
• Plans to improve histograms to be more detailed and less expensive
• Openness and community involvement in Prometheus development
• Monthly public meetings and community calls for Prometheus developers and users
• The definition of observability and how it has evolved beyond the traditional metrics, logs, and traces framework
• The importance of using data to tell a story and the focus on what needs to be conveyed
• A personal anecdote about using Grafana tooling to diagnose an issue with a hosted service
• The role of logs in root cause analysis and the importance of considering different elements of observability
• The integration of tools like Zipkin and Jaeger with Prometheus and the use of Jaeger for request-centric logging
• The difference between tracing tools and logging tools and the focus of Loki on developer-centric logging
• Discussion of an unofficial logo for Grafana being a cuttlefish
• Comparison of different data sources and databases supported by Grafana (ELK, Stackdriver, Prometheus, etc.)
• Integration of Loki with Grafana, allowing for automatic switching between metrics and logs
• Explanation of Loki's metadata-only indexing approach and its benefits
• Discussion of Loki's focus on providing a simple, easy-to-use experience for log analysis
• Comparison of Loki with other projects (Elastic, Lucene, etc.) and its approach to building focused, user-centered tools
• The importance of staying focused on a specific use case or story when building a project
• Challenges of resistance to change and scope creep in software development
• Code reuse and reusing data structures from previous projects
• Importance of authenticity and telling real stories in business and product development
• Overview of the Prometheus project and its limitations
• Background and development of the Cortex project, including its relation to Prometheus and Grafana Labs
• Comparison between Cortex and Thanos, including their approaches and similarities
• Potential for Cortex and Thanos to merge and combine efforts
• Query performance improvements and acceleration in the Cortex project
• Collaboration between Thanos, Prometheus, and Cortex projects
• Importance of community and openness in the Kubernetes and cloud-native ecosystem
• Development and benefits of the Tanka project, a reimplementation of Ksonnet
• Low barrier to entry for contributors and users in the Kubernetes community
• Value of shared code and libraries between Thanos, Prometheus, and Cortex
• Potential for further collaboration and possible merger between Thanos and Cortex, but not as a priority
• Experiences and impressions of KubeCon, including community engagement and developer enthusiasm
• Discussion of KubeCon and its growing popularity
• Importance of open source technology, specifically Prometheus
• Welcoming and inclusive nature of the Kubernetes community
• Benefits of a strong and collaborative community for project success
• Open source's shift from being exclusive to being inclusive and accessible to all
• Opening a pull request and getting it accepted
• Importance of being welcoming and inclusive in open-source communities
• Success of the CNCF community and its growth
• Crossplane as an example of a project that levels the playing field and provides open access to cloud providers
• Stacks in Crossplane and how they extend the Kubernetes API with knowledge of cloud provider resources
• Abstractions in Crossplane and how they allow for easy access to infrastructure resources
• Higher-level building blocks in Crossplane for applications, such as application templates or blueprints
• Layers of functionality in Crossplane, starting with low-level building blocks and building up to higher-level abstractions.
• Kubernetes API standardization for integration with various infrastructure resources
• Crossplane bundling of infrastructure and application stacks into custom resources
• Dynamic provisioning of Kubernetes clusters with preinstalled resources
• Philosophy of treating everything as a resource in Kubernetes
• Rook as an orchestrator for storage, focusing on persistent storage within Kubernetes clusters
• Rook's design and separation of layers, including the core orchestration layer and the management layer
• Rook performs storage orchestration in Kubernetes clusters and supports various storage providers, including LVM.
• Crossplane supports various cloud providers, including AWS, GCP, and Azure, and has a process for other providers to integrate with it.
• Crossplane's design patterns and best practices have been abstracted out into libraries and libraries, making it easier for new providers to integrate.
• Packet is an example of a provider that has integrated with Crossplane, providing a stack for dynamically provisioning and integrating with Crossplane.
• Crossplane's abstraction allows for portability across different cloud providers and enables users to create claims for resources, such as MySQL instances, that can be reconciled to different cloud providers.
• The Crossplane Runtime library provides an interface for building controllers and running them in a Kubernetes cluster, and abstracts out common patterns for interacting with external APIs.
• Crossplane has been used to deploy GitLab, a higher-level application, in a portable way across different cloud providers.
• There is a discussion about the possibility of having a Crossplane instance that manages other Crossplane instances and applications, and reconciles less frequently.
• Discussion of managing Crossplane instances as a service, automating effort, and utilizing controllers to achieve this
• Future plans for scheduling in Kubernetes, including dynamic resolution of abstract types and scheduling based on cost, region, locality, and affinity
• Expanding the idea of scheduling to a global scale, leveraging the control plane to make smart decisions
• TBS (The Binding Status) YouTube livestreams, including informal discussion, live demoing, and community engagement
• The importance of community building and user feedback in shaping the Crossplane platform
• Risks of engaging with Crossplane content due to its exciting and entertaining nature
• Solutions to encourage trying out Crossplane, including hosting a show and being forced to use it
• Ease of trying out Crossplane with Helm-install and documentation
• Importance of feedback from new users with fresh perspectives
• Plans to try out Crossplane for the first time on the show