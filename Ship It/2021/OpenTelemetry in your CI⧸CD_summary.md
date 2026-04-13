• Introduction to Ship It podcast and its focus on code, ops, infrastructure, and people
• Guests Cyril Leclerc (Product Manager at Elastic) and Oleg Dinashev (Principal Engineer at Cloudbeast)
• Akihiro Kiuchi's project on Jenkins Monitoring with OpenTelemetry in the context of Google's Summer of Code
• Importance of open telemetry in CI environments for visibility, monitoring, and cost-effectiveness
• Discussion of tracing agents, not just the Jenkins master, to gain visibility into job execution and agent availability
• Breakdown of job duration and tracking time spent on build allocation
• Visibility in CI/CD steps and allocation of build agents was limited
• AkiHero aimed to complement existing traces with detailed visibility on agent allocation and communication
• Importance of open telemetry in CI/CD systems for unified observability
• Blurred lines between CI and CD, with other automation use cases needing accessibility
• Open telemetry helps glue information from multiple tools in CI/CD pipelines
• Need for data to verify pipeline performance and security in audit and supply chain security
• Data structure for modeling CI and CD pipelines
• Exposing data of CD processes as a goldmine for troubleshooting and maintenance
• Benefits of sizing platforms and shortening build cycles
• Interest in cost accounting, process optimization, and digital transformation
• Capturing data on distributed traces using open telemetry
• Unified view of CI and CD processes
• Debate over standardizing tools or implementing different ones
• Distributed trace culture providing overall visibility across phases
• Dimensions of data collection and culture of abstraction
• Requirements for a good CI-CD system with open telemetry integration
• Perfect flow of a system with good open telemetry in the software development pipeline
• Steps involved in processing code, including invocation of external services and tools like Maven or Gradle
• Need for observability at each level of the pipeline
• Distributed tracing and passing context through levels of systems
• Understanding the beginning of a pipeline and its end result
• Debate on whether deployment should be the last step in a CI or CD pipeline
• Importance of reporting, post-processing, and accounting work after deployment
• Use of external tools for various tasks in the pipeline
• Discussion of instrumenting pipelines with Jenkins, Maven, and Ansible
• Need to understand what spans to capture during pipeline execution to measure time taken for specific steps.
• Understanding the importance of attribute extraction from pipeline execution
• Capturing relevant attributes for troubleshooting and use cases
• Associating attributes with teams for cost accounting and performance analysis
• Using stages (CI build, QA, security) to group pipeline constructs for organizational grouping and data usefulness
• Attributes for velocity and team performance in software delivery process
• Inviting entire listener base to move latency sensitive workloads to the edge with compute at edge free for three months and up to $100,000 in credit
• Overview of Fastly's edge cloud network and modern approach to serverless computing
• Benefits of deploying complex logic at the edge, including unparalleled security, blazing fast computational speed, and real-time observability
• Calculation or "spans" being worked out incorrectly when it comes to job allocation in agents, and how open telemetry can help CICD administrators solve this problem
• Role of open telemetry in helping CICD administrators, who may be a shared role among many people
• Security scanners and deployment
• Complicated systems and scalability problems
• CI/CD pipeline maintenance and troubleshooting difficulties
• Limited observability of data in distributed systems
• Need for assistance to quickly understand problem impact and scope
• Importance of observability for slicing and dicing data in any dimension
• Docker registry issues and their impact on CI/CD administrators
• Provision of tools to help notify CI/CD administrators early of problems
• Observability and its benefits in microservices architecture
• Automated anomaly detection through machine learning and statistics
• Benefits of observability for CI/CD administrators
• Comparison of modern CI/CD systems as a mesh of asynchronous processes
• Complexity of pipeline dependencies and interactions
• Agent provisioning and synchronization issues
• Caching in CI/CD systems and its impact on pipeline performance
• Difficulty in tracing events and understanding pipeline flow
• Managing outages and issues across multiple pipelines
• Difficulty in caching system interaction
• Complexity of pipeline systems and debugging challenges
• Importance of caching for reducing costs
• Simplifying complex systems for better throughput
• Visibility and monitoring of cicd pipelines
• Divergence between dev and ops teams' goals (stability vs. new features)
• Need for observability to build confidence in change
• Flaky tests in distributed systems
• Challenges with testing distributed systems, including race conditions
• Open Telemetry's potential to help with flaky tests
• Existing solution for Go test using Open Telemetry
• Opportunity to create a backbone for unit test results through Open Telemetry channels
• Potential for dev/ops team to implement their own tool to process and share flaky test reports
• Community-driven open source solution leveraging the flexibility of Open Telemetry
• Expecting an emerging standard for open telemetry in CI/CD systems
• Currently, almost no tools have built-in serial open telemetry instrumentation
• Jenkins and Concourse CI are two platforms that provide native open telemetry instrumentation
• Integrating open telemetry in Jenkins requires installing the Jenkins Open Telemetry plugin and connecting to an open telemetry endpoint backend (e.g. Elastic or Jaeger)
• Auto CLI from Equinix Labs can be used to collect open telemetry data for systems without built-in support
• Capturing health metrics and tracing pipeline execution using open telemetry
• Two initiatives that came to mind for instrumenting CI/CD pipelines were using Honeycomb's small cli tool and Hotel CLI as a wrapper.
• Hotel CLI can be used with tools like GitHub Actions, GitLab CI, and Jenkins, even if the platform itself is not instrumented.
• A hackish method was mentioned of replacing the shell on agents with one that has Hotel CLI enabled by default.
• An example of using Open Telemetry to create a shell wrapper that sends commands to Open Telemetry was discussed.
• Running Jenkins in production was touched upon, and it was noted that elastic uses Kubernetes for their modern Jenkins platform.
• Leverage flexibility of Docker containers to let development teams customize their build environment was recommended.
• Modern Jenkins management and the elimination of "Jenkins Plugin Hell"
• Running Jenkins and Kubernetes in production
• Deploying Jenkins using configurations, code, and infrastructure as code
• Packaging Jenkins into containers using tools like Helm charts
• Local development and testing of CI pipelines
• Deployment options for Jenkins in production, including use of Kubernetes and Helm charts
• Jenkins configuration as code
• Pipelines stored in repository with project
• Agent definitions stored in repository
• Entire Jenkins combination (server, login, config) as a single deliverable
• Configuring Jenkins using Kubernetes API or targeting Jenkins master directly
• Flexibility of deploying Jenkins and retrieving configurations without redeploying system
• Fire Hydrant platform and its features
• Incident response automation
• Separating CI (Continuous Integration) from CD (Continuous Deployment) pipelines
• Implementation of separate CI and CD tools (e.g. GetHub Actions, ArgoCD)
• Discussion on automating deployment processes and supply chain security
• KeylessH is currently used to watch images and automatically update when changes occur
• A desire to decouple deployment and integration concerns, allowing for multiple copies of production environments
• The use of CI/CD systems, with a focus on scalability concerns
• Jenkins is commonly used for pipeline development, along with GitHub Actions
• Pipeline libraries are created to implement common steps, such as deploying to Docker Hub or building Maven projects
• Test frameworks can be built for these pipelines to ensure they function correctly
• Jenkins plugin development and maintenance process
• Importance of standardizing CI/CD processes, managing them as a "kettle" rather than individual "pets"
• Security considerations for build systems and production environments
• Supply chain security within the CICD space and importance of dependency updates and scanning
• Open telemetry instrumentation for continuous delivery pipelines
• Audit trails and logs management for release and build processes
• Importance of capturing accurate information in the bill of material
• Verification and trust requirements for Jenkins and CI systems
• Incremental journey of verifying captured data and metadata on builds
• Integration of Captain Obvious with OpenTelemetry and Jenkins
• Exposure of quality gate information to enable verification
• Plans for integrating Captain with other tools and systems
• Update on the status of Captain Obvious project, including its integration into Cloud Native Computing Foundation
• Discussion of the vibrant community surrounding Captain Obvious
• Discussion about living in Switzerland
• Open source standard "open telemetry" for observing CICD pipelines
• Importance of exposing data from CICD processes
• Data analysis for optimizing pipelines and decision-making
• Standardization of open telemetry events
• Adoption and growth of the open telemetry ecosystem
• Future plans for donating code to the open telemetry community
• Progress on open telemetry Ansible integration
• Donating Ansible integration to the community
• Iterating and rolling out inside Elastic
• Jenkins evolution roadmap to be published soon
• Future projects in observability and open source