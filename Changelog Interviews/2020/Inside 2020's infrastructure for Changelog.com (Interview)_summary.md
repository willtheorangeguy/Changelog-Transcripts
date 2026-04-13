• Gerhard Lazu's background and experience with infrastructure and breaking it down to understand its limits
• Changelog.com's infrastructure evolution, including previous episodes and setup changes
• Transition from Docker Swarm to Kubernetes, including challenges and benefits
• Linode Kubernetes Engine (LKE) and its one-click simplicity for setting up a Kubernetes cluster
• Comparison of simplicity between Docker Swarm and Kubernetes, including trade-offs and complexity
• Use of External DNS, cert-manager, and other mature components to simplify infrastructure management
• cert-manager is a Kubernetes component that extends the Kubernetes API with knowledge of certificates
• it allows users to request certificates through a single API, hiding the complexity of certificate management
• LKE (Linode Kubernetes Engine) made it easier to use cert-manager and other Kubernetes components
• managed Kubernetes provides a convenient and standardized way to manage clusters, including updates and integrations with other services
• declarative nature of Kubernetes allows users to describe what they want to happen, rather than how it should be done
• providers like Linode can offer curated Kubernetes experiences with built-in security, monitoring, logging, and other features
• the goal is to provide a standardized and easy-to-use way to manage Kubernetes clusters and applications
• Shift from manual scripting to declarative configuration with tools like YAML
• Kubernetes benefits, including automated reconvergence and VM management
• Changelog.com's experience with Linode Kubernetes Engine and its open-source implementation
• Practical applications of Kubernetes, including running web applications in production
• Customizing Kubernetes components, such as cert manager, NGINX Ingress, and DNS management
• Monitoring and metrics, including Grafana and Prometheus integration
• Deployment process from pushing a commit to GitHub to deploying in production
• Keel automation of Helm deployments and updates
• Comparison of Keel to GitOps and other approaches
• Separation of CI from deployment process
• Use of Circle CI to build and publish Docker images
• Keel's automated deployment process triggered by webhooks or periodic polls
• Readiness probes in Kubernetes to determine when a pod is ready to serve traffic
• Blue-green deployments and migration of database schema during updates
• Current deployment process relies on Keel, which automatically updates production instances
• GitOps is discussed as a more complex and explicit way to implement deployments
• GitOps allows defining application configurations in Git, including versioning and approvals for deployments
• Current setup may break idempotency and consistency due to using "latest" versions in production
• GitOps tools like Flux or ArgoCD can capture versioning and track changes, but require separate repositories
• Current setup has a single repository for code and infrastructure, making it hard to implement GitOps
• Potential solutions discussed include configuring CI to ignore certain commits or using GitOps tools with separate repositories.
• Keel as a simple tool for small teams
• Kubernetes cluster setup for high availability
• Testing resilience by simulating a node failure
• Deleting a node and observing the system's response
• Understanding the process behind the 10-minute recovery time
• Observing the system's behavior through events and logs
• Identifying the issue with the persistent volume claim
• Downtime and auto-healing process
• NodeBalancer and NGINX configuration
• Chaos engineering and manually introducing failures
• Previous downtime experience with Docker service not configured to automatically start
• Current failure and recovery process with Kubernetes and K9s
• Observability and monitoring tools, including K9s
• Recovery time and testing of auto-healing process
• K9s tool for Kubernetes clusters
• K9s award or recognition
• Gerhard's experience with K9s
• K9s developer, Fernand Galiana
• Kubernetes cluster migration and downtime
• DNS propagation and LetsEncrypt issues
• DNS TTL settings for External DNS
• DNS cache expiration settings and their impact on availability
• SLO (Service Level Objective) and SLI (Service Level Indicator) for measuring availability
• Instantaneous updates and the trade-off between availability and complexity
• Logging and metrics, including the need for better metrics and log aggregation
• Automating updates for container images, Kubernetes, and PostgreSQL
• Automation of data storage and updates
• Self-updating and self-healing systems
• Automated updates and rollouts
• Open-source contributions and community involvement
• LetsEncrypt implementation and automation
• Kubernetes and cloud-native services
• Community engagement and feedback
• Achieving four nines uptime next year
• Linode's future plans to move to five nines uptime
• Discussion of YAML and its complexities
• Introduction to Skylark, a templating language for YAML
• Overview of Ytt, a tool for shaping and manipulating YAML configurations