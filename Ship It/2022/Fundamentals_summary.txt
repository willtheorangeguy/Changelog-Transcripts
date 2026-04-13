• Running databases on Kubernetes
• Changelog.com database running on Kubernetes
• Kelsey Hightower's initial concerns about running databases on Kubernetes
• Importance of context and nuance when discussing complex topics like database management
• Use cases where running a database on Kubernetes might be suitable (e.g. small data, low risk)
• Managed services as an alternative to self-managed solutions in certain situations
• Balancing the value of running databases on Kubernetes with the potential risks and complexity
• The importance of keeping infrastructure self-contained
• Using Crossplane to interact with managed databases via Kubernetes
• Limitations of using Kubernetes as a hammer for every task
• The rise of declarative APIs and tools like Terraform and Crossplane
• Focusing on protocols rather than specific tools or vendors
• Replacing Kubernetes: Kelsey Hightower mentions Google Cloud's work on a potential replacement, including Knative and Cloud Run
• Kubernetes limitations in handling differences between infrastructure as a service (IaaS) providers
• Idea of replacing Kubernetes with platform-based approach that abstracts away complexity
• Examples of platforms like Cloud Run and Vercel that allow mixing and matching runtimes and APIs
• Discussion on the need for future platforms to simplify application development and deployment
• Concerns about vendor lock-in and the importance of being aware of emerging technologies
• Designing a technology stack for a new service
• Choosing between container-based frameworks like Docker and serverless platforms like Lambda
• Selecting protocols such as HTTP, REST, gRPC, and Pub/Sub for data transfer
• Implementing a content delivery network (CDN) for fast media serving
• Using edge functions to handle specific tasks close to the user
• Managing updates across distributed systems with limited team size
• Simplifying deployment and understanding complex architectures using endpoints and contracts
• Importance of clear contracts for developers to work efficiently
• Centralizing configuration and reducing complexity
• Source of truth: where to capture authoritative configuration data
• Documenting APIs and endpoints for external teams
• Using tools like Consul, Etcd, or Vault for central secrets storage and management
• Implementing role-based access control (RBAC) for configuration database
• Syncing tooling with the authoritative source of truth
• Principles for secrets management
• Vault as a tool for optimizing secrets management
• Etcd as an alternative to Vault for key-value storage
• Confd as a tool for fetching secrets from multiple sources and assembling templates
• Kubernetes and control planes versus data planes
• Running control planes outside of the controlled environment
• Using Cloud Run or Terraform to manage Vault instances
• Comparison to managed services like Letsencrypt
• Open source tools and protocols can be run on managed platforms like DigitalOcean or Google Cloud
• Let's Encrypt certificates are widely supported by cloud providers, reducing configuration complexity
• Focusing on protocol universality can reduce configuration management and automation needs
• Documentation and contract agreements between developers and users can simplify tool usage
• Companies like Azure, AWS, and Google Cloud provide comprehensive API documentation and support for various tools
• Terraform, HashiCorp's modules, and other tools enable automated deployment of complex systems
• Managed services, such as Atlassian's JIRA, offer a "click-and-go" experience for users
• Documenting manual processes first before automating them
• Importance of understanding fundamentals in application delivery
• Decoupling packaging from deployment
• Automation should be a by-product of understanding, not the source of truth
• Versioning and reproducibility are key to successful automation
• Understanding boundaries between concepts is crucial for effective tool adoption
• Overemphasis on automation has led to neglect of fundamental concepts