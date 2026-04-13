• Alex Sims returns to ShipIt.show six months after episode 49
• He discusses improving an e-commerce fulfillment platform with significant growth, including:
	+ From 15 million to almost 20 million orders in six months
	+ Expanding to four sites worldwide (UK, US, NZ)
	+ Plans for two more sites next year
• Alex's team migrated a monolithic PHP app to modern architecture with serverless and EKS
• The improved system coped well with Black Friday and Christmas peak demand
• The company James and James has received a large number of orders in recent months, with one of them being an LED sign that displays each dispatched order.
• The company provides 3PL (third-party logistics) services to clients, acting on their behalf to handle orders and shipping.
• The company's technical infrastructure is currently undergoing a migration from a monolithic architecture to a service-oriented architecture using Kubernetes.
• The company has created an EKS cluster for new services and is slowly transitioning legacy applications into the cluster.
• The company has rewritten one of its largest parts, PIC, as a new application using Remix and deployed it on the edge with Lambda, while the API is deployed inside the EKS cluster.
• Deploying new service using blue-green strategy
• Configuration error caused issues with cache driver
• Scaling from one to three nodes in Kubernetes cluster
• Incident occurred when users were redirected to new node and lost progress
• Feature flags used to roll back to old system and minimize downtime
• 30% of requests were degraded, but majority of users had a good experience
• Importance of feature flags for rolling forward and minimizing impact of incidents
• Confidence vs fear in decision-making
• Managing risk and uncertainty, especially in high-stakes situations like production systems
• Lessons learned from a recent mistake with the new system, including a failure that required fixing weeks of reporting data
• The impact of increased volume on the shipping industry, specifically during major events like Black Friday and Christmas
• Overview of the company's order volumes, including a spike to 31,000 orders on Black Friday
• Recent system changes, specifically "Label at Pack", caused performance issues and increased request times
• AJAX requests for printing labels were being fired multiple times, leading to significant delays (up to 30-40 seconds)
• The issue was resolved by changing the code to fire the AJAX request only once
• Other areas of the system slowed down due to high traffic of label-printing requests
• Performance issues also occurred on reporting pages due to:
	+ Legacy application using an ORM and overfetching data from the database
	+ Queries running out of memory buffer pool and then running on disk, causing significant performance degradation
	+ Upgrade from HDDs to SSDs was partially effective in addressing the issue
• The speaker discusses their system's performance issues leading up to Black Friday.
• They discovered and fixed a critical issue with Redis usage, switching from a blocking operation to a non-blocking one.
• Small changes made significant improvements in system performance.
• The importance of identifying the root cause of problems, rather than just writing more code.
• The process of identifying the problem involved connecting to the database, analyzing query execution plans, and making an educated guess about the issue being disk I/O related.
• The conversation shifts to a discussion with John Daniel Trask from Raygun about monitoring and observability in software development.
• Raygun APM and observability
• Datadog APM and integrations with other tools
• Troubleshooting slow SQL statements
• Importance of proactive identification of code smells
• Integrating multiple tools for comprehensive system monitoring
• Implementing a culture of knowledge sharing and tool literacy among team members
• Discussion of complexity in monitoring multiple applications, instances, and services
• Mention of service meshes and their role in understanding interactions between services during degradation
• Use of tools like SLIs (Service Level Indicators) and SLOs (Service Level Objectives) to improve understanding of system behavior
• Description of a wiki and play-by-plays for common issues, as well as alarm references that guide users through troubleshooting steps
• Need for more documentation across the platform to help with root cause analysis
• Discussion of using Slack for incident tracking and logging
• Use of SLIs and SLOs as new tools being implemented by the organization
• The value of creating SLIs (Service Level Indicators) and SLOs (Service Level Objectives)
• Managing a small team of 12 people, with everyone experiencing various aspects of the system
• Challenges of scaling the team beyond 20-30 people, including difficulty in achieving consensus and maintaining understanding of the system
• Implementing SLIs and SLOs as a tool for clarity and focus in a chaotic environment
• The importance of user experience and gathering feedback from operators to improve the system
• Rotating days where the development team spends time on the picking floor to gain insight into the system's performance
• Peak season operations at the company
• High volume order processing (300,000 orders in one day)
• Statistics on order processing speed (3.5 orders per second)
• Concerns about deployment and testing of legacy system
• Incidents with production downtime due to code changes
• Plans for hardening deployment pipeline to improve confidence in releases
• Discussion of using Bluegreen deployment strategy for legacy app
• Challenges and limitations of migrating legacy app to Kubernetes
• Static assets (e.g. JavaScript, CSS, images) being decoupled from app volume in legacy application
• Moving static assets to S3 and the benefits that came with it
• Issue with Docker container name vs host name causing internal resolution failure
• Troubleshooting issue where application is trying to access other service by hostname instead of container name due to legacy configuration
• Successes in system improvements, including a rewrite of PIC (Portal Information Console) application
• Transition from POC to PIC (production-ready microservices)
• Successfully implementing a new application with improved user experience in six months
• Implementing feature flags, Canary releases, and other new tooling for operational efficiency
• Establishing SLIs (Service Level Indicators) and SLOs (Service Level Objectives) for monitoring and improving system stability
• Creating a status page for stakeholders to view uptime and behind-the-scenes activity
• Discussion of the importance of real-time or near-real-time updates on the status page
• Deployment pipeline for legacy systems
• Future plans for automation in the warehouse, specifically automating the process of weighing and labeling orders
• Implementing sensors on conveyor belts to monitor order weights and detect errors
• Building SLOs (Service Level Objectives) and SLIs (Service Level Indicators) around the new automated system
• Combining software with real-world processes to improve efficiency and accuracy
• Company's bespoke systems for managing end-to-end fulfillment, including order ingest and dispatch
• Fulfillment center vs warehouse terminology
• Kubernetes usage and potential for future growth in the company
• Datadog service, its benefits, and ease of use
• Real-time user monitoring (RUM) feature within Datadog
• Use of Sentry and comparison to Datadog
• Honeycomb tooling and desire to integrate it with PHP SDK
• Importance of iterating and improving processes in production
• Replacing fear with courage through risk assessment and having a backout strategy
• The value of failing and learning from failures to improve confidence in deployments
• Keeping up with innovation and not accepting the status quo
• Continuous improvement and striving for better solutions
• Sharing knowledge and progress on architecture improvements
• Fastly's worldwide low-latency changelog.com
• Blazing fast MP3s for listeners
• Firecracker VMs and WireGuard integration by Fastly
• Flat.io mentioned
• Last Ship It episode of 2022
• Holiday wishes and New Year greetings
• Upcoming January episode of Ship It