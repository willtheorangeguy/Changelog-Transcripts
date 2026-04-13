• Discussion of Changelog.com's infrastructure changes since 2017
• Overview of previous infrastructure, including use of Ansible and Concourse
• Introduction of new Docker Swarm-based infrastructure
• Use of a custom makefile as a replacement for Ansible and other scripts
• Gerhard Lazu's experience with make, learned from his time at RabbitMQ team
• Discussion of make's features and benefits, such as simplicity and composibility
• Changelog.com's infrastructure and deployment process were previously complex and involved multiple tools, including Ansible, Docker, and Concourse CI.
• The application is Elixir-based and uses a Phoenix framework, with an NGINX proxy, Postgres database, and requirements for local file storage.
• The goal was to simplify the infrastructure and deployment process, using modern technologies and relying on Linode's load balancers and other features.
• Changelog.com is now a simple three-tier web app, with a Docker stack that describes the core components of the application.
• The Docker stack allows for local development and testing, and also enables easy deployment to production environments.
• A NodeBalancer is used for load balancing and SSL termination, and a CDN (Fastly) is used for caching static content and providing features such as IPv6 and HTTP/2.
• The use of a CDN allows for global content delivery and reduces the load on the Linode data center.
• IPv6 and HTTP/2 support through CDN provider
• Linode block storage limitations and comparison to object storage like S3
• Use of local storage for development ease and performance
• Alternative approach of choosing tools based on personal comfort and simplicity
• Replacement of Concourse CI with Circle CI for better integration with GitHub pull request flow
• Concourse vs Circle CI: reasons for switching to Circle CI, including complexity and lock-in
• Benefits of using Circle CI, such as simplicity and partner relationships
• Design of the CI/CD pipeline, including Docker and application updater
• Continuous deployment and monitoring process, including webhook notifications and health checks
• Transparency and openness in development and operations, including community involvement and documentation
• The benefits of open source and community-driven development
• Changelog's use of a monorepo for codebase and infrastructure
• Docker and Docker Compose for containerization and orchestration
• The self-updating Docker container and Application Updater
• The simplicity of the Application Updater's code and its location in the Changelog repository
• Docker service update and lifecycle management
• Blue-green deployment and automatic rolling updates
• Docker's internal IP and gateway for directing requests
• Health checks and updating the internal routing
• Database migrations and potential issues with breaking changes
• Alternatives to auto-rollback, such as separate database instances or manual intervention
• Complexity of distributed stateful systems and rolling upgrades
• Monitoring tools discussed: Rollbar, Pingdom, netdata, Papertrail, Prometheus, Grafana, InfluxDB
• Changelog's current monitoring setup: uses netdata for system metrics and Rollbar for application exceptions and error tracking
• Limitations of current setup: only stores metrics for last hour, due to memory constraints
• Future plans: to integrate Prometheus and Grafana for long-term metrics storage and visualization
• Business metrics discussed: tracking downloads, user engagement, and other metrics that require long-term storage and visualization
• Tools for business metrics: Prometheus, Grafana, InfluxDB, SQL queries
• Current implementation of business metrics: using Postgres and SQL to manually slice and dice data.
• Discussion of using Grafana to visualize metrics and explore data in an ad-hoc manner
• Comparison of Prometheus and InfluxDB for storing and managing metrics
• Benefits of using a system built for metric management, such as Grafana, to free up resources for high-value tasks
• Introduction of Grafana's new feature for exploring metrics and its potential for log aggregation with Loki
• Exploration of using Prometheus for tracking business metrics, particularly in a simple use case
• Discussion of considering Kubernetes for the Changelog.com stack, but currently deciding against it due to the difficulty of managing it oneself and the availability of managed services
• Linode's infrastructure has switched from Ubuntu to CoreOS, which comes with Docker pre-installed and automatic updates.
• The company is using Docker in Swarm mode and is planning to add more instances.
• Linode's managed Kubernetes wrapper is the core of their infrastructure, and Docker is a necessary component.
• The team is currently using Terraform to manage block storage, but they plan to switch to a Docker plugin for better management.
• The team is discussing areas for improvement, including automating stateful services and implementing HTTPS and IPv6.
• They are also considering using LetsEncrypt for automated SSL certificates.
• Discussion about the Linode API and integration with Changelog
• Issues with SSL, H2, and CDN, including slowdowns and 503 errors
• Proposal to improve CDN caching to reduce downtime in case of Linode issues
• Jerod's concern about prioritizing CDN improvements over other tasks
• Value of having a team with diverse expertise and experience
• Importance of understanding the complexities of deployment and infrastructure
• Invitation to the listening audience to share feedback and contribute to Changelog's roadmap
• Announcement of free access to Slack and the #dev channel
• Appreciation for the team's hard work on Changelog.com
• Reference to the website's origins on Tumblr
• Reminders of the website's motto: "Slow and steady wins the race"