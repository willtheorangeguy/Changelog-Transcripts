• Hyper-growth followed by a bear market led to infrastructure challenges at Lemon Cash
• Monolithic codebase with 300+ developers made maintenance difficult
• Team recognized need for service-oriented architecture (SOA) but lacked infrastructure expertise
• Proposal aimed to tackle deployment and operational aspects of SOA
• Current infrastructure includes ECS, Lambda functions, Redshift cluster, Aurora database, and DMS
• Monolithic application still in production, causing issues with deployments and migrations
• Poor observability and monitoring hindered problem detection and resolution
• Incident with card payment failures caused by technical debt from not having a way to roll back migrations
• Fix involved scaling down service to zero and redeploying with manual intervention due to AWS ECS constraints
• Post-mortem analysis was conducted, including root cause analysis and action items for future improvement
• Incident management process has been improved with regular post-mortems and accountability through Monday meetings
• Discussion on the importance of turning problems into learning opportunities and improving processes rather than assigning blame
• Breaking down a monolith into microservices
• Current progress on splitting the monolith (6 new services out of 10-12 planned)
• Challenges in transitioning from a monolithic architecture, including technical debt and lack of standardization
• Infrastructure requirements for supporting microservices, including static and dynamic infrastructure
• Static resources such as databases, VPCs, S3 buckets, and Route 53 records
• Dynamic infrastructure, which has not yet been fully addressed
• Identifying static infrastructure and creating a list of it
• Centralizing static infrastructure to enable observability and cost ownership
• Using tools like TerraForm and Pulumi for managing static infrastructure
• Coupling static and dynamic infrastructure in development process
• Developers' role in specifying static infrastructure, with infrastructure team reviewing and challenging decisions
• Dynamic infrastructure: continuously deploying services, making them available, and ensuring security policies
• Using CI/CD to build, ship, and run changes safely
• Importance of developers understanding the state of their service in production.
• Developer creates new feature using Lemmy tool
• YAML abstraction hides complexity of ECS API
• Changes are pushed to central TerraForm repository with CI/CD files generated automatically
• Pipelines verify service definition and environment variables before deployment
• Merge to Develop branch triggers automatic deployment to Staging environment
• Discussion around naming conventions for branches and environments
• Thoughts on QA process, including possibility of production-only testing
• Current deployment issues with production environment and potential solutions
• Implementing feature branches to create infrastructure and test in an isolated way
• Optimizing time to production and its benefits (faster fixes, smaller changes)
• Requirements for services going into production (ports, health checks, etc.)
• Using conventions to simplify infrastructure setup and automation
• Limitations of port number choices
• Requirements for health checks and endpoint conventions
• Observability with metrics, tracing, and logs using Datadog
• Packaging process including build, integration tests, and end-to-end tests
• Docker image creation and deployment to ECR (Amazon Elastic Container Registry)
• Service naming convention based on GitHub repository names
• Convention over configuration and its benefits
• Using GitHub as a foundation for on-call and ownership processes
• Go language features, including automatic code formatting and standardization
• TerraForm modules and their use in simplifying infrastructure provisioning
• Limitations of ECS (Elastic Container Service) and the need for standardized traffic routing
• The challenges of transitioning from a monolith to microservices, including issues with infrastructure management.
• The difficulties of using TerraForm and managing dependencies between modules.
• The importance of slicing projects correctly to avoid feeling overwhelmed and making progress.
• The need for a central team to oversee the transition process in larger organizations.
• Importance of a central team in charge of breaking down a monolith application
• Need for the central team to be hands-on and make technical decisions themselves
• Scoping and slicing tasks into manageable pieces is crucial to avoid taking on too much at once
• Experience and teamwork are necessary to successfully break down a monolith application