• Tamer Saleh and Gerhard Lassil discuss their shared experience working in the same London office on Cloud Foundry
• They transition to discussing Kubernetes, its challenges, and their experience helping companies like Bloomberg and Shopify with DevOps problems
• Gerhard asks why companies need Kubernetes and what are the right reasons for choosing it
• Tamer's company, Super Orbital, offers engineering and training services to tackle hard Kubernetes and DevOps problems
• The conversation includes a humorous anecdote about table tennis culture at Pivotal and its decline with remote work
• Company has been fully remote since before the apocalypse, finding it easier to adapt
• Benefits of remote work include access to global talent and equal footing for all employees
• Remote work can also lead to cultural benefits by bringing people from different backgrounds together
• Cities are a strain on infrastructure and can create cultural divides; remote work can help flatten this divide
• Companies now see Kubernetes as necessary, rather than just interesting, with many seeking to implement it
• Challenges of implementing Kubernetes include its complexity, with many resource types and attributes to understand
• Kubernetes release cycle has slowed down to every three months
• Original authors of Kubernetes did not envision application developers directly using it
• Complexity of YAML in Kubernetes is significant and requires engineer knowledge
• Training for Kubernetes is a popular workshop topic due to complexity
• Customers struggle with on-premise installations, targeting 80% market share through Kubernetes
• Going on-premise is challenging, even with Kubernetes substrate, due to lack of telemetry and control
• Highly regulated customers require custom code development for health checks and security
• Integrating EKS with Nitro was challenging but successful
• Comparison of Cloud Foundry to Kubernetes in terms of management complexity
• Discussion of Bosch, a tool used for managing Cloud Foundry, and its similarities to Terraform and Ansible
• Explanation of the "great wall DevOps model" vs. the "kumbaya DevOps model"
• Observations on the use of YAML in Kubernetes and potential future changes
• General discussion of Kubernetes' ubiquity and ability to handle complexity
• Complex software modeling with Kubernetes
• Maturity level needed for data services
• Ubiquity of Kubernetes and its expected use
• Finding the right combination of objects or products in Kubernetes ecosystem
• Complexity and beauty of building blocks in Kubernetes community
• Trade-offs between using Kubernetes and other platforms for small teams
• Analogy between Linux on laptop experience and Kubernetes adoption
• Recommendation to stay on fully managed platforms for as long as possible
• Discussion of provisioning raw instances vs Kubernetes
• Importance of standardization in container technology
• Docker's role in popularizing containers and enabling Kubernetes' success
• History of container technology, including early versions like Solaris Zones and FreeBSD Jails
• Kubernetes' adoption and growth due to community excitement around Docker
• The speaker discusses how Kubernetes and Docker are often confused as being the same thing
• Docker is no longer a dependency for Kubernetes, but its standard is still used
• Understanding Docker concepts, such as container runtimes, is necessary to grasp Kubernetes
• Application developers don't need to be experts in crafting Dockerfiles, but rather understand the basics of Docker Compose and command-line tools
• Centralizing expertise in Dockerfile creation can help teams use Kubernetes effectively
• It's possible to use Kubernetes without a deep understanding of Docker
• The speaker shares their personal experience with starting with Docker before learning Kubernetes
• Importance of understanding Linux networking and general networking concepts for Kubernetes
• Use of managed Kubernetes services (EKS, AKS, GKE) over self-managed clusters due to cost and ease of use
• Risks and complexities associated with additional tooling such as Istio
• Need for restraint when adding new components or tools to a cluster
• Importance of understanding networking before diving into advanced features like Istio
• Examples of essential components (cert manager) versus nice-to-have components (Helm)
• Potential pitfalls in cluster management, including upgrade complexities and resource splitting
• Using Helm charts for internal applications is tedious and can be handled by simpler tools
• Automation is key when using Kubernetes, not just for cluster management but also for resource management within the cluster
• Investing in automation will save time and money in the long run
• Teams should focus on building an internal automation system, including CI/CD pipelines and GitOps
• Hiring experts or partnering with companies that specialize in Kubernetes can be beneficial to avoid wasted time and resources
• The importance of education for engineers when working with Kubernetes and cloud native technologies.
• The need for automation in the world of Kubernetes and cloud native.
• The spectrum of internal platforms, from simple Docker file management to full Heroku-style interfaces.
• The challenges of debugging and understanding complex systems like Kubernetes.
• The benefits of having multiple tools and services for monitoring and logging, such as Grafana Cloud and Honeycomb.
• Importance of observability in understanding application behavior
• EBPF and Pixie for deep insights into system performance
• Redundancies and failovers to minimize downtime
• Debugging challenges and the need for visibility into complex systems
• Observability and metrics as crucial investments, especially with Kubernetes
• The difficulty of building observability infrastructure without automation tools
• Feeding observability data back into automation for automated rollouts and error detection
• Simplifying Kubernetes setup through public sharing of configuration and components
• Inefficiencies in IT teams lead to wasted resources (20% CPU and memory usage)
• CIOs seek to reduce infrastructure costs by consolidating VMs into one massive cluster
• Kubernetes adoption was initially driven by cost savings, but operators saw benefits in its API and extensibility
• Operators found that large clusters can be difficult to manage and upgrade, leading to the concept of "fleets" (small, homogeneous clusters)
• Running small clusters per availability zone or workload type improves manageability and reduces costs
• Stateful workloads pose challenges for Kubernetes and should be handled with caution, either by externalizing databases or using teams to manage them
• Issues with PostgreSQL replication and networking
• Use of Crunchy data and Zalanda operators
• Comparison of managed vs self-managed PostgreSQL services
• Data backup and restore procedures
• Downtime and availability considerations for single instance PostgreSQL
• Trade-offs between feature complexity and simplicity in system design
• Serving stale content when origin is down
• Managed services for databases vs running own infrastructure
• Pitfalls of running multiple stateful sets in Kubernetes
• Technical debt and complexity associated with scaling database operations
• Importance of launching when necessary, rather than prematurely adopting complex solutions
• Delay Kubernetes adoption as long as possible
• Use existing managed platforms instead of managing Kubernetes installations
• Focus on automation and education when adopting Kubernetes
• Be prepared to spend "innovation points" on learning and implementing Kubernetes
• Kubernetes is more complicated than expected, with many configuration options and best practices.