• Alex Sims returns to Ship It six months after episode #49 to discuss the growth of James & James
• The company has fulfilled 15-20 million orders and expanded internationally with four fulfillment centers in the UK, US, and Auckland
• Alex discusses his role transition from senior engineer to solution architect and the company's move towards breaking down its monolithic application into smaller services
• The new services will use modern frameworks and allow for easier upgrades and maintenance
• The applications run on AWS with EC2 instances and a newly created EKS cluster, with plans to migrate legacy applications to the cluster
• Deploying new system with Kubernetes and feature flags
• Unexpected issue with cache driver causing lost progress and resetting users
• Use of feature flags to roll back deployment and minimize downtime
• Discussion on confidence and risk management when introducing new systems
• Reflection on mindset shift towards embracing change and iterating during busy periods
• Comparison of past practices (code-freezing) vs. current approach
• Sharing of lessons learned from recent incidents, including a mistake in reporting system
• System architecture challenges with high volume orders
• Identification and resolution of a performance bottleneck due to an AJAX request being fired multiple times
• Optimization of database queries through indexing and reducing column fetches
• Replacement of Redis keys command with scan to alleviate stress on Redis
• Upgrade from HDDs to SSDs (and potentially NVMEs) for improved disk performance
• Discussion about educated guesses made during troubleshooting, specifically around database issues
• Use of APM in Datadog for slow-running query detection and alarms
• Integrations with other tools, including RDS and Kafka for monitoring edge services
• Importance of a shared knowledge base for understanding system interactions and troubleshooting
• Limited use of play-by-plays and playbooks for common issues due to lack of permanent fixes
• Plans to improve documentation and incident response procedures
• Implementing SRE practices and SLIs/SLOs to improve incident response and system understanding
• Team management and scalability challenges with 12 people on the engineering team
• Using metrics and monitoring tools for incident investigation and root cause analysis
• Improving deployment pipelines and adding smoke tests for legacy systems
• Experience with Kubernetes and potential future use cases
• Peak season operations, including 24/7 order processing and employee involvement in system testing
• Deployment pipeline hardening
• Legacy application issues with deployment
• Potential for blue/green deployment strategy
• Migrating legacy app to Kubernetes
• Static asset management
• Successful Pick application rewrite
• Improved user experience through microservices architecture
• Implementing feature flags and Canary releases
• Creating SLIs (Service Level Indicators) and SLOs (Service Level Objectives)
• Developing a status page for stakeholders and clients
• Automating the packing process with sensors and conveyer belts
• Building bespoke software to monitor and improve efficiency in the warehouse
• Potential decrease in Kubernetes usage due to changes in infrastructure
• Kubernetes and cloud provider independence
• Datadog usage for monitoring and troubleshooting
• Real-time user monitoring (RUM) and end-to-end tracing
• Comparison with other tools such as Sentry and Honeycomb
• Importance of iterating and experimenting in production
• Overcoming fear through failure and learning
• Continuous improvement and iteration in software development