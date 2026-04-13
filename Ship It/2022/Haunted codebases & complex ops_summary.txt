• Code deployment from dev to prod
• Using observability and metrics for testing
• Blue-green deployments with canary traffic routing
• Simulating real users through bots to test system behavior
• Service meshes (e.g. K3s) and Kubernetes cluster setup
• Database management (Postgres, Zalando operator, Yugabyte, CockroachDB)
• Database issues with secondary promotion
• PostgreSQL replication challenges
• Backup and restore process
• Desire for stream replication to S3
• Managed PostgreSQL options (Fly)
• Discussion on DevOps vs NewOps
• Challenges of Kubernetes complexity for junior/mid-level developers
• Need for higher-level primitives and abstraction in Kubernetes
• Complexity of modern development platforms
• Familiarity with Heroku and Kubernetes
• Perceived complexity in managing various tools and ecosystems
• Comparison to JavaScript framework development
• Specific complexities in Kubernetes, including ecosystem growth and configuration diversity
• Difficulty finding relevant logs in complex systems
• Discussion of various logging tools, including Datadog, Loki, Cortex, and Grafana Cloud
• GDPR considerations and portability of logging solutions
• Lightweight Kubernetes alternative (K3s)
• Logging: Loki and Grafana instead of Elasticsearch
• Event handling: NATS
• Database: Evaluating Yugabyte for horizontal scalability
• Single-tenant clusters per customer, with different namespaces
• Provisoning: Customers start with one instance, scale up as needed
• Ingress management: Using Traefik
• External DNS: Considering Cloudflare APIs or ExternalDNS
• Code updates: Pipeline using Tekton, Git repo, and Harbor for image storage
• CLI tool for creating clusters (initially supporting Hetzner)
• Integrating Kubernetes with Hetzner servers
• Using KVM for virtualization and creating VMs on bare metal machines
• Choosing a lightweight Kubernetes distribution (K3s) and its limitations
• Operating system options for Kubernetes, including Talos OS, Flatcar, and NixOS
• Importance of operating systems designed specifically for Kubernetes
• Managed Kubernetes providers and their benefits
• Discussion on deploying applications via the Kubernetes API
• Description of "haunted codebases" where developers fear making changes due to unpredictable outcomes and long test suite run times
• Case study of a customer's codebase with a shared, slow test suite that caused delays and maintenance costs
• Use of metrics to measure test suite value and justify change decisions
• Psychological safety concerns when multiple teams share a test suite and must agree on changes
• Recommendation for prioritizing tests based on value and avoiding excessive testing
• Discussion of data processing and microservices architecture
• Fear of changing contracts between services due to implicit assumptions and lack of clear specifications
• Importance of explicit contract definition and management in microservices architecture
• Comparison of monolithic vs microservices approach with Erlang/Elixir as an example
• Debate on whether microservices is a technical or organizational solution to problems
• Discussion of DevOps considerations for microservices, including packaging and deployment
• Managing monolithic codebases in large teams and their potential drawbacks
• Google, GitHub, and Facebook's use of monorepos at scale
• Alternatives to microservices architecture, such as function-as-a-service approach
• Using tools like Knative for handling complexity in microservices
• Importance of questioning established practices and finding value in what you're doing
• Measuring pain points and deploying with minimal disruption
• Challenging assumptions around code reviews
• Discussing Ship/Show/Ask model for software development
• Critique of traditional pull request and code review processes
• Importance of system resilience and catching failures early on
• Discussion of the Kubernetes codebase and open source projects' experiences with code reviews
• Introduction to a new platform being developed by Robin Morero's team