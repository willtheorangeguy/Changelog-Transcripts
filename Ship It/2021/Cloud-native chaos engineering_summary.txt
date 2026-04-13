• Reliability of systems and infrastructure is often assumed, but failures can occur at any time
• Chaos engineering is a method for testing system resiliency by introducing artificial faults
• Importance of chaos engineering in preventing costly downtime and improving overall reliability
• Applying chaos engineering principles to specific systems such as CDNs and complex microservices environments
• Need for developers, SREs, and site reliability engineers to work together to fix root causes of failures
• Chaos engineering involves testing at multiple levels, including infrastructure dependencies and service reliability.
• Definition of chaos engineering
• Importance of steady-state hypothesis and understanding system behavior
• Injecting harm (faults) to build immunity (resilience)
• Scientifically trying to understand user happiness through metrics, logs, and events
• Willful fault injection to verify system behavior and identify tolerance limits
• Applying non-best practices in small doses for security and performance testing
• Chaos engineering as a practice to intentionally break and test systems to improve resilience
• Importance of learning from failures rather than successes in software development
• Applying chaos engineering to monolithic applications, not just microservices
• Tools and platforms for chaos engineering, such as LitmusChaos
• Best practices for implementing chaos engineering, including playing the role of a person outside the system, using good metrics and monitoring, and starting with small experiments in pre-production environments
• Litmus is an open-source, CNCF project that provides chaos engineering capabilities for Kubernetes environments.
• It can be installed as a Helm chart or operator with its own CRDs.
• The control plane of Litmus sets up the account and user access, while the agent infrastructure is where experiments are executed.
• Argo workflows are used to construct scenarios, and Argo CD integrates with Litmus for GitOps support.
• Litmus can be triggered by event tracker functionality via Argo CD updates or other GitOps tools.
• It supports storing chaos artifacts in Git, allowing changes to reflect on the chaos center.
• Users without Kubernetes can spin up a small cluster to use Litmus and create chaos scenarios for non-Kubernetes environments.
• Running databases on Kubernetes is discussed, with Uma expressing that it's becoming more feasible due to active community support.
• Stateful sites and distributed databases are key elements in Kubernetes
• Storage systems and containerized storage solutions (e.g. OpenEBS) are evolving for running databases on Kubernetes
• Networking issues, such as latency and packet loss, can impact database replication and performance
• Distributed application architecture, such as message brokers, can make it easier to run on Kubernetes
• Chaos engineering is essential for testing failures in Kubernetes environments and improving resilience
• Different platforms (e.g. AWS, GCP, Linode) have varying recovery times and require tailored approaches
• Infrastructure matters and needs to be considered when running databases on Kubernetes
• The importance of testing reliability in production, rather than just in staging
• Chaos engineering as a tool for simulating failures and improving system resilience
• The value of creating random triggers to test systems after changes are made in production
• The need for a culture of continuous chaos engineering at all levels of an organization
• The ultimate goal of chaos engineering is to be able to confidently break things in production, thereby ensuring system reliability